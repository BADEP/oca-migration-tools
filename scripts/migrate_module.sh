#!/usr/bin/env bash
# Deterministic migration of one module, following
# https://github.com/OCA/maintainer-tools/wiki/Migration-to-version-20.0
#
# usage: migrate_module.sh <repo> <module> <source_branch> [dep_pr_ref ...]
#   dep_pr_ref: "OCA/<repo>#<number>" — an open upstream PR for a dependency, merged
#               into the migration branch so the module can be tested in isolation.
#
# Produces branch <target>-mig-<module> on the BADEP fork, pushed, with:
#   1. the module's history ported from <source_branch> (git format-patch | git am)
#   2. dependency PRs merged (if any)
#   3. odoo-module-migrator applied (deterministic code transforms)
#   4. "[IMP] <module>: pre-commit auto fixes" (one commit, as the wiki asks)
#   5. "[MIG] <module>: Migration to <target>" with the wiki's mandatory edits
#      (version bump, migrations/ removed, CREDITS.rst financed-migration lines removed)
#      and the Assisted-by trailer
# The AI repair step, if needed, comes after CI has run, never before.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
cfg() { python3 -c "import yaml,sys;c=yaml.safe_load(open('$ROOT/config.yaml'));print(eval('c'+sys.argv[1]))" "$1"; }

REPO="$1"; MODULE="$2"; SRC="$3"; shift 3
DEP_PRS=("$@")
ORG="$(cfg "['org']")"; UP="$(cfg "['upstream_org']")"; TARGET="$(cfg "['target']")"
TRAILER="$(cfg "['migrate']['ai_trailer']")"
WORK="${OCA_WORK_DIR:-$ROOT/.work}"; mkdir -p "$WORK"
PATH_REPO="$WORK/$REPO"
BRANCH="$TARGET-mig-$MODULE"

if [ ! -d "$PATH_REPO/.git" ]; then
  git clone "https://github.com/$ORG/$REPO.git" "$PATH_REPO"
  git -C "$PATH_REPO" remote add upstream "https://github.com/$UP/$REPO.git"
fi
cd "$PATH_REPO"
# An AI tool is never author or committer (OCA AI policy): refuse before any commit.
if { git var GIT_AUTHOR_IDENT; git var GIT_COMMITTER_IDENT; } | grep -qiE 'claude|anthropic'; then
  echo "AI_IDENTITY: git identity is an AI tool; run bootstrap.sh"; exit 13
fi
git fetch -q upstream "$TARGET" "$SRC"
git fetch -q origin "$TARGET" || true
git fetch -q origin "$BRANCH" 2>/dev/null && EXISTS=1 || EXISTS=0

if [ "$EXISTS" = 1 ]; then
  echo "branch $BRANCH already exists on fork; rebasing on upstream/$TARGET"
  git checkout -q -B "$BRANCH" "origin/$BRANCH"
  git rebase "upstream/$TARGET"
else
  git checkout -q -B "$BRANCH" "upstream/$TARGET"
  # 1. port history
  git format-patch --keep-subject --stdout "upstream/$TARGET..upstream/$SRC" -- "$MODULE" \
    | git am -3 --keep --ignore-whitespace || { git am --abort; echo "PORT_CONFLICT"; exit 10; }
fi

# 2. dependency PRs (merged, not referenced: this branch is for isolated testing)
for ref in "${DEP_PRS[@]:-}"; do
  [ -z "$ref" ] && continue
  dep_repo="${ref%%#*}"; dep_repo="${dep_repo#*/}"; num="${ref##*#}"
  git fetch -q "https://github.com/$UP/$dep_repo.git" "refs/pull/$num/head" || { echo "DEP_FETCH_FAILED $ref"; exit 11; }
  git merge --no-edit -m "[DEP] merge $ref for local testing (remove before upstream PR)" FETCH_HEAD \
    || { git merge --abort; echo "DEP_MERGE_CONFLICT $ref"; exit 12; }
done

# 3. deterministic code transforms
if command -v odoo-module-migrate >/dev/null; then
  odoo-module-migrate --directory . --modules "$MODULE" --init-version-name "$SRC" \
    --target-version-name "$TARGET" --no-commit --no-pre-commit || echo "odoo-module-migrate reported problems (continuing)"
fi

# 4. pre-commit, one commit
if [ -f .pre-commit-config.yaml ]; then
  pre-commit run -a || true
  pre-commit run -a || true   # second pass settles formatter ping-pong
  git add -A
  git diff --cached --quiet || git commit -qm "[IMP] $MODULE: pre-commit auto fixes" --no-verify
fi

# 5. mandatory wiki edits
python3 - "$MODULE" "$TARGET" <<'EOF'
import re, sys, pathlib, shutil
mod, target = sys.argv[1], sys.argv[2]
p = pathlib.Path(mod) / "__manifest__.py"
s = p.read_text()
# wiki: "Bump the module version to <target>.1.0.0" (reset, not a series swap)
s2 = re.sub(r'(["\']version["\']\s*:\s*["\'])[^"\']+(["\'])', rf'\g<1>{target}.1.0.0\g<2>', s)
p.write_text(s2)
mig = pathlib.Path(mod) / "migrations"
if mig.exists():
    shutil.rmtree(mig)
credits = pathlib.Path(mod) / "readme" / "CREDITS.rst"
if credits.exists():
    lines = [l for l in credits.read_text().splitlines(keepends=True)
             if not re.search(r"(financ|sponsor).*migration|migration.*(financ|sponsor)", l, re.I)]
    credits.write_text("".join(lines))
EOF
git add -A
git commit -qm "[MIG] $MODULE: Migration to $TARGET" -m "$TRAILER" --no-verify || true

git push -u --force-with-lease origin "$BRANCH"
echo "PUSHED $ORG/$REPO $BRANCH"
