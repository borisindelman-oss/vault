# Import/check run for deploy_interleaved_models on updated PUDO branch

Date: 2026-02-19
Branch: `boris/interleaved/updated_pudo_15_02_26`

## Command run
```bash
bazel run //wayve/ai/si:deploy_interleaved_models -- \
  --baseline_model_session_path /mnt/remote/azure_session_dir/BaselineCandidates/candidate-structured-testing/session_2026_01_23_09_39_08_si_candidate_2026_5_4_baseline_rl_bl_45_65_85_flourishing-pink-roadrunner \
  --session_id session_2026_02_15_13_01_33_si_parking_bc_train_release_2026_5_4_pud_only_bc_release_2026_5_4_b3.0.1 \
  --suffix __interleaved_silver-harmonious-lark \
  --enable_parking \
  --with_temporal_caching true \
  --baseline_model_load_mode wrapper \
  --primary_model_load_mode wrapper \
  --dilc_on
```

## Result
Failed before runtime/import stage due missing Bazel target in `wayve/ai/si/BUILD`:
- `ERROR: ... no such target '//wayve/ai/si:deploy_interleaved_models'`

## Missing build wiring compared to source branch
- `wayve/ai/si/BUILD`: missing `py_binary(name = "deploy_interleaved_models", ...)` (and `deploy_interleaved` block)
- `wayve/ai/zoo/deployment/BUILD`: `interleaving_stopping_wrapper.py` missing from `py_library(name = "deployment", srcs=[...])`
