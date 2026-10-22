#!/usr/bin/env python3
"""Step 4 — reports/<target>/summary.md: totals per status, and what changed since the
previous commit of the CSVs (new candidates, merged upstream, claimed by others,
unblocked, CI failures). Deterministic; the Claude task may append a short
human-written paragraph under "## Notes from this run".
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import subprocess
from collections import Counter, defaultdict

from common import REPORT_DIR, ROOT, STATUSES, TARGET, all_reports, report_csvs


def previous_reports() -> dict[str, dict[str, dict]]:
    out = {}
    for p in report_csvs():
        r = subprocess.run(["git", "show", f"HEAD:{p.relative_to(ROOT)}"], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode == 0:
            out[p.stem] = {row["module"]: row for row in csv.DictReader(io.StringIO(r.stdout))}
    return out


def main():
    now = all_reports()
    prev = previous_reports()
    counts = Counter()
    per_repo = defaultdict(Counter)
    changes = defaultdict(list)
    for repo, rows in now.items():
        for m, r in rows.items():
            counts[r["status"]] += 1
            per_repo[repo][r["status"]] += 1
            old = prev.get(repo, {}).get(m)
            key = f"{repo}/{m}"
            if old is None:
                changes["new candidates"].append(key)
            elif old["status"] != r["status"]:
                changes[f"{old['status']} → {r['status']}"].append(key)
            if r.get("ci") == "fail" and (old or {}).get("ci") != "fail":
                changes["CI failing on our fork PR"].append(f"{key} {r['our_fork_pr']}")
            if r.get("self_maintained") == "no" and (old or {}).get("self_maintained") != "no":
                changes["no longer self-maintained (OCA overrode)"].append(key)
        for m in prev.get(repo, {}):
            if m not in rows:
                changes["removed from report"].append(f"{repo}/{m}")

    lines = [f"# OCA → {TARGET} migration status", "",
             f"Generated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC · {len(now)} repos · {sum(counts.values())} modules tracked", "",
             "## Totals", "", "| status | modules |", "|---|---:|"]
    lines += [f"| {s} | {counts[s]} |" for s in STATUSES if counts[s]]
    lines += ["", "## Changes since last run", ""]
    if not changes:
        lines.append("_none_")
    for k, items in sorted(changes.items()):
        lines.append(f"### {k} ({len(items)})")
        lines += [f"- {i}" for i in sorted(items)[:200]]
        lines.append("")
    lines += ["## Per repo", "", "| repo | " + " | ".join(s for s in STATUSES if counts[s]) + " |",
              "|---|" + "---:|" * len([s for s in STATUSES if counts[s]])]
    for repo in sorted(per_repo):
        lines.append(f"| [{repo}]({repo}.csv) | " + " | ".join(str(per_repo[repo][s]) for s in STATUSES if counts[s]) + " |")
    lines += ["", "## Notes from this run", ""]
    (REPORT_DIR / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:40]))


if __name__ == "__main__":
    main()
