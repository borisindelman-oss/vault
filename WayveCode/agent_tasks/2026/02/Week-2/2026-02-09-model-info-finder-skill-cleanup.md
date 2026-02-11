# Model Info Finder Skill Cleanup

## Summary
Refactored `model-info-finder` to reduce command complexity and improve reliability for operational use.

## Changes
- Rewrote the skill into helper-based workflows (`mc_curl`, `resolve_model_id`, `latest_checkpoint_num`) to remove duplicated command blocks.
- Added explicit guardrails for:
  - no model matches
  - ambiguous nickname matches
  - no Model CI builds
- Kept Model CI + Buildkite + Eval Studio + Shadow Gym flows, but simplified command structure.
- Preserved curl-only requirement and plain-text response requirements.

## Validation
Ran the new flow against `teal-llama-scholarly`:
- nickname -> model id resolution worked
- checkpoint resolution worked
- latest Model CI summary worked
- failed job logs fetched with Buildkite token (HTTP 200)
- Shadow Gym summary handled empty result safely

## Branch / PR
- Branch: current workspace branch
- PR: none
