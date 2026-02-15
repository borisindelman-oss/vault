# Interleaved Route Threshold Calibration

- Date: 2026-02-15
- Branch: `boris/train/parking_pudo_interleaving`
- PR: none
- Type: code

## Summary
Updated interleaved parking-route thresholds to calibrated values and aligned deploy defaults + wrapper documentation.

## Changes
- Updated `RouteInterleavingWrapperImpl` defaults in `wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py`:
  - `near_end_of_route_sum_thresh: 3.45e4`
  - `end_of_route_sum_thresh: 2.07e4`
- Updated constructor documentation in `wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py` to calibrated conversion:
  - `230 signal-units per meter`
  - `3.45e4 -> ~150m`, `2.07e4 -> ~90m`
- Updated CLI defaults in `wayve/ai/si/deploy_interleaved_models.py`:
  - `--route_end_sum_thresh` default `3.45e4`
  - `--route_no_sum_thresh` default `2.07e4`

## Validation
- Verified references and call-path wiring:
  - `deploy_interleaved_models.py` passes `route_end_sum_thresh` and `route_no_sum_thresh` into `build_route_interleaving_wrapper(...)`.
- No tests run in this task.
