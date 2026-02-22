# Split model-info-finder into focused skills

- Date: 2026-02-22
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
- Change type: docs/tooling

## Context

The original `model-info-finder` bundled multiple workflows in one skill. The goal was to separate it into focused skills with narrower triggers while preserving existing behavior.

## What changed

Created four focused skills under `~/.codex/skills`:

1. `model-lookup-basic`
   - Uses `lookup_by_nickname.sh`, `lookup_by_author.sh`
2. `model-deep-summary`
   - Uses `deep_model_summary.sh`
3. `model-checkpoint-inspector`
   - Uses `checkpoint_licenses.sh`, `checkpoint_runs.sh`
4. `modelci-shadowgym-debug`
   - Uses `modelci_evalstudio_shadowgym.sh`

Each new skill includes:
- dedicated `SKILL.md`
- `agents/openai.yaml` with corrected `$skill-name` default prompt
- self-contained scripts copied into `scripts/` (including shared helper)

Updated `model-info-finder/SKILL.md` into a lightweight router/deprecation bridge that points to the four focused skills, while retaining legacy script compatibility in that folder.

## Validation

- `quick_validate.py` passed for:
  - `model-lookup-basic`
  - `model-deep-summary`
  - `model-checkpoint-inspector`
  - `modelci-shadowgym-debug`
  - updated `model-info-finder`
- Smoke-tested one command in each new skill folder successfully.

## Paths

- `/home/borisindelman/.codex/skills/model-lookup-basic/`
- `/home/borisindelman/.codex/skills/model-deep-summary/`
- `/home/borisindelman/.codex/skills/model-checkpoint-inspector/`
- `/home/borisindelman/.codex/skills/modelci-shadowgym-debug/`
- `/home/borisindelman/.codex/skills/model-info-finder/SKILL.md`
