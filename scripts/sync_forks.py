#!/usr/bin/env python3
"""Step 1 — keep the BADEP forks in sync with OCA.

For every enabled repo:
  * create the fork if missing (needs a token with org repo-creation rights)
  * source branches (19.0, 18.0, 17.0): fast-forward the fork to OCA; divergence is
    reported, never forced
  * target branch (20.0): merge OCA/20.0 into BADEP/20.0.
      - a module that exists on both sides because OCA merged it (ours or someone
        else's): OCA's copy replaces ours wholesale, our 20.0-mig-<module> branch
        is deleted, status -> merged-upstream
      - any other conflict: OCA's side wins, the module is marked self_maintained=no
  * every surviving 20.0-mig-<module> branch is rebased on the fresh OCA/20.0 so the
    migration branch always starts from upstream

Writes sync notes into `<OCA_SCRATCH_DIR>/sync-<repo>.json` which scan.py merges into the CSV.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

from common import (CONFIG, ORG, SCRATCH, SOURCES, TARGET, UP, branch_exists, clone_path,
                    ensure_clone, gh_json, list_modules, load_repos, log, mig_branches, run)


def ensure_fork(repo: str) -> bool:
    if gh_json(["repo", "view", f"{ORG}/{repo}", "--json", "name"]) is not None:
        return True
    if not CONFIG["sync"].get("create_missing_forks", True):
        log(f"[{repo}] fork missing and create_missing_forks=false")
        return False
    r = run(["gh", "repo", "fork", f"{UP}/{repo}", "--org", ORG, "--clone=false",
             "--default-branch-only=false"], check=False)
    if r.returncode != 0:
        log(f"[{repo}] fork creation failed: {r.stderr.strip()}")
        return False
    log(f"[{repo}] fork created")
    return True


def ensure_actions_enabled(repo: str, notes: dict):
    """Forks have Actions disabled by default; OCA's test.yml is what tests our PRs.
    Public repos: unlimited free minutes."""
    cur = gh_json(["api", f"repos/{ORG}/{repo}/actions/permissions"])
    if isinstance(cur, dict) and cur.get("enabled"):
        return
    r = run(["gh", "api", "-X", "PUT", f"repos/{ORG}/{repo}/actions/permissions",
             "-F", "enabled=true", "-f", "allowed_actions=all"], check=False)
    notes["actions"] = "enabled" if r.returncode == 0 else f"enable failed: {r.stderr.strip()[:120]}"


def register_workflows(path, repo: str, notes: dict):
    """Enabling Actions is not enough on a fork: GitHub only registers its workflows when
    a git push that edits a workflow file lands on a branch matching that workflow's push
    trigger (a commit made through the contents API does not count). OCA's test.yml
    triggers on <target>-ocabot-*, so a one-line edit pushed to a throwaway branch of that
    name registers them without touching <target>; the branch and its runs are removed."""
    api = f"repos/{ORG}/{repo}"
    wf = gh_json(["api", f"{api}/actions/workflows"])
    if not isinstance(wf, dict) or wf.get("total_count"):
        return
    wf_path = ".github/workflows/test.yml"
    text = run(["git", "show", f"origin/{TARGET}:{wf_path}"], cwd=path, check=False).stdout
    if f"{TARGET}-ocabot-" not in text:
        notes["actions"] = f"workflows not registered: no test.yml triggering on {TARGET}-ocabot-*"
        return
    branch = f"{TARGET}-ocabot-register-workflows"
    # build the commit with plumbing on a private index: the clone's checkout is untouched
    text += ("" if text.endswith("\n") else "\n") + "# registers this fork's workflows\n"
    blob = subprocess.run(["git", "hash-object", "-w", "--stdin"], cwd=path, input=text,
                          capture_output=True, text=True, check=True).stdout.strip()
    env = dict(os.environ, GIT_INDEX_FILE=str(SCRATCH / f"register-{repo}.index"))
    run(["git", "read-tree", f"origin/{TARGET}"], cwd=path, env=env)
    run(["git", "update-index", "--cacheinfo", f"100644,{blob},{wf_path}"], cwd=path, env=env)
    tree = run(["git", "write-tree"], cwd=path, env=env).stdout.strip()
    commit = run(["git", "commit-tree", tree, "-p", f"origin/{TARGET}", "-m",
                  "[CI] register this fork's workflows (temporary branch)"], cwd=path).stdout.strip()
    try:
        run(["git", "push", "-q", "origin", f"{commit}:refs/heads/{branch}"], cwd=path)
        for _ in range(12):
            time.sleep(5)
            wf = gh_json(["api", f"{api}/actions/workflows"])
            if isinstance(wf, dict) and wf.get("total_count"):
                break
        notes["actions"] = ("workflows registered" if isinstance(wf, dict) and wf.get("total_count")
                            else "workflows not registered after 60s")
    finally:
        # the push starts a run per workflow, a few seconds after registration: wait for them
        expected = wf.get("total_count", 0) if isinstance(wf, dict) else 0
        for _ in range(6):
            runs = gh_json(["api", f"{api}/actions/runs?branch={branch}"]) or {}
            found = runs.get("workflow_runs", []) if isinstance(runs, dict) else []
            if len(found) >= expected:
                break
            time.sleep(5)
        for r in found:
            run(["gh", "api", "-X", "POST", f"{api}/actions/runs/{r['id']}/cancel"], check=False)
        run(["git", "push", "-q", "origin", "--delete", branch], cwd=path, check=False)
        (SCRATCH / f"register-{repo}.index").unlink(missing_ok=True)
    log(f"[{repo}] {notes.get('actions', 'workflows not registered')}")


def sync_source_branch(path, repo, branch, notes):
    if not branch_exists(path, f"upstream/{branch}"):
        return
    if not branch_exists(path, f"origin/{branch}"):
        run(["git", "push", "origin", f"upstream/{branch}:refs/heads/{branch}"], cwd=path)
        notes["branches"][branch] = "created"
        return
    r = run(["git", "merge-base", "--is-ancestor", f"origin/{branch}", f"upstream/{branch}"],
            cwd=path, check=False)
    if r.returncode == 0:
        run(["git", "push", "origin", f"upstream/{branch}:refs/heads/{branch}"], cwd=path)
        notes["branches"][branch] = "fast-forwarded"
    else:
        notes["branches"][branch] = "DIVERGED — not touched (fork has commits OCA does not)"
        log(f"[{repo}] {branch} diverged; left as is")


def sync_target_branch(path, repo, notes):
    up = f"upstream/{TARGET}"
    ours = f"origin/{TARGET}"
    if not branch_exists(path, up):
        notes["branches"][TARGET] = "upstream branch missing"
        return
    if not branch_exists(path, ours):
        run(["git", "push", "origin", f"{up}:refs/heads/{TARGET}"], cwd=path)
        notes["branches"][TARGET] = "created"
        return

    run(["git", "checkout", "-q", "-B", TARGET, ours], cwd=path)
    before = list_modules(path, ours)
    up_mods = list_modules(path, up)
    our_mig = {b.removeprefix(f"{TARGET}-mig-") for b in mig_branches(path)}

    # modules OCA has merged that we also carried: take OCA's version wholesale
    merged_upstream = sorted(m for m in our_mig if m in up_mods)
    for m in merged_upstream:
        run(["git", "rm", "-rq", "--ignore-unmatch", m], cwd=path)
        run(["git", "checkout", up, "--", m], cwd=path, check=False)
    if merged_upstream:
        run(["git", "commit", "-qm", f"[SYNC] take upstream copy of {', '.join(merged_upstream)}"],
            cwd=path, check=False)

    r = run(["git", "merge", "--no-edit", "-X", "theirs", up], cwd=path, check=False)
    conflicted = []
    if r.returncode != 0:
        # -X theirs resolves content conflicts; what remains are add/add or delete/modify
        st = run(["git", "status", "--porcelain"], cwd=path).stdout.splitlines()
        for line in st:
            code, p = line[:2], line[3:]
            if code.strip() and code[0] in "UDA" and code[1] in "UDA":
                mod = p.split("/", 1)[0]
                conflicted.append(mod)
                run(["git", "checkout", "--theirs", "--", p], cwd=path, check=False)
                run(["git", "add", "-A", "--", p], cwd=path, check=False)
        run(["git", "-c", "core.editor=true", "merge", "--continue"], cwd=path, check=False)
        if run(["git", "rev-parse", "-q", "--verify", "MERGE_HEAD"], cwd=path, check=False).returncode == 0:
            run(["git", "merge", "--abort"], cwd=path, check=False)
            notes["branches"][TARGET] = "MERGE FAILED — manual attention"
            log(f"[{repo}] merge of {up} failed; aborted")
            return

    # detect modules where OCA overrode our content (self-maintained no more)
    after = list_modules(path, "HEAD")
    overridden = sorted(set(conflicted))
    for m in our_mig:
        if m in up_mods and m not in merged_upstream:
            overridden.append(m)
    run(["git", "push", "origin", f"HEAD:refs/heads/{TARGET}"], cwd=path)
    notes["branches"][TARGET] = "merged from upstream"
    notes["merged_upstream"] = merged_upstream
    notes["self_maintained_no"] = sorted(set(overridden))

    # cleanup branches for modules now upstream
    for m in merged_upstream:
        run(["git", "push", "origin", "--delete", f"{TARGET}-mig-{m}"], cwd=path, check=False)
        notes["deleted_branches"].append(f"{TARGET}-mig-{m}")

    # rebase surviving mig branches on fresh upstream target — only the module's own
    # commits. Pre-existing branches may have been cut from BADEP/<target> (which carries
    # other migrations), so rebase --onto from the merge-base with our target branch.
    # A branch already merged into our target is left alone: it is history now.
    for b in mig_branches(path):
        m = b.removeprefix(f"{TARGET}-mig-")
        if m in merged_upstream:
            continue
        if run(["git", "merge-base", "--is-ancestor", f"origin/{b}", "origin/" + TARGET],
               cwd=path, check=False).returncode == 0:
            notes.setdefault("merged_in_fork", []).append(m)
            continue
        base = run(["git", "merge-base", f"origin/{b}", f"origin/{TARGET}"], cwd=path, check=False).stdout.strip()
        if not base:
            notes["rebase_conflicts"].append(m + " (no merge-base)")
            continue
        if run(["git", "merge-base", "--is-ancestor", up, base], cwd=path, check=False).returncode == 0 \
                and run(["git", "merge-base", "--is-ancestor", up, f"origin/{b}"], cwd=path, check=False).returncode == 0:
            continue  # already on top of current upstream target
        run(["git", "checkout", "-q", "-B", b, f"origin/{b}"], cwd=path)
        rr = run(["git", "rebase", "--onto", up, base], cwd=path, check=False)
        if rr.returncode != 0:
            run(["git", "rebase", "--abort"], cwd=path, check=False)
            notes["rebase_conflicts"].append(m)
            log(f"[{repo}] {b} does not rebase cleanly on {up}")
            continue
        run(["git", "push", "--force-with-lease", "origin", b], cwd=path, check=False)
        notes.setdefault("rebased", []).append(m)
    run(["git", "checkout", "-q", TARGET], cwd=path, check=False)


def main(repos):
    for repo in repos:
        notes = {"repo": repo, "branches": {}, "merged_upstream": [], "self_maintained_no": [],
                 "deleted_branches": [], "rebase_conflicts": [], "fork": "ok"}
        try:
            if not ensure_fork(repo):
                notes["fork"] = "missing"
                continue
            ensure_actions_enabled(repo, notes)
            path = ensure_clone(repo)
            for b in SOURCES:
                sync_source_branch(path, repo, b, notes)
            sync_target_branch(path, repo, notes)
            register_workflows(path, repo, notes)
        except Exception as e:  # keep going; one repo must not sink the run
            notes["error"] = str(e)[:500]
            log(f"[{repo}] ERROR {e}")
        finally:
            (SCRATCH / f"sync-{repo}.json").write_text(json.dumps(notes, indent=1))
            log(f"[{repo}]", json.dumps(notes))


if __name__ == "__main__":
    main(sys.argv[1:] or load_repos())
