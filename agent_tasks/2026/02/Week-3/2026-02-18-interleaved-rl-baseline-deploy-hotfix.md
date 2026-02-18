# Interleaved RL Baseline Deploy Hotfix (Temporary, Uncommitted)

Date: 2026-02-18
Repo: `/workspace/WayveCode`
Branch: `zmurez/pudo`

## Context
Deploy command for interleaving primary parking BC session with RL baseline wrapper failed in multiple stages:
- malformed `full_config.yml` fallback path
- TD3 legacy config compatibility issues
- checkpoint tensor shape mismatch (`radar_input_adaptor.mask_token` 512 vs 1536)
- radar argument propagation and TorchScript typing/branching issues inside interleaving wrapper

## Temporary code changes applied
- `wayve/ai/si/deploy_interleaved_models.py`
  - deploy-time TD3 config migration:
    - remove `model.pca_action_space`
    - remove `model.reward_encoder.compile_mode`
    - set `model.pretrained_bc_model.checkpoint_load_function = None`
  - tolerant TD3 checkpoint loading:
    - load `state_encoder`/`policy` with shape filtering + `strict=False`
    - log skipped mismatched keys
  - normalize baseline/primary input signatures to wrapper signature before building interleaving wrapper.

- `wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py`
  - static interleaving wrapper uses radar-enabled generated wrapper
  - forward path now passes radar tensors to baseline model calls
  - TorchScript-safe call paths for current combo:
    - baseline call: with radar
    - primary call: without radar
  - keep static input/output key normalization for wrapper deployment config.

## Experiment run ledger
1. `__interleaved_temp_no_upload` (first rerun)
- Change: TD3 migration + mismatch filtering active.
- Targeted issue: `StateEncoder` size mismatch crash.
- Outcome: passed mismatch stage; failed later because baseline wrapper required radar args not forwarded.

2. `__interleaved_temp_no_upload` (after initial radar pass-through)
- Change: passed radar tensors when model signature indicated radar.
- Targeted issue: missing radar positional args.
- Outcome: failed TorchScript with `Optional[Tensor]` passed to Tensor-only radar args.

3. `__interleaved_temp_no_upload` (after radar-enabled generated wrapper + Tensor radar types)
- Change: wrapper with radar inputs + non-optional radar arg types.
- Targeted issue: TorchScript Optional/Tensor type mismatch.
- Outcome: failed TorchScript because compiled alternate no-radar baseline branch (`Argument radar_data not provided`).

4. `__interleaved_temp_no_upload` (after removing mixed-signature branches)
- Change: fixed compile-time call signatures (baseline always with radar, primary without radar).
- Targeted issue: TorchScript branch compile failure.
- Outcome: success; model compiled/saved locally, command exited `0`.

## Successful artifact
- `/mnt/remote/azure_session_dir/Parking/parking/session_2026_02_04_13_44_32_si_parking_bc_train_wfm_october_2025_pudo_only_31.01_october_wfm_bc__interleaved_temp_no_upload/traces/model-000100000.torchscript`

## Notes
- No commit was created.
- Local working tree remains dirty with temporary deploy-only changes.
