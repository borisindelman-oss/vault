# 2026-02-12 — PUDO train fix: BehaviorCustomizer non-DILC control keys

## Summary
- Investigated failed training run `koala-perplexing-blush-125494`.
- Root cause was behavior-customization code raising on non-DILC driving control keys when parking/PUDO key tuples were passed.
- Updated behavior customization to consume only `DILC_MODE` and ignore other control keys.

## Root Cause
- Crash:
  - `ValueError('Unsupported driving control key: 0')`
- Failure path:
  - `BehaviorCustomizer.forward(...)` iterated `deployment_driving_controls_keys=(0, 1, 3, 2)`.
  - It correctly handled `DILC_MODE` (`2`) but raised for the preceding parking keys (`0`, `1`, `3`).
- In this deployment path, those non-DILC keys are valid for parking wrappers/processors and should not be rejected by behavior customization.

## Code Changes
- `wayve/ai/zoo/deployment/behavior_customization.py`
  - Replaced the non-DILC `raise ValueError(...)` branch with `continue`.
  - Kept DILC masking behavior unchanged.
- `wayve/ai/zoo/deployment/test/test_behavior_customization.py`
  - Replaced unsupported-control negative test with `test_behavior_customizer_ignores_non_dilc_control_keys`.
  - Added `test_behavior_customizer_mixed_controls_applies_dilc_only` to cover mixed parking + DILC key tuples.

## Validation
- `bazel test //wayve/ai/zoo/deployment:test_deployment_py_test --test_arg='-k=test_behavior_customizer_ignores_non_dilc_control_keys or test_behavior_customizer_mixed_controls_applies_dilc_only'`
  - Passed.
- `bazel test //wayve/ai/si:test_deployment_wrapper`
  - Passed.

## Experiment Run Ledger
- `black-flamingo-fiery-125307`
  - Change tested: previous config update before this fix.
  - Targeted issue: model init failure path.
  - Outcome: fail; different upstream issue, resolved separately.
- `jellyfish-moccasin-singing-125420`
  - Change tested: checkpoint/bucket adjustments.
  - Targeted issue: training startup after adaptor updates.
  - Outcome: fail; progressed to control-key path.
- `koala-perplexing-blush-125494`
  - Change tested: latest branch with wrapper/key updates.
  - Targeted issue: deployment behavior path compatibility.
  - Outcome: fail with `Unsupported driving control key: 0`; fixed by this patch.

## Related
- Project: [[projects/pudo-update-current-driving-release]]
- Branch: `boris/train/pudo_11_02_26`
