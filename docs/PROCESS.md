# Process: keeping BADEP's OCA forks current and migrating missing modules

Branch of this repo = Odoo version being targeted (`20.0` now, `21.0` next year).
`config.yaml` holds the target and source versions; everything else derives from it.

## Principles

1. **Deterministic first.** Anything a script or an OCA tool can do is scripted
   (`scripts/`). AI is used for exactly two things: the *relevancy* verdict and
   *repairing* what the deterministic port leaves broken, after CI has said what is broken.
2. **OCA is the source of truth.** Our forks mirror OCA; our additions live on
   `<target>-mig-<module>` branches and, once CI passes, in the fork's `<target>` branch.
   On any conflict OCA wins and the module is flagged `self_maintained=no`.
3. **Nothing goes to OCA automatically.** The final OCA pull request is opened by a
   human, after manual testing, and only when every dependency exists on OCA's target
   branch ([AI policy](GUIDELINES.md#oca-ai-policy)).
4. **Never step on a claim.** A module announced on OCA's "Migration to version X"
   issue, or with an open `[X][MIG]` PR, is skipped (`claimed-by-others`).

## Branch model

```
OCA/<repo>:17.0 ──mirror──► BADEP/<repo>:17.0      (fast-forward only)
OCA/<repo>:18.0 ──mirror──► BADEP/<repo>:18.0
OCA/<repo>:19.0 ──mirror──► BADEP/<repo>:19.0
OCA/<repo>:20.0 ──merge───► BADEP/<repo>:20.0      = OCA 20.0 + our migrated modules
                 └──base───► BADEP/<repo>:20.0-mig-<module>   one branch per module,
                                                              always rebased on OCA/20.0
```

* `20.0-mig-<module>` starts from **OCA**/20.0, not from our 20.0, so the diff stays
  clean for the eventual OCA PR.
* Dependencies that only exist as an open OCA PR are **merged into** the
  `20.0-mig-<module>` branch (commit `[DEP] merge OCA/<repo>#N …`) so the branch can be
  tested in isolation by the fork's CI. They are stripped before the OCA PR.
* When CI passes, the branch is merged into BADEP/20.0 (local dev convenience).
* When OCA merges the module (ours or anyone's), the next sync replaces our copy with
  OCA's, deletes the `20.0-mig-*` branch and marks the module `merged-upstream`.

## The weekly run (Friday morning, Toronto)

### Part 1 — GitHub Actions (`.github/workflows/weekly-sync.yml`, 05:00)

Needs the `BADEP_GH_TOKEN` secret. Runs `scripts/sync_forks.py` → `scripts/scan.py` →
`scripts/report.py` and commits `reports/<target>/*.csv` + `summary.md`.

| script | does |
|---|---|
| `sync_forks.py` | create missing forks; ff source branches; merge OCA/target into ours (OCA wins); rebase our mig branches; delete mig branches merged upstream; register the fork's workflows so CI runs on our PRs (a fork runs none until a git push editing a workflow file lands on a branch its push trigger matches: one-line edit on a throwaway `<target>-ocabot-*` branch, deleted right after) |
| `scan.py` | per repo: modules missing on OCA/target, newest source branch, migration-issue claims, open `[MIG]` PRs, recursive dependency status (core / OCA target / open PR / missing), our branch & PR & CI state, PyPI downloads (`scan.downloads_window`), oca-port dry-run analysis (`scan.run_oca_port_dry_run`) |
| `report.py` | totals, per-repo table, delta vs. previous run |

### Part 2 — Claude scheduled task (07:00)

Prompt in [`docs/CLAUDE-TASK.md`](CLAUDE-TASK.md). Reads the fresh CSVs and:

Session prerequisites (learned 2026-10-23): the scheduled session must have **every BADEP
fork attached with push access** (`add_repo`; without it git push and the GitHub API answer
403 for `BADEP/<repo>` and steps 2–4 below are impossible) and **pypi.org /
files.pythonhosted.org allowed** in its network settings (`bootstrap.sh` installs
pre-commit and odoo-module-migrator from there). If those hosts are allowed but still do
not resolve, the sandbox proxy lists them in `NO_PROXY`: drop them (and `registry.npmjs.org`,
which pre-commit's prettier hook needs) from `NO_PROXY`, `no_proxy` and
`npm_config_noproxy` so pip and npm go through the proxy; otherwise pre-commit aborts
without running any hook. `bootstrap.sh` also sets the commit identity
(`config.migrate.commit_identity`, a human; never an AI tool). Schedule it after the Actions cron
(Friday 09:00 UTC), e.g. 11:00 UTC. Step 1 only needs `BADEP/oca-migration-tools` and git
read access to `OCA/*`.

1. **Relevancy** (`select_candidates.py relevancy`) — for each module without a verdict,
   an Opus subagent answers `relevant | native-in-target | deprecated-upstream` with a
   one-line rationale. Permissive: only clear cases skip. Written back with
   `select_candidates.py set-relevancy`. `overrides.csv` always wins.
2. **Migrate** (`select_candidates.py migrate`) — modules in `todo`, relevant, not
   claimed, ordered: manual priority → deps ready → most downloaded. Up to
   `max_modules_per_run` within `time_budget_minutes`. Per module:
   `scripts/migrate_module.sh <repo> <module> <source> [dep PRs…]`, then a PR against
   the fork's target branch (title `[20.0][MIG] <module>: Migration to 20.0`, concise
   body, AI assistance disclosed). The fork's own OCA CI workflow runs the tests.
2b. **Review & bloat detection** (`scripts/diff_stats.py`) — the change between the
   module on its source branch and the migrated branch, minus the pre-commit commit and
   dependency merges, is bucketed into python / xml / i18n / tests / docs / other net
   lines (same buckets as BADEP's original `oca_diff_report.py`). Zero code change →
   `formatting`; only a negative tests bucket → `tests-missing` (flagged for the weekend);
   anything else → a review subagent on the task's default model checks that every change
   is explained by the migration (e.g. a core model dropped), reverts what is not, and
   labels the result in `diff_review` (`core-api-changes`, `data-model-changes`,
   `tests-added`, `bloat-suspected`, `needs-human`). `diff_lines` holds the buckets;
   `scripts/diff_stats.py --all` regenerates `reports/<target>/diff_report.csv`.
3. **Repair** (`select_candidates.py repair`) — for fork PRs whose CI failed: an Opus
   subagent gets the CI log, the diff, the
   [20.0 migration tasks](https://github.com/OCA/maintainer-tools/wiki/Migration-to-version-20.0)
   and OpenUpgrade's `upgrade_analysis.txt` for the modules involved, fixes, pushes,
   waits for CI once more. One repair round per module per run.
4. **Merge into fork target** when CI is green (`merge_into_target_when`).
5. Re-runs `report.py`, appends a short paragraph under *Notes from this run*, commits,
   and ends with the link to `reports/<target>/summary.md` (that line is the email).

## Manual gate (weekend)

For every row in `pr-to-fork` / `merged-in-fork` with green CI:

1. Pull the branch into your local environment, test functionally.
2. If the module is `ready-for-upstream-pr` (all deps exist on OCA/target):
   * drop any `[DEP]` commits (`git rebase -i`), re-run CI,
   * announce on the repo's "Migration to version 20.0" issue,
   * open the OCA PR with the wiki's title pattern; keep the `Assisted-by:` trailer.
3. Anything you decide not to pursue: add a row in `overrides.csv`
   (`status_override=skip`) so the run stops proposing it.
4. Anything to push forward first: `status_override=priority`.

## CSV columns (`reports/<target>/<repo>.csv`)

`repo, module, source_branch, in_upstream_target, relevancy, relevancy_rationale,
claimed_by, upstream_open_pr, claim_age_days, downloads, oca_port, deps, deps_status,
deps_blocking, our_mig_branch, our_fork_pr, ci, diff_lines, diff_review, self_maintained,
status, last_run, notes`

Status lifecycle: `todo → in-progress → pr-to-fork → merged-in-fork →
ready-for-upstream-pr → upstream-pr-open → merged-upstream`, with side exits
`skipped-relevancy`, `claimed-by-others`, `blocked-by-deps`, `dropped`.

## Next Odoo version

Branch this repo (`git checkout -b 21.0`), set `target: "21.0"` and
`sources: ["20.0","19.0","18.0"]` in `config.yaml`, update the cron if needed, change the
scheduled task's branch. `reports/21.0/` starts empty.
