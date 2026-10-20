#!/usr/bin/env python3
"""Change report for a migrated module — the bloat / review trigger.

  diff_stats.py <repo> <module> <source_branch>            -> JSON for one module
  diff_stats.py --all                                       -> CSV of every migrated module
                                                               (reports/<target>/diff_report.csv)

Compares <module>/ on upstream/<source_branch> with the tip of <target>-mig-<module>.
Net changed lines (added - deleted, may be negative) are bucketed like the original
BADEP oca_diff_report.py: python, xml, i18n, tests, docs, other. Anything under tests/
is "tests" whatever the extension; binary files count 0.

The pre-commit commit ("[IMP] <module>: pre-commit auto fixes") and "[DEP] merge"
commits are subtracted so the buckets show substantive change only.

Review rule (config.review): no deep review when the substantive diff is zero within
`tolerance_lines`, or when the only non-zero bucket is a negative `tests` (test suite
missing: flagged, not reviewed). Everything else -> needs_review=true.
"""
from __future__ import annotations

import csv
import json
import os
import sys
from collections import defaultdict

from common import CONFIG, REPORT_DIR, TARGET, all_reports, clone_path, ensure_clone, run

COLS = ["python", "xml", "i18n", "tests", "docs", "other"]
REVIEW = CONFIG.get("review", {})


def classify(rel: str) -> str:
    parts = rel.split("/")
    name = parts[-1].lower()
    ext = os.path.splitext(name)[1]
    if "tests" in parts[:-1]:
        return "tests"
    if "i18n" in parts[:-1] or ext in (".po", ".pot"):
        return "i18n"
    if ext in (".md", ".rst", ".txt") and (len(parts) == 1 or parts[0] in ("readme", "static")):
        return "docs"
    if ext in (".md", ".rst"):
        return "docs"
    if ext == ".html" and (parts[0] == "readme" or parts[:2] == ["static", "description"]):
        return "docs"
    if ext == ".py":
        return "python"
    if ext == ".xml":
        return "xml"
    return "other"


def bucketed_numstat(path, a, b, module) -> dict[str, int]:
    out = dict.fromkeys(COLS, 0)
    r = run(["git", "diff", "--numstat", "--no-renames", a, b, "--", module], cwd=path)
    for line in r.stdout.splitlines():
        add, dele, p = line.split("\t", 2)
        if add == "-":
            continue
        _, _, rel = p.partition("/")
        if rel:
            out[classify(rel)] += int(add) - int(dele)
    return out


def sub(a, b):
    return {k: a[k] - b.get(k, 0) for k in COLS}


def stats(repo, module, source) -> dict:
    path = clone_path(repo)
    if not (path / ".git").exists():
        ensure_clone(repo)
    branch = f"{TARGET}-mig-{module}"
    run(["git", "fetch", "-q", "origin", branch], cwd=path, check=False)
    run(["git", "fetch", "-q", "upstream", source, TARGET], cwd=path, check=False)
    tip, src = f"origin/{branch}", f"upstream/{source}"
    total = bucketed_numstat(path, src, tip, module)
    formatting = dict.fromkeys(COLS, 0)
    dep = dict.fromkeys(COLS, 0)
    commits = run(["git", "log", "--format=%H %s", f"upstream/{TARGET}..{tip}", "--", module],
                  cwd=path).stdout.splitlines()
    for line in commits:
        sha, subject = line.split(" ", 1)
        if "pre-commit auto fixes" in subject:
            s = bucketed_numstat(path, f"{sha}~1", sha, module)
            formatting = {k: formatting[k] + s[k] for k in COLS}
        elif subject.startswith("[DEP]"):
            s = bucketed_numstat(path, f"{sha}~1", sha, module)
            dep = {k: dep[k] + s[k] for k in COLS}
    substantive = sub(sub(total, formatting), dep)
    tol = int(REVIEW.get("tolerance_lines", 0))
    code = {k: v for k, v in substantive.items() if k in ("python", "xml", "other") and abs(v) > tol}
    tests_missing = substantive["tests"] < -tol
    needs_review = bool(code) or substantive["docs"] > tol * 10
    if not code and tests_missing:
        verdict = "tests-missing"
    elif not code:
        verdict = "formatting"
    else:
        verdict = "review"
    return {"repo": repo, "module": module, "source": source,
            "total": total, "formatting": formatting, "dep_merge": dep, "substantive": substantive,
            "tests_missing": tests_missing, "needs_review": needs_review, "auto_verdict": verdict,
            "commits": [l.split(" ", 1)[1] for l in commits]}


def main_all():
    rows = []
    for repo, report in all_reports().items():
        for m, r in report.items():
            if r.get("our_mig_branch") and r.get("source_branch"):
                try:
                    s = stats(repo, m, r["source_branch"])
                except Exception as e:
                    s = {"repo": repo, "module": m, "substantive": dict.fromkeys(COLS, ""), "auto_verdict": f"error: {e}"[:80],
                         "needs_review": ""}
                rows.append([repo, m] + [s["substantive"][c] for c in COLS] + [s["auto_verdict"], s["needs_review"]])
    out = REPORT_DIR / "diff_report.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["repo", "module"] + COLS + ["auto_verdict", "needs_review"])
        w.writerows(sorted(rows))
    print(f"{len(rows)} rows -> {out}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        main_all()
    else:
        print(json.dumps(stats(*sys.argv[1:4]), indent=1))
