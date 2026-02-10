# Model Info Finder Script Extraction

## Summary
Moved `model-info-finder` from inline `SKILL.md` command blocks to dedicated shell scripts in the skill folder, then updated the skill doc to call those scripts.

## Changes
- Added reusable helper module:
  - `.ai/skills/model-info-finder/common.sh`
- Added workflow entry scripts:
  - `.ai/skills/model-info-finder/lookup_by_nickname.sh`
  - `.ai/skills/model-info-finder/lookup_by_author.sh`
  - `.ai/skills/model-info-finder/deep_model_summary.sh`
  - `.ai/skills/model-info-finder/checkpoint_licenses.sh`
  - `.ai/skills/model-info-finder/checkpoint_runs.sh`
  - `.ai/skills/model-info-finder/modelci_evalstudio_shadowgym.sh`
- Rewrote `.ai/skills/model-info-finder/SKILL.md` to document script-based usage and expected outputs.
- Added script-evolution rule in `SKILL.md`: extend/modify `.sh` scripts when workflows are insufficient, instead of re-embedding long inline command blocks.
- Added preflight and missing-requirement prompts:
  - Required command checks (`curl`, `jq`, `column`) in `common.sh`
  - Token guidance prompt when `MODEL_CATALOGUE_TOKEN` is unset
  - Explicit `BUILDKITE_TOKEN` prompt in Model CI flow when failed jobs are present
  - `perl` missing prompt with raw-log fallback for Buildkite log parsing

## Validation
- `bash -n` passed on all new scripts.
- Invoked each script without args; each printed the expected usage line and exited cleanly.

## Branch / PR
- Branch: `skill/model-info-finder`
- PR: none
