# 2026-02-17 — Naive stopping_mode hazard stacked PR alignment

## Summary
- Rebased/scoped naive stopping_mode hazard work to stack cleanly on `origin/soham/otf-gear-input` (PR #94961 lineage).
- Kept this branch diff focused to four files and hazard-related logic only for [[projects/parking-stopping-mode-naive-heuristic]].
- Added stack-compatibility fix so `stopping_mode` is written as legacy raw key (`"stopping_mode"`) instead of `DataKeys.STOPPING_MODE` on this base.

## Branch / Commits
- Branch: `boris/stopping_mode_hazard_stack`
- Commits:
  - `13a1fcce19a` — `feat: add naive stopping mode hazard heuristic`
  - `30d67525706` — `fix: use legacy stopping_mode key on otf-gear-input stack`

## Code Changes
- `wayve/ai/si/datamodules/otf.py`
  - Added `enable_naive_stopping_mode` flag plumbing.
  - Enabled parking lookahead path for naive mode and added indicator lookahead gather (`additional_parking_indicator_light`).
  - Passed naive mode flag into `insert_parking_data`.
  - Extended timeslicer with indicator lookahead indices.
- `wayve/ai/zoo/data/parking.py`
  - Added naive stopping-mode heuristic:
    - no neutral detected -> random PARK/PUDO
    - neutral + hazard -> PUDO
    - neutral + no hazard -> PARK
  - Added stack compatibility by writing `"stopping_mode"` key directly.
- `wayve/ai/si/datamodules/test/test_otf.py`
  - Added assertions for indicator lookahead and naive flag forwarding.
  - Added timeslicer coverage for parking indicator lookahead indices.
- `wayve/ai/zoo/data/test/test_parking.py`
  - Added naive stopping-mode behavior tests + missing indicator guard.
  - Updated assertions to use `"stopping_mode"` key on this stack base.

## Validation
- `bazel test //wayve/ai/zoo/data:py_test --test_filter=test_parking --test_output=errors` -> PASS
- `bazel test //wayve/ai/si/datamodules:py_test --test_arg='-k' --test_arg='parking_and_gear_direction_hooks or adds_parking_indicator_lookahead' --test_output=errors`
  - Selected tests passed; target fails coverage threshold when heavily filtered (expected for this target config).
- Full `//wayve/ai/si/datamodules:py_test` currently shows an unrelated existing `test_sarsa` dtype failure in this environment; not modified in this scoped hazard delta.
