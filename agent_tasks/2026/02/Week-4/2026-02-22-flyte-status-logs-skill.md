# Flyte status + logs skill and CLI

- Date: 2026-02-22
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
- Change type: code/tooling

## Context

Needed a reusable way to read Flyte execution status and task log links from a Flyte console execution URL.

## What changed

- Added a new Bazel CLI target that inspects a Flyte execution and extracts:
  - workflow phase
  - workflow error message (if any)
  - node/task phases
  - task execution log URIs (`closure.logs`)
- Added a new local skill `flyte-status-logs` that wraps the CLI.

## Code references

- `wayve/prototypes/robotics/vehicle_dynamics/tools/flyte_status_logs/inspect_execution_logs_cli.py`
- `wayve/prototypes/robotics/vehicle_dynamics/tools/flyte_status_logs/BUILD`
- `.ai/skills/flyte-status-logs/SKILL.md`
- `.ai/skills/flyte-status-logs/scripts/inspect_flyte_status_logs.sh`
- `.ai/skills/flyte-status-logs/references/troubleshooting.md`
- `.ai/skills/flyte-status-logs/agents/openai.yaml`

## Validation

- `python .../quick_validate.py /workspace/WayveCode/.ai/skills/flyte-status-logs` -> `Skill is valid!`
- `bazel run //wayve/prototypes/robotics/vehicle_dynamics/tools/flyte_status_logs:inspect_execution_logs_cli -- --help` -> success
- `./.ai/skills/flyte-status-logs/scripts/inspect_flyte_status_logs.sh "https://flyte.data.wayve.ai/console/projects/synthetic-data-studio/domains/development/executions/am4vpqq8vh2ft4fnj9m8" --include-successful-task-logs --json` -> success, returned status and log URIs

## Outcome for requested execution

Execution `am4vpqq8vh2ft4fnj9m8` is `SUCCEEDED` and exposes task log links (Datadog/Loki/etc.) when `--include-successful-task-logs` is enabled.
