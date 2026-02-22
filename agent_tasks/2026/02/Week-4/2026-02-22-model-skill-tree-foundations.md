# Model Skill Tree Foundations

- Date: 2026-02-22
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
- Change type: docs/tooling

## Context

After splitting `model-info-finder` into focused model skills, we needed a base-layer skill tree so model workflows can compose reusable observability and model primitives instead of duplicating scripts.

## What changed

Added foundational skills under `~/.codex/skills`:

1. `model-catalogue-core`
   - Shared helper: `scripts/model_catalogue_api_helpers.sh`
   - New primitives: `scripts/resolve_model.sh`, `scripts/latest_checkpoint.sh`
2. `obs-flyte-execution`
   - New wrapper: `scripts/inspect_flyte_execution.sh`
3. `obs-buildkite-jobs`
   - New utilities: `scripts/fetch_buildkite_job_log.sh`, `scripts/extract_error_lines.sh`
4. `obs-datadog-logs`
   - New utility: `scripts/build_datadog_logs_url.sh`

Rewired composite model skills to consume foundations:

- `model-lookup-basic`, `model-deep-summary`, `model-checkpoint-inspector`, `modelci-shadowgym-debug` now source `model-catalogue-core/scripts/model_catalogue_api_helpers.sh`.
- Removed duplicated helper copies from each composite skill.
- `modelci-shadowgym-debug` now uses `obs-buildkite-jobs` scripts for Buildkite log fetch and failure extraction.

Updated tree routing and compatibility:

- `model-info-finder/SKILL.md` now documents the full tree (foundations + composites) and composition examples.
- Added `model-info-finder/agents/openai.yaml`.
- `flyte-status-logs` kept as a compatibility alias and now delegates to `obs-flyte-execution`.

## Validation

- `quick_validate.py` passed for all updated/new skills:
  - `model-catalogue-core`
  - `obs-flyte-execution`
  - `obs-buildkite-jobs`
  - `obs-datadog-logs`
  - `model-lookup-basic`
  - `model-deep-summary`
  - `model-checkpoint-inspector`
  - `modelci-shadowgym-debug`
  - `model-info-finder`
- `bash -n` passed for all updated/new shell scripts.
- Smoke checks:
  - Datadog URL builder returned expected URL format.
  - Flyte execution inspector returned `workflow_phase=SUCCEEDED` for execution `am4vpqq8vh2ft4fnj9m8`.
