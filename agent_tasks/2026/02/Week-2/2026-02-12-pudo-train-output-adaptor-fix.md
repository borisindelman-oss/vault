# 2026-02-12 — PUDO train fix: OutputAdaptor behavior-control init

## Summary
- Investigated failed training job `black-flamingo-fiery-125307` in Datadog.
- Root cause was config-time model construction failure in `parking_bc_train_release_2026_5_4`.
- Fixed `ParkingOutputAdaptorCfg` to provide `latent_action_encoder` when behavior control is enabled.

## Root Cause
- Training failed during Hydra object construction:
  - `ValueError('`latent_action_encoder` must be provided if `enable_behavior_control` is True')`
  - `full_key: model.model.output_adaptor`
- In `wayve/ai/si/configs/parking/parking_config.py`, behavior control was enabled for `OutputAdaptor` without passing `latent_action_encoder`.

## Code Changes
- `wayve/ai/si/configs/parking/parking_config.py`
  - Imported `ActionsDiscretizerCfg` from `wayve.ai.si.config`.
  - Added `latent_action_encoder=ActionsDiscretizerCfg()` to `ParkingOutputAdaptorCfg`.
  - Added `enable_latent_action=False` explicitly to keep latent-action outputs disabled.

## Validation
- `bazel test //wayve/ai/si:test_config --test_output=errors`
  - Passed (`4/4`): mypy, flake8, pylint, config pytest.

## Related
- Project: [[projects/pudo-update-current-driving-release]]
- Branch: `boris/train/pudo_11_02_26`
