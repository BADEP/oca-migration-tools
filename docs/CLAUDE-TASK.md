# Prompt of the weekly Claude scheduled task

This is the exact prompt the scheduled task "BADEP · OCA weekly migration" runs with.
Keep it in sync when the process changes.

---

You are running BADEP's weekly OCA migration pass. Everything about the process is in the
GitHub repo `BADEP/oca-migration-tools`, branch `20.0`. Read `docs/PROCESS.md`,
`docs/GUIDELINES.md` and `config.yaml` first and follow them; where this prompt and the
repo disagree, the repo wins.

Setup
1. Attach `BADEP/oca-migration-tools` with push access, clone branch `20.0`, run
   `bash bootstrap.sh`.
2. Confirm `reports/20.0/last_scan.json` is from today (the GitHub Actions workflow
   runs two hours before you). If it is older than 24 h, trigger the workflow
   (`gh workflow run weekly-sync.yml`), wait for it to finish, pull, and continue. If it
   fails, stop here and report the failure.
3. Re-read the two OCA pages linked in `docs/GUIDELINES.md` (migration wiki for the
   target version, AI policy) so any change there is applied this run.

Relevancy
4. `python3 scripts/select_candidates.py relevancy` lists modules without a verdict.
   For each, delegate to a subagent on the model `config.migrate.models.relevancy` with
   the module's manifest summary and description from its source branch, and the
   question: is this functionality now native in Odoo <target> (`native-in-target`),
   explicitly deprecated or replaced upstream (`deprecated-upstream`), or otherwise
   `relevant`? Be permissive: when in doubt, `relevant`. Record each verdict with
   `scripts/select_candidates.py set-relevancy <repo> <module> <verdict> "<rationale>"`.
   Commit the CSVs.

Migrate
5. `python3 scripts/select_candidates.py migrate` returns the ordered list, already
   capped. Keep a clock: stop starting new modules once
   `config.migrate.time_budget_minutes` has elapsed since step 1.
6. For each module: attach `BADEP/<repo>` with push access, then run
   `bash scripts/migrate_module.sh <repo> <module> <source_branch> [dep PR refs from
   deps_blocking, "pr=" entries]`. Exit codes 10–12 mean a port or dependency conflict:
   do not fix by hand at this stage; note it in the CSV `notes` column and move on.
7. Open a PR on `BADEP/<repo>` from `20.0-mig-<module>` to `20.0`, title
   `[20.0][MIG] <module>: Migration to 20.0`, body: source branch, dependency PRs merged
   (if any), a one-line statement that the port was produced by BADEP's migration scripts
   with AI assistance and awaits human testing. Nothing else in the body.
8. Never open, comment on, or review anything in the OCA organisation.

Review and bloat detection
8a. For every module migrated or repaired this run:
    `python3 scripts/diff_stats.py <repo> <module> <source_branch>`. Record
    `substantive.added+deleted / source_lines` in the CSV column `diff_lines` via
    `select_candidates.py set-field … diff_lines "<added>+<deleted> / <source_lines>"`.
8b. If `needs_review` is true (thresholds in `config.review`), delegate to a review
    subagent on `config.review.model` (the task's default model) with: the substantive
    diff only (`git diff upstream/<source> origin/20.0-mig-<module> -- <module>`, minus
    the pre-commit and [DEP] commits), the migration wiki tasks, and the question: is
    every change explained by the version migration? It answers with labels from
    `config.review.labels` and one clause each. If the review finds unexplained
    changes, it may revert them (commit `[FIX] <module>: drop unneeded changes`,
    `Assisted-by:` trailer) and must then re-run 8a.
8c. Write the verdict with `select_candidates.py set-field … diff_review "<labels: clause>"`,
    for example `formatting; core-api-changes: _rec_names_search replaces name_search`.
    Below threshold, write `formatting` or `minimal` so the column is never empty for a
    migrated module. `bloat-suspected` or `needs-human` must also be mentioned in the
    PR body and in the run notes.

Repair
9. After the migrations are pushed, wait for CI on the new PRs (poll
   `gh pr checks` every few minutes, up to 40 minutes total). Then
   `python3 scripts/select_candidates.py repair` lists failing ones (including those from
   previous weeks). For each, one repair round: a subagent on
   `config.migrate.models.repair` receives the failing job log, the module diff, the
   migration wiki "tasks to do", and OpenUpgrade's `upgrade_analysis.txt` for the core
   modules in `depends`. It may only change files under `<module>/`, commits with
   `[FIX] <module>: <what>` plus the `Assisted-by:` trailer, pushes, and you re-check CI
   once. If still failing, leave it; the CSV shows `ci=fail` for the weekend review.
10. For PRs with green CI and `config.migrate.merge_into_target_when: ci_pass`: merge the
    PR into the fork's `20.0` (merge commit, no squash, branch kept).

Report
11. `python3 scripts/scan.py` on the repos you touched (so branch/PR/CI columns are
    fresh), then `python3 scripts/report.py`. Under "Notes from this run" in
    `reports/20.0/summary.md`, write at most ten lines: what was migrated, what failed and
    why in one clause each, anything that needs a human decision. Commit and push to
    `oca-migration-tools` `20.0`.
12. Your final message must be exactly three lines: counts (migrated / CI green / CI
    failing / skipped), the link
    `https://github.com/BADEP/oca-migration-tools/blob/20.0/reports/20.0/summary.md`,
    and one line on anything blocking. That message is what the email carries.

Rules
- Deterministic scripts first; AI only in steps 4 and 9. Do not hand-edit module code
  outside step 9.
- Use the cheapest model for plumbing (`config.migrate.models.plumbing`) and the
  configured models for relevancy, repair and the summary.
- If something needs an approval you cannot obtain unattended, skip that module, say so
  in the notes, and continue.
