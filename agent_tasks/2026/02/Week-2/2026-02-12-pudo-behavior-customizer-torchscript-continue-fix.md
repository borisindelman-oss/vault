# 2026-02-12 — PUDO train fix: BehaviorCustomizer TorchScript continue

## Summary
- Investigated failed training run `velociraptor-proficient-ivory-125547`.
- Root cause was TorchScript rejecting `continue` inside the driving-controls loop in `BehaviorCustomizer.forward(...)`.
- Rewrote the loop to be branch-only (no `continue`) while preserving behavior (consume `DILC_MODE`, ignore other keys).

## Root Cause
- Crash:
  - `Because we emit iteration over modulelists or tuples as unrolled loops, we do not support break or continue inside the body of these loops`
- Failure path:
  - `wayve/ai/zoo/deployment/behavior_customization.py`
  - loop over `self.driving_controls_keys` used `continue` in the non-DILC branch.

## Code Changes
- `wayve/ai/zoo/deployment/behavior_customization.py`
  - Removed `else: continue` in the control-key loop.
  - Kept functional behavior unchanged:
    - apply masking only for `DrivingControlKey.DILC_MODE`
    - pass through all other control keys.

## Validation
- `bazel test //wayve/ai/zoo/deployment:test_deployment_py_test --test_arg='-k=behavior_customizer'`
  - Passed.

## Experiment Run Ledger
- `velociraptor-proficient-ivory-125547`
  - Change tested: latest branch after prior control-key fix.
  - Targeted issue: training/export scriptability of behavior customization path.
  - Outcome: fail due to TorchScript loop restriction on `continue`; fixed by this patch.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
