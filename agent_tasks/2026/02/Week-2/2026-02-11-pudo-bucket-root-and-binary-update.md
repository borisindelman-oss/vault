# 2026-02-11 — PUDO bucket root + binary update

## Summary
- Updated parking/PUDO datamodule bucket routing in `wayve/ai/si/configs/parking/parking_config.py`.
- Set parking/PUDO bucket root to:
  - `materialised/si/parking/dev/2026_02_03_10_30_34_server_parking_pudo_buckets_bc`
- Set release buckets root to:
  - `DS_26_01_06_SERVER_GEN2_IPACE`
- Added missing release buckets:
  - `dc_high_lateral_acceleration_uk`
  - `dc_high_lateral_acceleration_usa`
  - `pre_ca_all_gen1`
- Bumped `binary_version` to `3.0.1`.

## Validation
- `python3 -m py_compile wayve/ai/si/configs/parking/parking_config.py` passed.

## Links
- Project: [[projects/pudo-update-current-driving-release]]
