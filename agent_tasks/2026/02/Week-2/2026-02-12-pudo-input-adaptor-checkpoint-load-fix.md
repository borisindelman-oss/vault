# 2026-02-12 — PUDO checkpoint load fix for parking adaptors

## Summary
- Investigated training crash after enabling parking adaptors on top of October release backbone.
- Root cause was strict input-adaptor checkpoint loading against a checkpoint that does not contain parking-only adaptor weights.
- Fixed checkpoint loading path to seed missing `gear_direction` / `parking_mode` adaptor keys from model defaults while keeping strict checks for all other expected keys.

## Root Cause
- Runtime error during model init:
  - `RuntimeError: Error(s) in loading state_dict for InputAdaptor`
  - Missing keys under:
    - `adaptors.gear_direction.*`
    - `adaptors.parking_mode.*`
- `load_multi_input_sttransformer_from_wfm_october_pretraining(...)` loads `model.input_adaptor` with `strict=True`.
- Parking/PUDO model adds adaptors not present in the release pretraining checkpoint.

## Code Change
- `wayve/ai/zoo/st/checkpoints.py`
  - In `load_multi_input_sttransformer_from_wfm_october_pretraining(...)`, added targeted fallback:
    - if model has `gear_direction` and/or `parking_mode` adaptors, fill missing keys from their initialized module state before strict load.

## Validation
- `bazel test //wayve/ai/si:test_config --test_output=errors`
  - Passed (`4/4`): mypy, flake8, pylint, config pytest.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
