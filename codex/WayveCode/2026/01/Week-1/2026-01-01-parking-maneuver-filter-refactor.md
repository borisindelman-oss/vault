# 2026-01-01 — Parking maneuver filter refactor

- Status: in progress
- Goal: simplify parking maneuver filters by sharing transition logic and clarifying label-based windows.
- Branch: boris/2025-12-30/zak-classifiers-parking-maneuver
- Related: [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]

## Progress
- Added shared helper for parking transition entry/exit indices.
- Reused shared transition logic in parking indices and maneuver windowing.
- Kept maneuver window filtering based on label presence within the window.
- Added a focused unit test for transition duration filtering.

## Tests
- Not run (new test added for transition filtering).

## Next
- Run `bazel test //wayve/ai/zoo:test_sampling_py_test`.
