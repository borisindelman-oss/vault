# 2026-02-12 — Naive stopping_mode Phase 2 (adaptor plumbing)

## Summary
- Implemented Phase 2 for [[projects/parking-stopping-mode-naive-heuristic]] on branch `02-12-park-pudo-stopping-mode-heuristic`.
- Added model-side `stopping_mode` adaptor plumbing behind default-off flags.
- Added BC/RL config migrations and updated migration sample snapshots/reference configs to keep config tests green.

## Code Changes
- Added new data key and ST adaptor wiring:
  - `wayve/ai/zoo/data/keys.py`
  - `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
  - `wayve/ai/zoo/st/input_adaptors/__init__.py`
  - `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py`
  - `wayve/ai/zoo/st/models.py`
  - `wayve/ai/zoo/st/BUILD`
  - `wayve/ai/zoo/st/test/test_adaptors.py`
  - `wayve/ai/zoo/st/test/test_adaptors_params.py`
- Added SI config flag default:
  - `wayve/ai/si/config.py` (`use_stopping_mode_adaptor=False`)
- Added migration support for new model args:
  - BC: `wayve/ai/si/configs/versioning/bc_migrations.py` (`migrate_to_v14`)
  - RL: `wayve/ai/si/configs/versioning/rl_migrations.py` (`migrate_to_v17`)
  - Version bumps:
    - `wayve/ai/si/config.py` (`bc_version=14`)
    - `wayve/ai/si/configs/store/offline_rl.py` (`rl_config_version=17`)
- Updated config regression/reference fixtures:
  - `wayve/ai/si/test/test_config_inputs/reference_bc.yaml`
  - `wayve/ai/si/test/test_config_inputs/reference_bc_alpha2.yaml`
  - `wayve/ai/si/test/test_config_inputs/reference_rl.yaml`
  - `wayve/ai/si/test/test_config_inputs/reference_rl_alpha2.yaml`
  - Added sample configs:
    - `wayve/ai/si/test/data/sample_configs/bc/v14.yaml`
    - `wayve/ai/si/test/data/sample_configs/rl/v17.yaml`

## Validation
- Ran: `bazel test //wayve/ai/si:test_config_py_test --test_output=errors`
- Result: PASS (includes migration structure checks + baseline regression checks).
- Generated missing migration snapshots via:
  - `bazel run //wayve/ai/si/scripts:dump_sample_cfg_for_migration_checks -- --training_stage=bc`
  - `bazel run //wayve/ai/si/scripts:dump_sample_cfg_for_migration_checks -- --training_stage=rl`

## Next Phase
- Phase 3: OTF + parking heuristic wiring (`indicator` lookahead + naive stopping_mode assignment + tests).
