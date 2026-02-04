# Interleaving wrapper debug signals

- Topic: interleaving wrapper debug outputs + radar arg fix
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/zoo/deployment/`, `wayve/ai/si/`

## Changes
- Added a dedicated `InterleavingOnBoardDrivingOutput` named tuple that extends `OnBoardDrivingOutput` with `interleaved_id` and `interleaved_event` for logging visibility.
- Emitted `interleaved_id` (0 baseline / 1 parking) and `interleaved_event` (1 on switch, else 0) from `InterleavingDeploymentWrapperImpl`.
- Avoided passing radar arguments to models when the wrapper is built without radar inputs (fixes argument count mismatch during scripting).
- Updated interleaved deploy script to regenerate output keys from the wrapper to include the new debug outputs.

## Files
- /workspace/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py
- /workspace/WayveCode/wayve/ai/si/deploy_interleaved.py
