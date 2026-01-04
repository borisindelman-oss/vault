# Vault sync cron

## Summary
- Switched vault sync script to fetch/merge with local-preferred conflict resolution.
- Added cron wrapper and setup script to run sync every minute.

## Details
- Conflict policy: merge with `-X ours` to keep local files on conflicts while still integrating non-conflicting remote changes.
- Cron entry: `* * * * * /home/borisindelman/git/vault/.vault-sync-cron.sh`.

## Files
- `/home/borisindelman/git/vault/.vault-sync.sh`
- `/home/borisindelman/git/vault/.vault-sync-cron.sh`
- `/home/borisindelman/git/vault/.vault-sync-cron-setup.sh`
