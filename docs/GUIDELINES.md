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
* bump version to `20.0.1.0.0`; remove `migrations/`; remove past financed-migration
  lines from `readme/CREDITS.rst`
* final commit `[MIG] <module>: Migration to 20.0`
* **not** done: changing copyright years or original authors
* PR title `[20.0][MIG] <module>: Migration to 20.0`
* before any OCA PR: announce on the repo's "Migration to version 20.0" issue (manual)

Data-model changes per core module: OpenUpgrade `upgrade_analysis.txt` files
<https://github.com/OCA/OpenUpgrade> (used by the repair step).

## OCA tools used

* **oca-port** <https://github.com/OCA/oca-port> — migration assistant / missing-commit
  porter; `scan.run_oca_port_dry_run` adds its analysis to the CSV.
* **odoo-module-migrator** <https://github.com/OCA/odoo-module-migrator> —
  deterministic code transforms between versions; run before pre-commit.
* **maintainer-tools** <https://github.com/OCA/maintainer-tools> — conventions, README
  generator (`oca-gen-addon-readme`, run by pre-commit in OCA repos).
* **oca-ci** — the forks keep OCA's `test.yml` workflow, so every PR to the fork runs the
  same tests OCA will run.
* **module-composition-analysis / odoo_repository_migration** — Odoo-side alternative to
  these CSVs, built on oca-port; not used yet.

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
