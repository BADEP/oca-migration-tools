#!/usr/bin/env bash
# Install the tooling the scripts need. Idempotent: safe to re-run in a persistent
# environment, cheap in a fresh one. Odoo itself is NOT installed here: unit tests run
# in the forks' own CI (OCA's test workflow) on every PR.
set -euo pipefail
python3 -m pip install --quiet --break-system-packages pyyaml 2>/dev/null || python3 -m pip install --quiet pyyaml
if ! command -v pipx >/dev/null; then python3 -m pip install --quiet --break-system-packages pipx; fi
command -v pre-commit >/dev/null || pipx install pre-commit
command -v oca-port >/dev/null || pipx install oca-port
command -v odoo-module-migrate >/dev/null || pipx install git+https://github.com/OCA/odoo-module-migrator.git@master
command -v gh >/dev/null || { echo "gh CLI missing: https://cli.github.com"; exit 1; }
git config --global user.name  >/dev/null || git config --global user.name  "BADEP OCA bot"
git config --global user.email >/dev/null || git config --global user.email "oca-bot@badep.ca"
echo "bootstrap ok"
