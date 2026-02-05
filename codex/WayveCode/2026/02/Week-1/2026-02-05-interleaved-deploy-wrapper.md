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

## Tests
- `bazel build //wayve/ai/si:deploy_interleaved_models`

## Files
- /workspace/WayveCode/wayve/ai/si/deploy_interleaved_models.py
- /workspace/WayveCode/wayve/ai/zoo/deployment/interleaving_stopping_wrapper.py
- /workspace/WayveCode/wayve/ai/si/BUILD
- /workspace/WayveCode/wayve/ai/zoo/deployment/BUILD
