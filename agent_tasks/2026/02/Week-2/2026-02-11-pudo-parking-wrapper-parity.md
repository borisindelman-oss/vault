# 2026-02-11 — PUDO parking wrapper parity (single wrapper)

## Summary
- Resumed PUDO update work on `boris/train/pudo_11_02_26` and completed wrapper parity changes without introducing a new wrapper class.
- Kept all parking logic in `ParkingDeploymentWrapperImpl` and enabled driving-parity preprocessing (behavior customization + navigation + indicator memory) behind optional parking wrapper inputs.
- Ported end-of-route parking trigger logic and set threshold to `5.5e2` (~5 meters).

## Follow-up update (same day)
- Parking-only deployment path was removed by policy for this project.
- Parking now defaults to driving-parity deployment behavior in `prepare_deployment_model(...)`:
  - `use_behavior_control_input=True`
  - `use_navigation_instructions=True`
- If a caller explicitly disables either of those while `enable_parking=True`, deployment now raises a `ValueError`.
- `ParkingDeploymentWrapperImpl` forward now requires `driving_parameters` and navigation tensors (instead of optional parity inputs).

## Code Changes
- `wayve/ai/zoo/deployment/deployment_wrapper.py`
  - Added optional parity inputs to `ParkingDeploymentWrapperImpl` (`navigation_version_number`, behavior config keys, optional `driving_parameters` + nav tensors in forward).
  - Added end-of-route parking path:
    - `enable_end_of_route_parking`
    - `_end_of_route_mask(...)`
    - OR-merge into `PARKING_MODE`.
  - Added inline threshold note: `5.5e2  # Equivalent to ~5 meters.`
  - Ensured no `UnifiedParkingDeploymentWrapperImpl` class is used/kept.
- `wayve/ai/si/models/deployment.py`
  - Parking + behavior-control + navigation now selects `ParkingDeploymentWrapperImpl` directly.
  - Allowed parking+behavior+nav(+indicator) in feature-combination validation.
- `wayve/ai/si/test/interfaces/test_deployment_wrapper.py`
  - Added regression tests for end-of-route trigger and toggle behavior.
- `wayve/ai/si/test/models/test_deployment.py`
  - Added parking behavior+nav wrapper selection test using `ParkingDeploymentWrapperImpl`.
- `wayve/ai/zoo/deployment/deployment_wrapper_codegen.py`
  - Preserved parameter order/defaults in generated wrapper signatures.
  - Added typing-safe generated imports for optional annotations.
- `wayve/ai/zoo/deployment/test/test_deployment_wrapper_codegen.py`
  - Added regression coverage for default-parameter preservation in generated wrappers.
- `wayve/ai/si/configs/parking/parking_config.py`
  - Renamed mode visibility alias to `parking_bc_train_release_2026_5_4`.

## Validation
- Passed:
  - `bazel test //wayve/ai/zoo/deployment:test_deployment_py_test`
  - `bazel test //wayve/ai/zoo/deployment:test_deployment`
- Blocked:
  - `bazel test //wayve/ai/si:py_test --test_arg="-k=...parking..."`
  - Fails at analysis due external ACR auth fetch: `azure-storage_azurite` `401 Unauthorized`.

## Project Update
- Related project: [[projects/pudo-update-current-driving-release]]
- Phase 2 progress:
  - Wrapper parity path: done.
  - End-of-route parking path: done.
  - Parking train mode naming visibility: done.
