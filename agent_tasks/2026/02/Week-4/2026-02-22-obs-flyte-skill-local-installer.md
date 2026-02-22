# Obs Flyte Skill Local Installer

- Date: 2026-02-22
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
- Change type: docs/tooling

## Context

Needed a simple way to copy the Flyte observability skill from `~/.codex/skills` into repo-local skills under `WayveCode/.ai/skills` without extra manual steps.

## What changed

- Added installer script:
  - `~/.codex/skills/obs-flyte-execution/scripts/install_to_wayvecode_ai_skills.sh`
- Updated skill docs with install command:
  - `~/.codex/skills/obs-flyte-execution/SKILL.md`

The installer copies:
- `SKILL.md`
- `agents/`
- `scripts/`
- `references/` (if present)

Destination defaults to:
- `/workspace/WayveCode/.ai/skills/obs-flyte-execution`

## Validation

- Script syntax check (`bash -n`) passed.
- Ran installer successfully.
- Confirmed files exist under `WayveCode/.ai/skills/obs-flyte-execution`.
