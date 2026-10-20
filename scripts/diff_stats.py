#!/usr/bin/env python3
"""Bloat detection — how much did the migration change the module, and of what kind?

  diff_stats.py <repo> <module> <source_branch>   -> JSON

Compares <module>/ on upstream/<source_branch> with the tip of <target>-mig-<module> and
splits the change into:
  formatting   lines touched by the "[IMP] <module>: pre-commit auto fixes" commit
  substantive  everything else (port conflicts resolved, odoo-module-migrator, MIG edits,
               AI repairs), net of formatting
  dep_merge    lines brought in by "[DEP] merge" commits (not the module's own change)

Verdict `needs_review` is true when substantive lines exceed config.review thresholds.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys

from common import CONFIG, TARGET, clone_path, run

REVIEW = CONFIG.get("review", {})


def numstat(path, a, b, pathspec):
    r = run(["git", "diff", "--numstat", a, b, "--", pathspec], cwd=path)
    add = dele = 0
    files = 0
    for line in r.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 3 or parts[0] == "-":
            continue
        add += int(parts[0]); dele += int(parts[1]); files += 1
    return {"added": add, "deleted": dele, "files": files}


def module_size(path, ref, module):
    r = run(["git", "ls-tree", "-r", "-l", ref, "--", module], cwd=path)
    lines = 0
    for line in r.stdout.splitlines():
        p = line.split("\t")[0].split()
        if len(p) >= 4 and p[3].isdigit() and not re.search(r"\.(png|jpg|gif|svg|ico|po|pot)$", line):
            blob = p[2]
            c = subprocess.run(["git", "cat-file", "-p", blob], cwd=path, capture_output=True, text=True)
            lines += c.stdout.count("\n")
    return lines


def main(repo, module, source):
    path = clone_path(repo)
    branch = f"{TARGET}-mig-{module}"
    run(["git", "fetch", "-q", "origin", branch], cwd=path, check=False)
    tip = f"origin/{branch}"
    src = f"upstream/{source}"
    total = numstat(path, src, tip, module)
    log = run(["git", "log", "--format=%H %s", f"upstream/{TARGET}..{tip}", "--", module], cwd=path).stdout.splitlines()
    formatting = {"added": 0, "deleted": 0, "files": 0}
    dep = {"added": 0, "deleted": 0, "files": 0}
    for line in log:
        sha, subject = line.split(" ", 1)
        if "pre-commit auto fixes" in subject:
            s = numstat(path, f"{sha}~1", sha, module)
        elif subject.startswith("[DEP]"):
            s = numstat(path, f"{sha}~1", sha, module)
            for k in dep: dep[k] += s[k]
            continue
        else:
            continue
        for k in formatting: formatting[k] += s[k]
    substantive = {k: max(0, total[k] - formatting[k] - dep[k]) for k in ("added", "deleted")}
    size = module_size(path, src, module) or 1
    ratio = (substantive["added"] + substantive["deleted"]) / size
    needs_review = (substantive["added"] + substantive["deleted"]) >= REVIEW.get("bloat_min_lines", 150) \
        and ratio >= REVIEW.get("bloat_ratio", 0.25)
    out = {"repo": repo, "module": module, "source": source, "source_lines": size,
           "total": total, "formatting": formatting, "dep_merge": dep, "substantive": substantive,
           "substantive_ratio": round(ratio, 3), "needs_review": needs_review,
           "commits": [l.split(" ", 1)[1] for l in log]}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:4])
