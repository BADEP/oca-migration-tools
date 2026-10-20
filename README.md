# oca-migration-tools

BADEP's tooling and status tracker for keeping its forks of [OCA](https://github.com/OCA)
repositories in sync and migrating modules that are missing on the newest Odoo version.

**Branch = target Odoo version.** You are on `20.0`.

| | |
|---|---|
| `repos.csv` | the OCA repos in scope (edit freely; `enabled` column) |
| `overrides.csv` | manual decisions that survive every run |
| `config.yaml` | target/source versions, caps, policies, models |
| `scripts/` | deterministic steps: sync, scan, select, migrate, report |
| `reports/20.0/` | one CSV per repo + `summary.md` — **start here on review day** |
| `docs/PROCESS.md` | the whole process, branch model, manual gate |
| `docs/GUIDELINES.md` | the OCA guidelines and tools we adhere to |
| `docs/CLAUDE-TASK.md` | prompt of the weekly AI task |
| `.github/workflows/weekly-sync.yml` | Friday 05:00 Toronto: sync + scan + report |

## Weekly cycle

```
Fri 05:00  GitHub Actions   sync forks → scan → CSV + summary   (no AI)
Fri 07:00  Claude task      relevancy → migrate → CI → repair → merge → notes → email
Weekend    human            test fork PRs, open OCA PRs for the ready ones
```

## Running locally

```bash
bash bootstrap.sh
export GH_TOKEN=...              # token with access to the BADEP org
python3 scripts/sync_forks.py server-tools           # one repo
python3 scripts/scan.py server-tools
python3 scripts/report.py
python3 scripts/select_candidates.py migrate
bash scripts/migrate_module.sh server-tools base_technical_features 19.0
```

## Setup once

1. Create the `BADEP_GH_TOKEN` repository secret (fine-grained PAT on the BADEP org:
   contents RW, pull requests RW, issues R, administration RW for fork creation).
2. Make sure GitHub Actions are enabled on the forks (the OCA `test.yml` workflow is what
   tests our PRs).
3. Create the Claude scheduled task with the prompt in `docs/CLAUDE-TASK.md`.

Nothing here opens pull requests on OCA. That step is human, after testing, and follows
OCA's [AI policy](docs/GUIDELINES.md#oca-ai-policy).
