# 2026-01-06 — Task Summary — Parking WFM December 2025 Modes

## Scope
- Add December 2025 WFM base config and mode in SI config system.
- Add parking model configs and modes that use the December 2025 WFM base.
- Preserve parking-specific overrides while switching training module defaults to StBcCfg in the new configs.

## Project
- [[WayveCode/projects/parking-wfm-update]]

## Changes
- Added WFMStDecember2025Cfg, wfm_space_time_december_2025_bc_cfg, and BCWFMStDecember2025Cfg.
- Registered new base mode: wfm_december_2025_bc.
- Added parking_bc_wfm_december_2025_cfg and parking_bc_wfm_december_2025_debug_cfg.
- Added parking modes: parking_bc_train_wfm_december_2025 and parking_bc_debug_wfm_december_2025.

## Files
- /workspace/WayveCode/wayve/ai/si/config.py
- /workspace/WayveCode/wayve/ai/si/configs/parking/parking_config.py

## Notes
- No tests run (per request).
- December checkpoint path sourced from foundation PRETRAINED_MODELS (WFM_v1.3.0.550M(1.4.0)).
