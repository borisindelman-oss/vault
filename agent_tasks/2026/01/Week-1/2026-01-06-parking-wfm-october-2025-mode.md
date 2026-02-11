# 2026-01-06 — Task Summary — Parking WFM October 2025 Mode

## Scope
- Add new parking model configs and modes that use the October 2025 WFM base.
- Preserve parking-specific overrides while switching training module defaults to StBcCfg in the new configs.
- Keep existing parking modes unchanged for A/B comparison.

## Project
- [[projects/parking-wfm-update]]

## Changes
- Added parking_bc_wfm_october_2025_cfg and parking_bc_wfm_october_2025_debug_cfg (StBcCfg-based).
- Added ParkingBcTrainWfmOctober2025Cfg and ParkingBcDebugWfmOctober2025Cfg based on BCWFMStOctober2025Cfg.
- Registered new modes: parking_bc_train_wfm_october_2025 and parking_bc_debug_wfm_october_2025.

## Files
- /workspace/WayveCode/wayve/ai/si/configs/parking/parking_config.py

## Notes
- No tests run (per request).
- Next: add December WFM variant once confirmed, then compare training runs before removing old mode.
