"""Shared helpers for the BADEP OCA migration scripts.

Everything here is deterministic: git, the GitHub CLI (`gh`, authenticated through
GH_TOKEN) and CSV files. No AI is involved at this layer.
"""
from __future__ import annotations

import ast
import csv
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field, fields
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text())
WORK = Path(os.environ.get("OCA_WORK_DIR", ROOT / ".work"))
WORK.mkdir(exist_ok=True)

ORG = CONFIG["org"]
UP = CONFIG["upstream_org"]
TARGET = str(CONFIG["target"])
SOURCES = [str(s) for s in CONFIG["sources"]]
REPORT_DIR = ROOT / "reports" / TARGET

CSV_COLUMNS = [
    "repo", "module", "source_branch", "in_upstream_target",
    "relevancy", "relevancy_rationale",
    "claimed_by", "upstream_open_pr", "claim_age_days",
    "downloads",
    "deps", "deps_status", "deps_blocking",
    "our_mig_branch", "our_fork_pr", "ci", "self_maintained",
    "status", "last_run", "notes",
]

# status values, in rough lifecycle order
STATUSES = [
    "todo",                 # missing in upstream target, nothing started
    "skipped-relevancy",    # relevancy verdict says skip
    "claimed-by-others",    # someone announced / opened a PR upstream
    "blocked-by-deps",      # a dependency is missing upstream and has no PR either
    "in-progress",          # our 20.0-mig-<module> branch exists
    "pr-to-fork",           # PR open against our fork's target branch
    "merged-in-fork",       # merged into our fork's target branch; waits for deps upstream
    "ready-for-upstream-pr",  # every dependency exists upstream; human opens the OCA PR
    "upstream-pr-open",     # our PR is open on OCA
    "merged-upstream",      # OCA merged it (ours or someone else's)
    "dropped",              # we stopped maintaining it (conflict with OCA, or override)
]


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def run(cmd, cwd=None, check=True, capture=True, env=None):
    log("$", " ".join(str(c) for c in cmd), f"(cwd={cwd})" if cwd else "")
    r = subprocess.run(cmd, cwd=cwd, check=False, text=True,
                       capture_output=capture, env=env)
    if check and r.returncode != 0:
        raise RuntimeError(f"command failed ({r.returncode}): {' '.join(map(str, cmd))}\n{r.stderr}")
    return r


def gh_json(args, repo=None):
    cmd = ["gh"] + args
    if repo:
        cmd += ["-R", repo]
    r = run(cmd, check=False)
    if r.returncode != 0:
        log("gh failed:", r.stderr.strip())
        return None
    try:
        return json.loads(r.stdout) if r.stdout.strip() else []
    except json.JSONDecodeError:
        return r.stdout


# ---------------------------------------------------------------- repos list

def load_repos() -> list[str]:
    """Enabled repos from repos.csv minus config exclusions."""
    out = []
    with open(ROOT / "repos.csv", newline="") as f:
        for row in csv.DictReader(l for l in f if not l.startswith("#")):
            name = row["repo"].strip()
            if not name or row.get("enabled", "true").strip().lower() not in ("true", "1", "yes"):
                continue
            if name in CONFIG.get("exclude_repos", []):
                continue
            if any(name.startswith(p) for p in CONFIG.get("exclude_repo_prefixes", [])):
                continue
            out.append(name)
    return out


def load_overrides() -> dict[tuple[str, str], dict]:
    out = {}
    p = ROOT / "overrides.csv"
    if not p.exists():
        return out
    with open(p, newline="") as f:
        for row in csv.DictReader(l for l in f if not l.startswith("#")):
            if row.get("repo") and row.get("module"):
                out[(row["repo"].strip(), row["module"].strip())] = row
    return out


# ---------------------------------------------------------------- git clones

def clone_path(repo: str) -> Path:
    return WORK / repo


def ensure_clone(repo: str) -> Path:
    """Clone of the BADEP fork with an `upstream` remote pointing at OCA.

    Fetches every source branch and the target branch from both remotes.
    """
    path = clone_path(repo)
    fork = f"https://github.com/{ORG}/{repo}.git"
    upstream = f"https://github.com/{UP}/{repo}.git"
    if not (path / ".git").exists():
        run(["git", "clone", "--filter=blob:none", "--no-checkout", fork, str(path)])
        run(["git", "remote", "add", "upstream", upstream], cwd=path)
    branches = SOURCES + [TARGET]
    run(["git", "fetch", "--prune", "origin"] + branches + [f"refs/heads/{TARGET}-mig-*:refs/remotes/origin/{TARGET}-mig-*"],
        cwd=path, check=False)
    run(["git", "fetch", "--prune", "upstream"] + branches, cwd=path, check=False)
    return path


def branch_exists(path: Path, ref: str) -> bool:
    return run(["git", "rev-parse", "--verify", "-q", ref], cwd=path, check=False).returncode == 0


def list_modules(path: Path, ref: str) -> dict[str, dict]:
    """{module_name: manifest_dict} for every addon on `ref` (an installable manifest)."""
    if not branch_exists(path, ref):
        return {}
    r = run(["git", "ls-tree", "--name-only", ref], cwd=path)
    mods = {}
    for name in r.stdout.split():
        if name.startswith(".") or name in ("setup",):
            continue
        m = run(["git", "show", f"{ref}:{name}/__manifest__.py"], cwd=path, check=False)
        if m.returncode != 0:
            continue
        try:
            manifest = ast.literal_eval(m.stdout)
        except Exception:
            manifest = {"_parse_error": True}
        if manifest.get("installable", True):
            mods[name] = manifest
    return mods


def mig_branches(path: Path) -> list[str]:
    r = run(["git", "branch", "-r", "--list", f"origin/{TARGET}-mig-*"], cwd=path)
    return [b.strip().removeprefix("origin/") for b in r.stdout.splitlines() if b.strip()]


# ---------------------------------------------------------------- GitHub reads

MIG_TITLE_RE = re.compile(r"\[(?P<ver>\d+\.\d+)\]\s*\[MIG\]\s*(?P<module>[a-z0-9_]+)", re.I)


def upstream_migration_issue(repo: str) -> dict | None:
    issues = gh_json(["issue", "list", "--state", "open", "--search",
                      f'"Migration to version {TARGET}" in:title', "--json",
                      "number,title,body,url", "--limit", "5"], repo=f"{UP}/{repo}") or []
    for i in issues:
        if i["title"].strip().lower() == f"migration to version {TARGET}":
            return i
    return issues[0] if issues else None


def parse_migration_issue(body: str) -> dict[str, dict]:
    """Parse the pinned issue body. Returns {module: {"claimed_by": str, "pr": str, "done": bool}}.

    Typical lines:
      - [ ] module_name - By @user - #123
      - [x] module_name - By @user - #123
      - [ ] module_name
    """
    out = {}
    for line in (body or "").splitlines():
        m = re.match(r"\s*-\s*\[(?P<done>[ xX])\]\s*(?P<module>[a-z0-9_]+)(?P<rest>.*)", line)
        if not m:
            continue
        rest = m.group("rest")
        by = re.search(r"@([A-Za-z0-9-]+)", rest)
        pr = re.search(r"#(\d+)|/pull/(\d+)", rest)
        out[m.group("module")] = {
            "done": m.group("done").lower() == "x",
            "claimed_by": by.group(1) if by else "",
            "pr": (pr.group(1) or pr.group(2)) if pr else "",
        }
    return out


def upstream_open_mig_prs(repo: str) -> dict[str, dict]:
    prs = gh_json(["pr", "list", "--state", "open", "--base", TARGET, "--search", "[MIG] in:title",
                   "--json", "number,title,url,author,createdAt,headRefName", "--limit", "200"],
                  repo=f"{UP}/{repo}") or []
    out = {}
    for pr in prs:
        m = MIG_TITLE_RE.search(pr["title"])
        if m and m.group("ver") == TARGET:
            out[m.group("module")] = pr
    return out


def fork_open_prs(repo: str) -> dict[str, dict]:
    prs = gh_json(["pr", "list", "--state", "open", "--base", TARGET,
                   "--json", "number,title,url,headRefName,statusCheckRollup", "--limit", "200"],
                  repo=f"{ORG}/{repo}") or []
    out = {}
    for pr in prs:
        head = pr.get("headRefName", "")
        if head.startswith(f"{TARGET}-mig-"):
            out[head.removeprefix(f"{TARGET}-mig-")] = pr
    return out


def ci_state(pr: dict | None) -> str:
    if not pr:
        return ""
    checks = pr.get("statusCheckRollup") or []
    if not checks:
        return "none"
    states = {(c.get("conclusion") or c.get("state") or "").upper() for c in checks}
    if any(s in ("FAILURE", "ERROR", "CANCELLED", "TIMED_OUT") for s in states):
        return "fail"
    if any(s in ("", "PENDING", "IN_PROGRESS", "QUEUED", "EXPECTED") for s in states):
        return "pending"
    return "pass"


# ---------------------------------------------------------------- PyPI downloads

def pypi_downloads(module: str) -> str:
    """Downloads of odoo-addon-<module> on PyPI (all Odoo versions) via pypistats.org,
    over config.scan.downloads_window: day | week | month | overall (~180 days retained).

    Empty string when unavailable (not published, rate limited, network blocked).
    """
    import urllib.request
    window = str(CONFIG["scan"].get("downloads_window", "overall"))
    pkg = f"odoo-addon-{module.replace('_', '-')}"
    try:
        if window == "overall":
            with urllib.request.urlopen(f"https://pypistats.org/api/packages/{pkg}/overall?mirrors=false", timeout=20) as r:
                data = json.load(r)
            return str(sum(d["downloads"] for d in data["data"]))
        with urllib.request.urlopen(f"https://pypistats.org/api/packages/{pkg}/recent?period={window}", timeout=15) as r:
            data = json.load(r)
        return str(data["data"][f"last_{window}"])
    except Exception:
        return ""


# ---------------------------------------------------------------- CSV I/O

def read_report(repo: str) -> dict[str, dict]:
    p = REPORT_DIR / f"{repo}.csv"
    if not p.exists():
        return {}
    with open(p, newline="") as f:
        return {r["module"]: r for r in csv.DictReader(f)}


def write_report(repo: str, rows: list[dict]):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    p = REPORT_DIR / f"{repo}.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda r: r["module"]):
            w.writerow({c: r.get(c, "") for c in CSV_COLUMNS})
    log("wrote", p)


def all_reports() -> dict[str, dict[str, dict]]:
    out = {}
    for p in sorted(REPORT_DIR.glob("*.csv")):
        out[p.stem] = read_report(p.stem)
    return out
