# Remove interleaved_id/interleaved_event from stopping interleaving wrapper

- Date: 2026-02-17
- Branch: `boris/train/parking_pudo_interleaving`
- PR: none
- Type: code

## Summary
Removed `interleaved_id` and `interleaved_event` from route interleaving stopping wrapper outputs and deployment output key generation. Switching observability remains via existing print logs.

## Changes
- Updated `wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py`:
  - Removed `interleaved_id` and `interleaved_event` from `RouteInterleavingOutput`.
  - Removed special-case optional handling for those two keys.
  - Updated cached output path to stop accepting/returning those tensors.
  - Removed runtime creation/propagation of those tensors in forward.
  - Stopped force-appending those keys in `get_interleaved_deployment_config`.
  - Kept switch/no-route diagnostics via existing prints.

## Validation
- `python -m py_compile wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py` passed.
- Searched file for removed outputs; no remaining `interleaved_id`/`interleaved_event` usages.
