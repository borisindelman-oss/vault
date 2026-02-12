# 2026-02-12 — PUDO train fix: Parking wrapper TorchScript continue

## Summary
- Investigated failed training run `magenta-wolverine-topographical-125575`.
- Root cause was TorchScript rejecting `continue` inside the parking wrapper driving-controls loop.
- Replaced `continue` with a no-op branch (`pass`) to keep behavior unchanged and scriptability intact.

## Root Cause
- Crash:
  - `... do not support break or continue inside the body of these loops`
- Failure path:
  - `ParkingDeploymentWrapperWithRadar._add_driving_controls_inputs(...)`
  - `wayve/ai/zoo/deployment/deployment_wrapper.py`
  - `continue` in the `dilc_mode` branch of `for idx, control_key in enumerate(self.driving_controls_keys)`.

## Code Changes
- `wayve/ai/zoo/deployment/deployment_wrapper.py`
  - In `_add_driving_controls_inputs(...)`, replaced:
    - `elif control_key == dilc_mode: continue`
  - with:
    - `elif control_key == dilc_mode: pass`
  - Semantics preserved:
    - DILC remains consumed by behavior customization.
    - No extra parking tensor is derived in this branch.

## Validation
- `bazel test //wayve/ai/zoo/deployment:test_deployment_py_test --test_arg='-k=deployment_wrapper or behavior_customizer or parking'`
  - Passed.

## Experiment Run Ledger
- `magenta-wolverine-topographical-125575`
  - Change tested: branch state after prior behavior-customizer TorchScript fix.
  - Targeted issue: generated parking wrapper TorchScript compile.
  - Outcome: fail due to `continue` in parking wrapper control loop; fixed by this patch.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
