# Vault sync minute pull

## Summary
- Updated the vault sync watcher to pull/commit at least once per minute even with no local file events.
- Kept existing event-driven debounce behavior for fast local changes.

## Details
- Added `PULL_INTERVAL_SECONDS = 60.0` and periodic sync scheduling.
- Reset the periodic timer after any sync (event-driven or timed) to avoid back-to-back runs.

## Files
- `/home/borisindelman/git/vault/.vault-sync-watch.py`
