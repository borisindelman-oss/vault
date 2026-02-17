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

## Code Changes
- `wayve/ai/zoo/data/parking.py`
  - Added naive stopping-mode heuristic:
    - no neutral detected -> random PARK/PUDO
    - neutral + hazard -> PUDO
    - neutral + no hazard -> PARK
  - Added stack compatibility by writing `"stopping_mode"` key directly.
- `wayve/ai/zoo/data/test/test_parking.py`
  - Added naive stopping-mode behavior tests + missing indicator guard.
  - Updated assertions to use `"stopping_mode"` key on this stack base.

## Validation
- `bazel test //wayve/ai/zoo/data:py_test --test_filter=test_parking --test_output=errors` -> PASS
- No `otf.py`/`test_otf.py` changes are included in this pre-`#94961` branch.
