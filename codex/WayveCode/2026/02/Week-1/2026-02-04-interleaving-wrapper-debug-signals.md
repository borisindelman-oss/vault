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
- Split interleaving wrapper into radar vs non-radar variants to avoid invalid argument counts during scripting.
- Updated interleaved deploy script to regenerate output keys from the wrapper to include the new debug outputs.
- Inferred baseline input keys from TorchScript signature to decide whether gear/controls should be passed.
- Prefer TorchScript `schema` when available to infer inputs reliably.
- Fall back to detecting `ParkingDeploymentWrapper` by qualified name when inference is missing.
- When schema is present but names are missing, scan the schema string for parking input names.
- Split interleaving wrappers by whether the baseline expects parking inputs to avoid invalid call signatures during scripting.

## Files
- /workspace/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py
- /workspace/WayveCode/wayve/ai/si/deploy_interleaved.py
