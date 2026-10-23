# OCA guidelines this process adheres to

Links are the source of truth; the notes below are what the scripts implement. Re-read
the linked pages when they change (the Claude task re-reads them every run).

## Migration guide for the target version

<https://github.com/OCA/maintainer-tools/wiki/Migration-to-version-20.0>

Implemented in `scripts/migrate_module.sh`:

* branch `20.0-mig-<module>` from OCA/20.0;
  `git format-patch --keep-subject --stdout origin/20.0..origin/<source> -- <module> | git am -3 --keep`
  (with `--ignore-whitespace` fallback as the wiki's troubleshooting section suggests)
* `pre-commit run -a` committed once as `[IMP] <module>: pre-commit auto fixes`
* bump version to `20.0.1.0.0` (a reset, not a series swap: `18.0.3.5.2` becomes `20.0.1.0.0`); remove `migrations/`; remove past financed-migration
  lines from `readme/CREDITS.rst`
* final commit `[MIG] <module>: Migration to 20.0`
* **not** done: changing copyright years or original authors
* wiki "tasks to do" not covered by the script, checked by the review and repair subagents
  (keep this list in sync with the wiki): since 2026-10-19 the widget `selection_badge` is
  split into `badges_selection` (selection fields) and `badges_many2one` (many2one fields)
* PR title `[20.0][MIG] <module>: Migration to 20.0`
* before any OCA PR: announce on the repo's "Migration to version 20.0" issue (manual)

Data-model changes per core module: OpenUpgrade `upgrade_analysis.txt` files
<https://github.com/OCA/OpenUpgrade> (used by the repair step).

## OCA tools: what calls what

| OCA tool | where it runs here | how |
|---|---|---|
| **Migration wiki procedure** (maintainer-tools wiki) | `scripts/migrate_module.sh` | the git commands transcribed step by step (format-patch/am, one pre-commit commit, `[MIG]` commit, version bump, `migrations/` removal, CREDITS cleanup) |
| **oca-port** <https://github.com/OCA/oca-port> | `scripts/scan.py` → `common.oca_port_dry_run` (Actions, `scan.run_oca_port_dry_run`) | `oca-port upstream/<src> upstream/<target> <module> --dry-run --verbose`; its analysis (existing PRs, commits to bring) lands in the CSV column `oca_port`. Not used for the port itself: its porting mode is interactive, and for an addon missing on the target it performs the same wiki procedure `migrate_module.sh` runs non-interactively |
| **odoo-module-migrator** <https://github.com/OCA/odoo-module-migrator> | `scripts/migrate_module.sh` step 3 | `odoo-module-migrate --modules <module> --init-version-name <src> --target-version-name <target>`; deterministic code transforms before pre-commit. It lags new Odoo versions (master stops at 19.0 on 2026-10-23), so the script runs it as far as it supports and logs the cap; the rest is for review/repair. `REBUILD=1` rebuilds an existing branch from scratch |
| **pre-commit with OCA hooks** (`oca-gen-addon-readme`, `oca-gen-addon-icon`, `odoo-pre-commit-hooks`, `pylint-odoo`, `setuptools-odoo`/`whool` metadata) | `scripts/migrate_module.sh` step 4 | `pre-commit run -a` twice, using each repo's own `.pre-commit-config.yaml`; this is where the `maintainer-tools` package actually executes |
| **oca-ci** (`test.yml` kept in every fork) | the forks' own GitHub Actions | tests every PR to the fork's target branch; `scan.py` reads the result into `ci` |
| **OpenUpgrade `upgrade_analysis.txt`** | the Claude task's repair step | data-model changes per core module, given to the repair subagent |

Installed by `bootstrap.sh` (task environment) and by the workflow (Actions):
pre-commit, oca-port, odoo-module-migrator.

Deliberately not used (OCA-side or release-time tooling, not addon migration):
`oca-migrate-branch` (creates the new branch on OCA repos), `oca-towncrier` (changelogs
at release), `oca-copier-update` (repo template refresh), the OCA GitHub bot and CI
internals. `module-composition-analysis / odoo_repository_migration` is an Odoo-hosted
alternative to these CSVs built on oca-port; noted, not adopted.

## Contribution conventions

<https://odoo-community.org/get-involved/contribute>

* PR title starts with the version tag; one concern per PR; migrations may keep several
  commits (history port + pre-commit + MIG).
* "AI-generated content submitted without review … will be asked to be revised": every
  fork PR is reviewed and tested by a human before anything reaches OCA.

## OCA AI policy

Policy text and discussion: <https://github.com/OCA/.github/pull/5> ·
summary of the open meeting:
<https://www.odoo-community.org/blog/news-updates-1/oca-ai-policy-open-meeting-summary-253>

What we apply:

* **Responsibility is never transferable to a tool.** A human (BADEP) tests, understands
  and signs every OCA PR.
* **Disclose assistance with the `Assisted-by:` trailer** (never `Co-authored-by:` for a
  tool). The `[MIG]` commit carries `config.migrate.ai_trailer`.
* **An AI tool is never the author or committer of a commit**, in the forks or in this
  repo. Every commit the Claude task makes is authored and committed by the human in
  `config.migrate.commit_identity`; `bootstrap.sh` applies it (overriding any identity the
  sandbox came with) and `migrate_module.sh` refuses to run under an AI identity (exit 13).
  Ported OCA commits keep their original authors.
* **Review is a human activity.** The automation never reviews or comments on OCA PRs.
* **Quantity × quality × rate.** The policy's reference point is ~30 lines; PSCs may set
  their own thresholds. We cap our own throughput (`max_modules_per_run`) and open OCA
  PRs only after the weekend review, never in bulk.
* Keep PR descriptions concise: no transcripts, no verbose AI prose.

## Temporary references to other PRs

<https://github.com/OCA/maintainer-tools/wiki/Use-temporary-reference(s)-to-another-pull-request(s)>

Used at OCA-PR time only (`test-requirements.txt` line pointing at the dependency's PR).
Inside our fork we merge the dependency PR into the migration branch instead, for
isolated testing; see PROCESS.md.
