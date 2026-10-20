# For any agent working in this repository

This repo is self-contained: everything an agent needs to run or help with BADEP's OCA
migration process is here. Read in this order before acting:

1. `docs/PROCESS.md` — what the process is, the branch model, statuses, the manual gate.
2. `docs/GUIDELINES.md` — the OCA rules and tools we follow (migration wiki, AI policy).
3. `config.yaml` — target/source versions, caps, policies, which model does what.
4. `docs/CLAUDE-TASK.md` — the exact weekly prompt; a one-off run follows the same steps.

Hard rules, whatever the request:

- Scripts first. `scripts/` does everything deterministic; AI is for relevancy verdicts
  and CI-failure repair only. Do not re-implement a script's job by hand.
- OCA wins every conflict in the forks' target branch.
- Never open, review or comment on anything in the OCA organisation; never claim a module
  on OCA's migration issue. Those are human steps.
- Never work on a module that is `claimed-by-others` in `reports/<target>/`.
- Respect `overrides.csv`; never edit it, humans own it.
- Disclose AI assistance with the `Assisted-by:` trailer (`config.migrate.ai_trailer`).
- The CSVs in `reports/<target>/` are the state. Update them through the scripts
  (`scan.py`, `select_candidates.py set-relevancy`), commit them, and keep `summary.md`
  current via `report.py`.

Local setup: `bash bootstrap.sh`, a GitHub token in `GH_TOKEN` with access to the forks.
Odoo is not needed locally; tests run in the forks' CI on each PR.
