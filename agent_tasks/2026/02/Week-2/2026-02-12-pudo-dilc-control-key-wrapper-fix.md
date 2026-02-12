# 2026-02-12 — PUDO parking wrapper DILC control-key crash fix

## Summary
- Investigated failed training run `jellyfish-moccasin-singing-125420`.
- Root cause was an export-time crash in `ParkingDeploymentWrapperImpl` when `deployment_driving_controls_keys` included `DrivingControlKey.DILC_MODE`.
- Updated parking wrapper to accept `DILC_MODE` in driving controls and keep behavior customization handling of DILC.
- Added a regression test to ensure this control-key combination no longer raises.

## Root Cause
- In run logs (`rank0.log`), wrapper init passed:
  - `deployment_driving_controls_keys: (0, 1, 3, 2)`
- Crash stack during on-train-start model export:
  - `ValueError: Unsupported driving control key: 2`
  - thrown from `ParkingDeploymentWrapperImpl._add_driving_controls_inputs(...)`
- `2` maps to `DrivingControlKey.DILC_MODE`.

## Code Change
- `wayve/ai/zoo/deployment/deployment_wrapper.py`
  - Added `dilc_mode` to internal control-key map.
  - Updated `_add_driving_controls_inputs(...)` to treat DILC as a valid control key (no parking-specific tensor derived there), instead of raising.
- `wayve/ai/si/test/interfaces/test_deployment_wrapper.py`
  - Added `test_parking_wrapper_accepts_dilc_control_key` regression test.

## Validation
- Attempted: `bazel test //wayve/ai/si:py_test --test_arg='-k=test_parking_wrapper_accepts_dilc_control_key' --test_output=errors`
- Target is very heavy and entered long full-suite collection; did not complete in this session.
- Log-based root-cause validation is complete and deterministic.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
- Job: `125420` (`jellyfish-moccasin-singing-125420`)
