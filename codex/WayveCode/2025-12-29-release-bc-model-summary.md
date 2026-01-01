# 2025-12-29 — Task Summary — Release BC Model

## Scope
- Goal: Identify the release BC (behavior cloning) mode, plus model and data components.

## Mode
- Release BC mode: `baseline_bc`.
- Location: `/workspace/WayveCode/wayve/ai/si/configs/baseline/release.py`.

## Model
- BC training config: `baseline_bc_model = StBcCfg(model=WFMStOctober2025Cfg())`.
- WFM model config: `WFMStOctober2025Cfg` in `/workspace/WayveCode/wayve/ai/si/config.py`.
- Key pieces: ST transformer backbone, reduced blind-spot preprocessing, behavior-control output adaptor, October 2025 WFM checkpoint load.

## Data
- Datamodule: `baseline_bc_datamodule = BcDataModuleCfg(...)`.
- Implementation: `OtfDrivingDataModule` in `/workspace/WayveCode/wayve/ai/si/datamodules/otf.py`.
- Datasets: `DS_25_10_01_GEN2_IPACE` and `DC_DILC_BUCKETS_25_10_01` across UK/USA/DEU/JPN + CA/pre-CA splits.
- Key settings: `batch_size=2`, `camera_frames=6`, `camera_stride_sec=0.20`, `binary_version=2.7.29`, `path_length=800`.

## Next Trace Steps
- Map the exact Python classes implementing the WFM blocks.
- Enumerate the concrete augmentations invoked for this mode.
