# Interleaving load modes + switch-debug matrix

## Scope
- Updated project and how-to docs for the latest interleaving deployment implementation.
- Synced docs with current `deploy_interleaved_models.py` and `interleaving_stopping_wrapper.py`.
- Logged latest upload/test variants and active HIL failure signature.

## What changed
- Standardized documented load modes:
  - `--primary_model_load_mode`: `wrapper|ingested`
  - `--baseline_model_load_mode`: `wrapper|ingested`
- Documented switch controls:
  - heuristic switching path
  - `--switch_every_n_forwards` periodic toggle path
- Documented cache warmup control:
  - `--num_cache_warmup_frames` including `0` behavior.
- Documented always-on interleaving telemetry:
  - `interleaved_id`, `interleaved_event`.

## Upload/test variants recorded
- `__interleaved6` (known-good reference from current cycle).
- `interleaved_every_30` (periodic switch stress case).
- `__interleaved_every_30_2` (follow-up periodic switch variant).
- `interleaving_30_no_cache` (periodic switch with warmup cache disabled).

## Known runtime issue under investigation
- HIL failures on switch-path variants include:
  - `RuntimeError: This Python function is annotated to be ignored and cannot be run`
  - stack traces through perceiver attention / flash-attention-v2 path.

## Notes
- Console link from latest no-cache periodic upload:
  - `https://console.sso.wayve.ai/model/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bcinterleaving_30_no_cache`
