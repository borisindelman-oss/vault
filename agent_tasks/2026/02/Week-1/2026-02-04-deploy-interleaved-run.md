# Deploy interleaved run

- Topic: deploy interleaved for parking/baseline session
- Labels: #parking #deployment #interleaving #run
- Branch: current
- PR: none
- Change type: run
- Areas: `wayve/ai/si/`

## Command
- `bazel run //wayve/ai/si:deploy_interleaved -- --baseline_session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --parking_session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --output_dir /tmp/interleaved_sessions --suffix _interleaved_pudo`

## Output
- Saved compiled model: `/tmp/interleaved_sessions/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc_interleaved_pudo/traces/model-000000001.torchscript`
- Output directory: `/tmp/interleaved_sessions/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc_interleaved_pudo/`

## Notes
- Warnings: Azure identity env not configured; Datadog app_key/statsd missing; TorchScript MonkeyType warnings.
- Run completed successfully.
