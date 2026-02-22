# Obs Flyte Bazel Runtime Install Layout

- Date: 2026-02-22
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
- Change type: tooling

## Context

Needed `~/.codex/skills/obs-flyte-execution` to be the source of truth, with an installer that copies only Bazel runtime files into `WayveCode/.ai/skills/obs-flyte-execution` so the skill can execute via `bazel run`.

## What changed

In `~/.codex/skills/obs-flyte-execution`:
- Added runtime files:
  - `BUILD`
  - `inspect_execution_logs_cli.py`
- Updated wrapper:
  - `scripts/inspect_flyte_execution.sh` now runs:
    - `bazel run //.ai/skills/obs-flyte-execution:inspect_execution_logs_cli -- ...`
- Reworked installer:
  - `install.sh` now copies only:
    - `BUILD`
    - `inspect_execution_logs_cli.py`
  - Destination:
    - `/workspace/WayveCode/.ai/skills/obs-flyte-execution/`
- Removed old copy helper:
  - `scripts/install_to_wayvecode_ai_skills.sh`

In `/workspace/WayveCode/.ai/skills/obs-flyte-execution`:
- Removed previously copied skill metadata/scripts.
- Installed only:
  - `BUILD`
  - `inspect_execution_logs_cli.py`

## Validation

- `bazel query //.ai/skills/obs-flyte-execution:inspect_execution_logs_cli` resolves.
- `bazel run //.ai/skills/obs-flyte-execution:inspect_execution_logs_cli -- <url> --json` executes successfully.
- Wrapper command works end-to-end and returns `workflow_phase=SUCCEEDED` for execution `am4vpqq8vh2ft4fnj9m8`.
