# SI config migration conflict fix after merge from main

## Context
Merged `origin/main` into branch `02-12-park-pudo-stopping-mode-heuristic` and resolved BC migration version collision where both sides defined `migrate_to_v17` differently.

## What changed
- Kept `origin/main` logic as `migrate_to_v17` in `wayve/ai/si/configs/versioning/bc_migrations.py`:
  - removes `enable_alpha_profiler_callback`, `alpha_interval`, `use_weightwatcher`
  - adds `enable_alpha_logging` and `log_alpha_every_n_steps`
- Moved branch-specific stopping-mode migration into new `migrate_to_v18` and registered `18: migrate_to_v18` in `BC_CONFIG_MIGRATION_FUNCTIONS`.
- Bumped BC source-of-truth version to `18` in `wayve/ai/si/config.py`.
- Accepted incoming historical snapshot for `wayve/ai/si/test/data/sample_configs/bc/v17.yaml` (kept identical to `origin/main`).
- Generated new BC snapshot `wayve/ai/si/test/data/sample_configs/bc/v18.yaml` via:
  - `bazel run //wayve/ai/si/scripts:dump_sample_cfg_for_migration_checks -- --training_stage=bc`
- Updated BC reference configs to `config_version.version_number: 18`:
  - `wayve/ai/si/test/test_config_inputs/reference_bc.yaml`
  - `wayve/ai/si/test/test_config_inputs/reference_bc_alpha2.yaml`

## Additional consistency fix (outside merge conflict)
During `//wayve/ai/si:test_config`, RL regression refs failed because branch already had `rl_config_version=22` while RL reference files still used `21`.
- Updated `wayve/ai/si/test/test_config_inputs/reference_rl.yaml` to `22`.
- Updated `wayve/ai/si/test/test_config_inputs/reference_rl_alpha2.yaml` to `22` and moved `config_version` block to match actual baseline ordering.

## Validation
- `bazel test //wayve/ai/si:test_config_py_test --test_output=errors --test_arg='-k=bc_migrations'` ✅
- `bazel test //wayve/ai/si:test_config --test_output=errors` ❌ initially failed only on RL baseline refs (`test_regression[rl]`, `test_regression[rl_alpha2]`) due stale version/order
- `bazel test //wayve/ai/si:test_config_py_test --test_output=errors --test_arg='-k=test_regression and (rl_alpha2 or rl)'` ✅ after RL ref updates

## Files touched for this task
- `wayve/ai/si/config.py`
- `wayve/ai/si/configs/versioning/bc_migrations.py`
- `wayve/ai/si/test/data/sample_configs/bc/v17.yaml`
- `wayve/ai/si/test/data/sample_configs/bc/v18.yaml`
- `wayve/ai/si/test/test_config_inputs/reference_bc.yaml`
- `wayve/ai/si/test/test_config_inputs/reference_bc_alpha2.yaml`
- `wayve/ai/si/test/test_config_inputs/reference_rl.yaml`
- `wayve/ai/si/test/test_config_inputs/reference_rl_alpha2.yaml`
