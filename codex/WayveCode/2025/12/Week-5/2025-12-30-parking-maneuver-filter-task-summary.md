# 2025-12-30 — Task Summary — Add parking maneuver filter for pred_park_type

- Status: done
- Goal: Port experimental parking maneuver windowing logic into SI materialization as a reusable filter and add a unit test.
- Notes: Will update as implementation and tests progress.

## Progress
- Implemented parking maneuver mask helper and pred_park_type maneuver filter.
- Wired pred_park_type into annotation loading with allow_pickle handling.
- Added a unit test for indicator-based maneuver expansion.

## Next
- Run relevant tests (filters test) and update logs with results.

## Test Status
- `python -m pytest /workspace/WayveCode/wayve/ai/zoo/test/sampling/test_filters.py -k parking_maneuver --maxfail=1`
  - Failed: pytest not installed in environment (`No module named pytest`).
- Added pylint suppression on get_parking_indices after bazel lint failure.

## Tests
- `bazel test //wayve/ai/zoo:test_sampling_py_test //wayve/ai/zoo:test_sampling_py_lint_pylint --test_output=errors` (PASS)

## References (zmurez/trt)
- `wayve/ai/experimental/dataset/single_run.py#L321`: gear cleanup to remove false gear changes (e.g., neutral shifts). https://github.com/wayveai/WayveCode/blob/zmurez/trt/wayve/ai/experimental/dataset/single_run.py#L321
- `wayve/ai/experimental/dataset/single_run.py#L332`: parking mask creation (frames considered parking). https://github.com/wayveai/WayveCode/blob/zmurez/trt/wayve/ai/experimental/dataset/single_run.py#L332
- `wayve/ai/experimental/dataset/single_run.py#L478`: dataloader get_item logic that uses parking signals. https://github.com/wayveai/WayveCode/blob/zmurez/trt/wayve/ai/experimental/dataset/single_run.py#L478
- `wayve/ai/experimental/samplers/sampler.py#L996`: filter to avoid sampling bad parking. https://github.com/wayveai/WayveCode/blob/zmurez/trt/wayve/ai/experimental/samplers/sampler.py#L996
