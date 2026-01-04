# Git sync tool

## Summary
- Moved sync scripts under `/home/borisindelman/git/assests/vault` and renamed them as a generic git sync tool.
- Updated scripts to accept a repo path argument and keep local changes on merge conflicts.
- Adjusted cron setup to install per-repo minute sync entries.

## Files
- `/home/borisindelman/git/assests/vault/git-sync.sh`
- `/home/borisindelman/git/assests/vault/git-sync-cron.sh`
- `/home/borisindelman/git/assests/vault/git-sync-cron-setup.sh`
