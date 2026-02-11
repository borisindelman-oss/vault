# 2026-01-21 — Task Summary — stopping_mode adaptor (Stage 1)

- Status: done
- Goal: Add a new `stopping_mode` model input adaptor and wire it through the parking model configs/tests.

## Progress
- Added DataKeys.STOPPING_MODE and created `StoppingModeSTAdaptor` (2-class embedding).
- Registered stopping_mode in adaptor ordering and exports; added checkpoint backfill for older weights.
- Wired optional use_stopping_mode_adaptor in ST model builder and parking configs (default off).
- Added adaptor unit tests and parameterized adaptor coverage for stopping_mode.

## Tests
- Not run (suggested): `bazel test //wayve/ai/zoo/st:test_st --test_output=errors`

## Files
- `wayve/ai/zoo/data/keys.py`
- `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
- `wayve/ai/zoo/st/input_adaptors/__init__.py`
- `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py`
- `wayve/ai/zoo/st/models.py`
- `wayve/ai/zoo/st/checkpoints.py`
- `wayve/ai/zoo/st/test/test_adaptors.py`
- `wayve/ai/zoo/st/test/test_adaptors_params.py`
- `wayve/ai/zoo/st/BUILD`
- `wayve/ai/si/configs/parking/parking_config.py`
- `wayve/ai/si/models/training.py`
