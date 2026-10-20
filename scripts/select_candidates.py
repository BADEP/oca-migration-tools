#!/usr/bin/env python3
"""Step 3 — what should the Claude task work on this week?

  select_candidates.py relevancy   -> JSON list of modules with no relevancy verdict yet
  select_candidates.py migrate     -> JSON list of modules to migrate, dependency-ordered,
                                      capped by config.migrate.max_modules_per_run
  select_candidates.py repair      -> JSON list of our fork PRs whose CI is failing
  select_candidates.py set-relevancy <repo> <module> <verdict> "<rationale>"
  select_candidates.py set-field <repo> <module> <column> "<value>"   (e.g. diff_review, notes)
"""
from __future__ import annotations

import json
import sys

from common import CONFIG, all_reports, read_report, write_report

MIG = CONFIG["migrate"]


def needing_relevancy():
    out = []
    for repo, rows in all_reports().items():
        for m, r in rows.items():
            if r["status"] in ("todo", "blocked-by-deps") and not r.get("relevancy"):
                out.append({"repo": repo, "module": m, "source_branch": r["source_branch"],
                            "deps": r["deps"]})
    return out


def migrate_candidates():
    reports = all_reports()
    priority = []
    normal = []
    for repo, rows in reports.items():
        for m, r in rows.items():
            if r["status"] != "todo":
                continue
            if not r.get("relevancy") or r["relevancy"] in MIG["skip_verdicts"]:
                continue
            item = {"repo": repo, "module": m, "source_branch": r["source_branch"],
                    "deps": r["deps"].split(), "deps_status": r["deps_status"],
                    "deps_blocking": r["deps_blocking"].split(),
                    "downloads": int(r.get("downloads") or 0)}
            (priority if "priority" in r.get("notes", "") else normal).append(item)
    # order: manual priority first, then deps ready before deps needing a PR merge,
    # then most-downloaded first (PyPI downloads of odoo-addon-<module>, window in config)
    key = lambda i: (i["deps_status"] != "ok", -i["downloads"], i["repo"], i["module"])
    ordered = sorted(priority, key=key) + sorted(normal, key=key)
    return ordered[: MIG["max_modules_per_run"]]


def repair_candidates():
    out = []
    for repo, rows in all_reports().items():
        for m, r in rows.items():
            if r["status"] == "pr-to-fork" and r.get("ci") == "fail":
                out.append({"repo": repo, "module": m, "pr": r["our_fork_pr"],
                            "branch": r["our_mig_branch"]})
    return out


def set_field(repo, module, column, value):
    rows = read_report(repo)
    if module not in rows:
        sys.exit(f"{repo}/{module} not in report")
    rows[module][column] = value
    write_report(repo, list(rows.values()))


def set_relevancy(repo, module, verdict, rationale):
    rows = read_report(repo)
    if module not in rows:
        sys.exit(f"{repo}/{module} not in report")
    rows[module]["relevancy"] = verdict
    rows[module]["relevancy_rationale"] = rationale
    if verdict in MIG["skip_verdicts"] and rows[module]["status"] in ("todo", "blocked-by-deps"):
        rows[module]["status"] = "skipped-relevancy"
    write_report(repo, list(rows.values()))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "migrate"
    if cmd == "relevancy":
        print(json.dumps(needing_relevancy(), indent=1))
    elif cmd == "migrate":
        print(json.dumps(migrate_candidates(), indent=1))
    elif cmd == "repair":
        print(json.dumps(repair_candidates(), indent=1))
    elif cmd == "set-relevancy":
        set_relevancy(*sys.argv[2:6])
    elif cmd == "set-field":          # set-field <repo> <module> <column> "<value>"
        set_field(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
