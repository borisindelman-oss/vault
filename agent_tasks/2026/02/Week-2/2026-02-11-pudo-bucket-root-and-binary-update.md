# 2026-02-11 — PUDO bucket root + binary update

## Summary
- Updated parking/PUDO datamodule bucket routing in `wayve/ai/si/configs/parking/parking_config.py`.
- Set parking/PUDO bucket root to:
  - `materialised/si/parking/dev/2026_02_03_10_30_34_server_parking_pudo_buckets_bc`
- Set bucket roots to:
  - `PARKING_PUDO_BUCKETS_ROOT` for legacy driving buckets, PUDO buckets, and parking validation buckets.
  - `DS_26_01_06_SERVER_GEN2_IPACE` only for:
    - `dc_high_lateral_acceleration_uk`
    - `dc_high_lateral_acceleration_usa`
    - `pre_ca_all_gen1`
- Added missing release buckets:
  - `dc_high_lateral_acceleration_uk`
  - `dc_high_lateral_acceleration_usa`
  - `pre_ca_all_gen1`
- Bumped `binary_version` to `3.0.1`.
- Re-normalized driving sampling scale to keep 93% target after added release buckets (`driving_weight = 0.93 / 0.695`).

## Validation
- `python3 -m py_compile wayve/ai/si/configs/parking/parking_config.py` passed.

## Links
- Project: [[projects/pudo-update-january-driving-release-2026-5-4]]
