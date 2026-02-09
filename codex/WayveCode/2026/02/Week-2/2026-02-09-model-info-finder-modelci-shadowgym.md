# Model Info Finder: Model CI, Buildkite Logs, Shadow Gym

## Summary
Extended the `model-info-finder` skill so it can:
- resolve model by nickname or full `model_session_id`
- summarize latest Model CI build + job statuses
- fetch Buildkite logs for failed jobs (when `BUILDKITE_TOKEN` is set)
- check Eval Studio/Flyte execution id from model artefact
- fetch Shadow Gym execution ids and latest metadata

## What Changed
- Updated skill doc: `/home/borisindelman/git/assests/codex/skills/model-info-finder/SKILL.md`
- Added a dedicated `Model CI + Shadow Gym Debugging` section with copy/paste commands.
- Added robust handling for:
  - nickname -> model id resolution
  - multi-failure job-id iteration in `zsh`
  - Shadow Gym API responses that are not arrays

## Validation
Validated end-to-end on nickname `yellow-fish-alert`:
- model id resolution works
- latest build summary matches expected statuses
- Buildkite log fetch returns HTTP 200 for both failed jobs
- Eval Studio info endpoint returns `{"av_test_suite_execution_id": null}`
- Shadow Gym query runs safely and returns empty list/header when no executions exist

## Branch / PR
- Branch: current workspace branch
- PR: none
