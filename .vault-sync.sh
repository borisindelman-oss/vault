#!/usr/bin/env bash
set -euo pipefail

VAULT="/home/borisindelman/git/vault"
cd "$VAULT"

# Prevent overlapping runs (e.g., rapid filesystem events)
exec 9>.git/.sync.lock
flock -n 9 || exit 0

# Pull first to minimize conflicts
if ! git pull --rebase --autostash --prune; then
  echo "[vault-sync] git pull failed; resolve manually" >&2
  exit 1
fi

# Commit/push only if there are local changes
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "vault sync $(date -u +'%Y-%m-%dT%H:%M:%SZ')" || true
  git push
fi
