# Interleaved deploy wrapper

- Topic: route interleaving deploy wrapper + session-id resolution
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/si/`, `wayve/ai/zoo/deployment/`

## Changes
- Reworked `deploy_interleaved_models` to build a route-interleaving wrapper via codegen and save with `save_compiled_model`.
- Generated an explicit TorchScript-friendly wrapper signature that unions baseline/primary inputs and routes by `map_route` end-of-route sum.
- Normalized `map_speed_limits` to `map_speed_limit` and added safeguards for missing `map_route` inputs.
- Added a fallback search for session IDs under `/mnt/remote/azure_session_dir/*/*/<session_id>`.
- Added optional output handling for route interleaving (custom NamedTuple with Optional fields and none-token filling).
- Registered the generated wrapper module in `sys.modules` so `save_compiled_model` can resolve the return type.
- Added an ingested-model fallback when the training session config is unavailable.
- Inferred primary wrapper input keys from `model.forward` to ensure navigation instruction inputs are included when required.
- Replaced the route interleaving codegen path with a static wrapper for the baseline + parking pair.
- Added navigation instruction inputs to the parking wrapper to keep inputs consistent across models.
- Added a latched near‑end‑of‑route trigger, auto‑park trigger, reverse gear trigger, and 5 mph hysteresis for model switching.
- Made end‑of‑route latch distance configurable (0 disables latch).
- Moved the generalized codegen wrapper into `interleaving_stopping_codegen.py` for future reuse.
- Redefined end‑of‑route as “no route available” in the parking wrapper to force parking mode when route data is missing.

## Tests
- `bazel build //wayve/ai/si:deploy_interleaved_models`
- `DEV_VM=0 TMPDIR=/workspace/tmp bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_path /mnt/remote/azure_session_dir/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --baseline_model_cache_dir /workspace/ai_lib_cache --output_dir /workspace/deploy_interleaved --suffix _retrace --dilc_on --enable_parking --with_temporal_caching true`
- `DEV_VM=0 TMPDIR=/workspace/tmp bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix _retrace2 --dilc_on --enable_parking --with_temporal_caching true`
- `DEV_VM=0 TMPDIR=/workspace/tmp bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix _retrace3 --dilc_on --enable_parking --with_temporal_caching true`
- `DEV_VM=0 TMPDIR=/workspace/tmp bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix _retrace10 --dilc_on --enable_parking --with_temporal_caching true`

## Files
- /workspace/WayveCode/wayve/ai/si/deploy_interleaved_models.py
- /workspace/WayveCode/wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py
- /workspace/WayveCode/wayve/ai/zoo/deployment/interleaving_stopping_codegen.py
- /workspace/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py
- /workspace/WayveCode/wayve/ai/si/BUILD
- /workspace/WayveCode/wayve/ai/zoo/deployment/BUILD
