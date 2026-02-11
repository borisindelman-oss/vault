# Inference model design (MVC)

## Summary
- Documented MVP InferenceModel plan: reuse existing SI visualisation loaders/wrapper, support both deployment wrapper and TorchScript, no caching.
- Captured smoke test plan using real session path + run segment to validate load and interface contract.

## InferenceModel (MVP)
- Reuse existing stack: `load_model` + `VisualisationModelWrapper`.
- Support both load paths:
  - Deployment wrapper: `wayve/ai/si/visualisation/pack_model.py` (unwrap training module + deployment config).
  - TorchScript: `wayve/ai/si/visualisation/inference_model.py` (`load_ingested_model_from_session_id`).
- No caching/stateful inference for MVP.
- Interface goal: `infer_batch(inputs)` returns outputs dict with standard DataKeys used by Plotly views.

## Smoke test plan
- Model source:
  - Session path: `/mnt/remote/azure_session_dir/Parking/parking/session_2026_01_05_22_16_44_si_parking_bc_train_parking_bc_w_temporal_caching_reverse_fix___waypoints_reverse_amplification`
- Data source:
  - Run segment: `run_id=fme10008/2024-11-23--05-17-45--gen2-dc-b972e3fe-0cf7-4baf-bf99-a88f29f3b2dd`
  - `from_unixus=1732339460424837`, `to_unixus=1732339474716245`
- Steps:
  - Load model via `load_model` (session checkpoint + config), wrap with `VisualisationModelWrapper`.
  - Load one batch via `RunSegment` + `get_datapipe` + `get_dataloader`.
  - Run `VisualisationModelWrapper(inputs)`.
  - Assert outputs include `DataKeys.POLICY_WAYPOINTS`.
