# Interleaved Compile vs Zak (`zmurez/pudo`)

## Scope
- Compared `wayve/ai/si/deploy_interleaved_models.py` + `wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py` against `zmurez/pudo:wayve/ai/experimental/compile_with_baseline.py`.
- Reproduced deploy command and validated compile path.

## Findings
- Zak keeps interleaving state as plain Python attributes.
- Our wrapper used `torch.jit.Attribute(...)` for mutable state and failed in eager pre-script validation in `compile_model`.
- Failure observed: `TypeError: can't multiply sequence by non-int of type 'float'` at `_distance_since_end_of_route_m += current_speed * self.inference_dt_s`.

## Fix
- Updated `RouteInterleavingWrapperImpl` to keep routing state as plain Python attributes.
- Kept index maps as registered tensor buffers for JIT-safe `index_select`.
- Re-ran deploy compile command successfully with suffix `__interleaved4_check2` (no upload).

## Command used
- `bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix __interleaved4_check2 --dilc_on --enable_parking --with_temporal_caching true`

## Notes
- This addressed compile-time wrapper state failures.
- HIL/runtime perf behavior still needs validation on a newly uploaded artifact.
