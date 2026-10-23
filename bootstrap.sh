#!/usr/bin/env bash
# Install the tooling the scripts need. Idempotent: safe to re-run in a persistent
# environment, cheap in a fresh one. Odoo itself is NOT installed here: unit tests run
# in the forks' own CI (OCA's test workflow) on every PR.
set -euo pipefail
cd "$(dirname "$0")"
python3 -m pip install --quiet --break-system-packages pyyaml 2>/dev/null || python3 -m pip install --quiet pyyaml
if ! command -v pipx >/dev/null; then python3 -m pip install --quiet --break-system-packages pipx; fi
command -v pre-commit >/dev/null || pipx install pre-commit
command -v oca-port >/dev/null || pipx install oca-port
command -v odoo-module-migrate >/dev/null || pipx install git+https://github.com/OCA/odoo-module-migrator.git@master
command -v gh >/dev/null || { echo "gh CLI missing: https://cli.github.com"; exit 1; }
# Commit identity: always the human in config.migrate.commit_identity, overriding any
# identity the environment came with (some sandboxes preset an AI tool's identity).
ID_NAME="$(python3 -c "import yaml;print(yaml.safe_load(open('config.yaml'))['migrate']['commit_identity']['name'])")"
ID_EMAIL="$(python3 -c "import yaml;print(yaml.safe_load(open('config.yaml'))['migrate']['commit_identity']['email'])")"
if echo "$ID_NAME $ID_EMAIL" | grep -qiE 'claude|anthropic'; then
  echo "config.migrate.commit_identity must be a human, not an AI tool"; exit 1
fi
git config --global user.name  "$ID_NAME"
git config --global user.email "$ID_EMAIL"
echo "bootstrap ok"
