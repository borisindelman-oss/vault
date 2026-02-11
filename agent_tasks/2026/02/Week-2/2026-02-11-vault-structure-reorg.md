# 2026-02-11 — Vault structure reorg

## Summary
- Removed the `codex/` layer from the WayveCode notes root.
- Moved dated task notes under `agent_tasks/YYYY/MM/Week-N/`.
- Kept `projects.md` at WayveCode top level with per-project files in `projects/`.
- Updated global agent instructions and the `project-manager` skill to the new paths/layout.

## What changed
- Moved:
  - `/home/borisindelman/git/vault/codex/WayveCode` -> `/home/borisindelman/git/vault/WayveCode`
- Moved date trees:
  - `/home/borisindelman/git/vault/2025` -> `/home/borisindelman/git/vault/agent_tasks/2025`
  - `/home/borisindelman/git/vault/2026` -> `/home/borisindelman/git/vault/agent_tasks/2026`
- Removed empty legacy folder:
  - `/home/borisindelman/git/vault/codex`
- Updated references:
  - `codex/WayveCode/...` -> `WayveCode/...`
  - `[[2025/...]]` / `[[2026/...]]` -> `[[agent_tasks/2025/...]]` / `[[agent_tasks/2026/...]]`
  - `/home/borisindelman/git/vault/codex/WayveCode/...` -> `/home/borisindelman/git/vault/...`

## Instruction updates
- `~/.codex/AGENTS.md`
  - Vault root path now points to `~/git/vault/`.
  - Task structure now points to `agent_tasks/YYYY/MM/Week-N/`.
- `~/.codex/skills/project-manager/SKILL.md`
  - Storage layout paths updated to `/home/borisindelman/git/vault/...`.
  - Continue workflow now reads `<slug>.md` (single-file project format).

## Validation
- Verified no remaining `codex/WayveCode` or old absolute vault root references in WayveCode docs.
- Verified `projects/projects.json` now points to `/home/borisindelman/git/vault/projects/*.md`.
