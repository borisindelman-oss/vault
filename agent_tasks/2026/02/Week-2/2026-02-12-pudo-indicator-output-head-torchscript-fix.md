# 2026-02-12 — PUDO train fix: Indicator output head TorchScript int capture

## Summary
- Investigated failed training run `wrasse-cosmic-rose-125532`.
- Root cause was TorchScript rejecting a closed-over global int constant in `IndicatorOutputHead._forward(...)`.
- Updated indicator expansion to a TorchScript-safe shape-preserving expand call.

## Root Cause
- Crash:
  - `python value of type 'int' cannot be used as a value ... NUM_PREDICTED_VEHICLE_INDICATORS`
- Failure path:
  - `wayve/ai/zoo/outputs/indicator_output_head.py` used:
    - `indicators.expand(tokens.shape[0], self.future_frames, NUM_PREDICTED_VEHICLE_INDICATORS)`
  - During scripted compilation, the global int constant was treated as a closed-over Python value and rejected.

## Code Changes
- `wayve/ai/zoo/outputs/indicator_output_head.py`
  - Replaced explicit constant-based expand with:
    - `indicators = indicators.expand(-1, self.future_frames, -1)`
  - This keeps batch/class dimensions from the tensor and only expands the temporal dimension.

## Validation
- `bazel test //wayve/ai/zoo:test_outputs_py_test --test_arg='-k=indicator_output_head'`
  - Passed.

## Experiment Run Ledger
- `wrasse-cosmic-rose-125532`
  - Change tested: latest parking/PUDO branch state before this patch.
  - Targeted issue: post-wrapper/startup training compile path.
  - Outcome: fail with TorchScript closed-over int error in `IndicatorOutputHead`; fixed by this patch.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
