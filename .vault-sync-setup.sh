#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_DIR="${1:-$SCRIPT_DIR}"

if [[ ! -d "$VAULT_DIR/.git" ]]; then
  echo "[vault-sync-setup] expected a git repo at: $VAULT_DIR" >&2
  echo "Usage: $0 /path/to/vault" >&2
  exit 1
fi

SYNC_SCRIPT="$VAULT_DIR/.vault-sync.sh"
WATCHER_SCRIPT="$VAULT_DIR/.vault-sync-watch.py"

if [[ ! -f "$SYNC_SCRIPT" || ! -f "$WATCHER_SCRIPT" ]]; then
  echo "[vault-sync-setup] missing sync files in: $VAULT_DIR" >&2
  exit 1
fi

chmod +x "$SYNC_SCRIPT" "$WATCHER_SCRIPT"

SYSTEMD_DIR="$HOME/.config/systemd/user"
mkdir -p "$SYSTEMD_DIR"

SERVICE_FILE="$SYSTEMD_DIR/vault-sync-watch.service"
cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=Vault git sync watcher

[Service]
Type=simple
ExecStart=$WATCHER_SCRIPT
Restart=always
RestartSec=2

[Install]
WantedBy=default.target
EOF

if command -v systemctl >/dev/null 2>&1; then
  if systemctl --user daemon-reload >/dev/null 2>&1; then
    systemctl --user enable --now vault-sync-watch.service
    echo "[vault-sync-setup] enabled and started vault-sync-watch.service"
  else
    echo "[vault-sync-setup] systemd user session not available." >&2
    echo "Run manually: $WATCHER_SCRIPT" >&2
  fi
else
  echo "[vault-sync-setup] systemctl not found; run manually: $WATCHER_SCRIPT" >&2
fi
