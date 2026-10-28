#!/usr/bin/env python3
"""Step 2 — build reports/<target>/<repo>.csv for every enabled repo.

Deterministic facts only. The `relevancy*` columns are filled later by the Claude
task (scripts/select_candidates.py prints what still needs a verdict); every other
column comes from git and the GitHub API.

Dependency resolution is recursive across all scanned repos plus Odoo core.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

from common import (CONFIG, ODOO_CORE_DIR, ORG, REPORT_DIR, SCRATCH, SOURCES, TARGET, UP, ci_state,
                    ensure_clone, fork_open_prs, list_modules, load_overrides, load_repos,
                    log, mig_branches, oca_port_dry_run, parse_migration_issue, pypi_downloads,
                    read_report, run,
                    upstream_migration_issue, upstream_open_mig_prs, write_report)

TODAY = dt.date.today().isoformat()


def path_of(repo):
    from common import clone_path
    return clone_path(repo)


def core_addons() -> set[str]:
    """Top-level addon names of odoo/odoo on the target branch (cached per run)."""
    cache = SCRATCH / f"core-{TARGET}.json"
    if cache.exists():
        return set(json.loads(cache.read_text()))
    if ODOO_CORE_DIR:
        # read-only use of an existing clone: no fetch, no checkout
        path = Path(ODOO_CORE_DIR)
        for ref in (f"origin/{TARGET}", TARGET):
            if run(["git", "rev-parse", "-q", "--verify", ref], cwd=path, check=False).returncode == 0:
                break
        else:
            raise SystemExit(f"ODOO_CORE_DIR={path} has no branch {TARGET}")
    else:
        path = SCRATCH / "odoo-core"
        if not (path / ".git").exists():
            run(["git", "clone", "--filter=tree:0", "--no-checkout", "--depth", "1", "-b", TARGET,
                 "https://github.com/odoo/odoo.git", str(path)])
        ref = "HEAD"
    names = run(["git", "ls-tree", "--name-only", f"{ref}:addons"], cwd=path).stdout.split()
    names += ["base", "web"]
    cache.write_text(json.dumps(sorted(names)))
    return set(names)


def scan_repo(repo: str) -> dict:
    path = ensure_clone(repo)
    per_branch = {b: list_modules(path, f"upstream/{b}") for b in SOURCES + [TARGET]}
    fork_target = list_modules(path, f"origin/{TARGET}")
    issue = upstream_migration_issue(repo)
    claims = parse_migration_issue(issue["body"]) if issue else {}
    up_prs = upstream_open_mig_prs(repo)
    our_prs = fork_open_prs(repo)
    our_mig = {b.removeprefix(f"{TARGET}-mig-") for b in mig_branches(path)}
    sync_notes = {}
    p = SCRATCH / f"sync-{repo}.json"
    if p.exists():
        sync_notes = json.loads(p.read_text())
    return {
        "repo": repo, "per_branch": per_branch, "fork_target": fork_target,
        "issue": issue, "claims": claims, "up_prs": up_prs, "our_prs": our_prs,
        "our_mig": our_mig, "sync": sync_notes,
    }


def build_rows(scans: dict[str, dict], core: set[str], overrides) -> dict[str, list[dict]]:
    # global index: where does a module live on the target branch upstream / in an open PR
    in_target = {}
    in_pr = {}
    in_source = {}
    for repo, s in scans.items():
        for m in s["per_branch"][TARGET]:
            in_target[m] = repo
        for m, pr in s["up_prs"].items():
            in_pr[m] = f"{UP}/{repo}#{pr['number']}"
        for b in SOURCES:
            for m, manifest in s["per_branch"][b].items():
                in_source.setdefault(m, (repo, b, manifest))

    def dep_status(mod, seen=None, depth=0):
        """Recursively classify dependencies. Returns (status, blocking list)."""
        seen = seen or set()
        if depth > CONFIG["scan"]["max_dependency_depth"]:
            return "ok", []
        info = in_source.get(mod)
        if not info:
            return "ok", []
        deps = info[2].get("depends", []) or []
        blocking = []
        status = "ok"
        for d in deps:
            if d in core or d in in_target or d in seen:
                continue
            seen.add(d)
            if d in in_pr:
                status = "needs-pr-merge"
                blocking.append(f"{d}:pr={in_pr[d]}")
                continue
            if d in in_source:
                status = "blocked"
                blocking.append(f"{d}:missing")
                sub_status, sub_block = dep_status(d, seen, depth + 1)
                blocking += sub_block
                continue
            status = "blocked"
            blocking.append(f"{d}:unknown")
        return status, blocking

    out = {}
    for repo, s in scans.items():
        prev = read_report(repo)
        rows = []
        all_source_mods = {}
        for b in SOURCES:  # newest first → first seen wins
            for m in s["per_branch"][b]:
                all_source_mods.setdefault(m, b)
        candidates = {m: b for m, b in all_source_mods.items() if m not in s["per_branch"][TARGET]}
        # also keep modules we touched that are now upstream, so the status is visible once
        for m in s["sync"].get("merged_upstream", []):
            candidates.setdefault(m, "")

        for module, source_branch in sorted(candidates.items()):
            old = prev.get(module, {})
            ov = overrides.get((repo, module), {})
            claim = s["claims"].get(module, {})
            up_pr = s["up_prs"].get(module)
            our_pr = s["our_prs"].get(module)
            manifest = s["per_branch"].get(source_branch, {}).get(module, {}) if source_branch else {}
            deps = manifest.get("depends", []) or []
            dstatus, dblock = dep_status(module)

            row = {c: old.get(c, "") for c in old} if old else {}
            row.update({
                "repo": repo, "module": module, "source_branch": source_branch,
                "in_upstream_target": "yes" if module in s["per_branch"][TARGET] else "no",
                "claimed_by": claim.get("claimed_by") or (up_pr["author"]["login"] if up_pr else ""),
                "upstream_open_pr": up_pr["url"] if up_pr else (f"#{claim['pr']}" if claim.get("pr") else ""),
                "claim_age_days": "",
                "downloads": pypi_downloads(module) or old.get("downloads", ""),
                "oca_port": (oca_port_dry_run(path_of(repo), repo, module, source_branch)
                             if CONFIG["scan"].get("run_oca_port_dry_run") and source_branch
                             and module not in s["per_branch"][TARGET]
                             else old.get("oca_port", "")),
                "deps": " ".join(deps),
                "deps_status": dstatus,
                "deps_blocking": " ".join(dblock),
                "our_mig_branch": f"{TARGET}-mig-{module}" if module in s["our_mig"] else "",
                "our_fork_pr": our_pr["url"] if our_pr else "",
                "ci": ci_state(our_pr),
                "self_maintained": old.get("self_maintained", "yes"),
                "last_run": TODAY,
                "notes": old.get("notes", ""),
            })
            if up_pr:
                created = dt.datetime.fromisoformat(up_pr["createdAt"].replace("Z", "+00:00")).date()
                row["claim_age_days"] = str((dt.date.today() - created).days)
            if module in s["sync"].get("self_maintained_no", []):
                row["self_maintained"] = "no"
                row["notes"] = (row["notes"] + " | " if row["notes"] else "") + f"{TODAY}: OCA changes overrode ours"

            # relevancy: override > previous verdict > empty (Claude fills)
            if ov.get("relevancy_override"):
                row["relevancy"] = ov["relevancy_override"]
                row["relevancy_rationale"] = "manual override"
            else:
                row.setdefault("relevancy", old.get("relevancy", ""))
                row.setdefault("relevancy_rationale", old.get("relevancy_rationale", ""))

            row["status"] = compute_status(row, module in s["per_branch"][TARGET], module in s["fork_target"], ov)
            rows.append(row)
        out[repo] = rows
    return out


def compute_status(row, in_upstream_target, in_fork_target, ov) -> str:
    if ov.get("status_override") == "skip":
        return "dropped"
    if in_upstream_target:
        return "merged-upstream"
    if row["relevancy"] in CONFIG["migrate"]["skip_verdicts"] or row["relevancy"] == "skip":
        return "skipped-relevancy"
    if row["upstream_open_pr"] and row["claimed_by"] != ORG.lower() and not row["our_mig_branch"]:
        return "claimed-by-others"
    if row["claimed_by"] and not row["our_mig_branch"]:
        return "claimed-by-others"
    if row["our_fork_pr"]:
        return "pr-to-fork"
    if in_fork_target and row["our_mig_branch"]:
        return "ready-for-upstream-pr" if row["deps_status"] == "ok" else "merged-in-fork"
    if row["our_mig_branch"]:
        return "in-progress"
    if row["deps_status"] == "blocked":
        return "blocked-by-deps"
    return "todo"


def main(repos):
    core = core_addons()
    overrides = load_overrides()
    scans = {}
    for repo in repos:
        try:
            scans[repo] = scan_repo(repo)
        except Exception as e:
            log(f"[{repo}] scan failed: {e}")
    for repo, rows in build_rows(scans, core, overrides).items():
        write_report(repo, rows)
    (REPORT_DIR / "last_scan.json").write_text(json.dumps({"date": TODAY, "repos": sorted(scans)}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:] or load_repos())
