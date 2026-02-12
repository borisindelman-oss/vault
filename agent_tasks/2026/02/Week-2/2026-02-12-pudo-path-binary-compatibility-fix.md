# 2026-02-12 — PUDO train fix: path/frame binary compatibility

## Summary
- Investigated failed training run `koala-crimson-unclouded-125607`.
- Root cause was path/frame incompatibility while reading driving path data under `driving/release/2.7.93/wo_path_data`.
- Reverted parking datamodule binary version to `2.7.73` to align with January release data compatibility.

## Root Cause
- First crash happened on `master-0`; worker NCCL/TCPStore broken-pipe logs were downstream.
- Master logs repeatedly showed:
  - `DistanceOutOfRangeException`
  - `bad_path ... Please ensure that the path binary and frame binary versions are compatible`
  - `Failed to load path data from data_file_path='driving/release/2.7.93/wo_path_data/...`.
- Config had `parking_bc_datamodule_cfg.binary_version="2.7.93"`, which diverged from release baseline (`2.7.73`) used for this bucket set.

## Code Changes
- `wayve/ai/si/configs/parking/parking_config.py`
  - Changed `parking_bc_datamodule_cfg.binary_version`:
    - from `"2.7.93"`
    - to `"2.7.73"`

## Validation
- Confirmed failure signature from Datadog logs for `koala-crimson-unclouded-125607` (master pod).
- Confirmed config diff locally.
- Full training rerun pending.

## Experiment Run Ledger
- `koala-crimson-unclouded-125607`
  - Change tested: prior config state with `binary_version=2.7.93`.
  - Targeted issue: continue after TorchScript-related fixes.
  - Outcome: fail with repeated path/frame compatibility errors and `DistanceOutOfRangeException`; fixed by reverting to `2.7.73`.

## Related
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
- Branch: `boris/train/pudo_11_02_26`
