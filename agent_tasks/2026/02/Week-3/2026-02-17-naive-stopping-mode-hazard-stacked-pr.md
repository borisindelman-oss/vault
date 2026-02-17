# 2026-02-17 — Naive stopping_mode hazard stacked PR alignment

## Summary
- Rebased/scoped naive stopping_mode hazard work to stack cleanly on `origin/02-11-parking_mode_heuristic`, positioned before `soham/otf-gear-input` (PR #94961).
- Kept this branch diff focused to parking hazard logic only for [[projects/parking-stopping-mode-naive-heuristic]].
- Added stack-compatibility fix so `stopping_mode` is written as legacy raw key (`"stopping_mode"`) instead of `DataKeys.STOPPING_MODE` on this base.

## Branch / Commits
- Branch: `boris/stopping_mode_hazard_stack`
- Commits:
  - `4a16c64fce5` — `feat: add naive stopping mode hazard heuristic`
  - `ad689381282` — `fix: use legacy stopping_mode key on otf-gear-input stack`
  - `e4c093c2b4c` — `fix: base naive stopping mode on parking window`
  - `0c3a72418d7` — `feat: add stopping mode adaptor and parking key wiring`

## Code Changes
- `wayve/ai/zoo/data/parking.py`
  - Added naive stopping-mode heuristic:
    - `parking_mode == False` -> random PARK/PUDO
    - `parking_mode == True` + hazard -> PUDO
    - `parking_mode == True` + no hazard -> PARK
  - Writes `DataKeys.STOPPING_MODE` in data output.
- `wayve/ai/zoo/data/test/test_parking.py`
  - Added naive stopping-mode behavior tests + missing indicator guard.
  - Added regression that hazard is ignored when `parking_mode=False` (random branch still used).
  - Updated assertions to use `DataKeys.STOPPING_MODE`.
- `wayve/ai/zoo/data/keys.py`
  - Added `STOPPING_MODE` key constant.
- `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
  - Added `StoppingModeSTAdaptor` with tokenization for `STOPPING_MODE` values (`2=park`, `3=pudo`) and dropout fallback for out-of-range values.
- `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py`
  - Added `stopping_mode` into adaptor ordering.
- `wayve/ai/zoo/st/input_adaptors/__init__.py`
  - Exported `StoppingModeSTAdaptor`.
- `wayve/ai/zoo/st/models.py`
  - Added `use_stopping_mode_adaptor` and `stopping_mode_dropout_probability` flags.
  - Wires `StoppingModeSTAdaptor` into model input adaptors when enabled.
- `wayve/ai/zoo/st/checkpoints.py`
  - Added compatibility loading for missing `stopping_mode` adaptor weights when loading pretraining checkpoints.
- `wayve/ai/zoo/st/test/test_adaptors.py`
  - Added unit test for `StoppingModeSTAdaptor`.
- `wayve/ai/zoo/st/test/test_adaptors_params.py`
  - Added parameterized coverage for `stopping_mode` modality.
- `wayve/ai/zoo/st/BUILD`
  - Included `input_adaptors/stopping_mode.py`.

## Validation
- `bazel test //wayve/ai/zoo/data:py_test --test_filter=test_parking --test_output=errors` -> PASS
- `bazel test //wayve/ai/zoo/st:test_st --test_output=errors` -> PASS
- No `otf.py`/`test_otf.py` changes are included in this pre-`#94961` branch.
