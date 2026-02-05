# Visualise interleaving wrapper

- Topic: bokeh visualise uses route-interleaving wrapper
- Labels: #visualisation #interleaving #parking
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/si/visualisation/`

## Changes
- Added baseline session id support to `visualise.py` to build the route-interleaving wrapper for visualisation.
- Added route signal thresholds args for near-end and no-route behavior.
- Disabled parking wrapper end-of-route triggering when interleaving.
- Ensured driving_controls and driving_parameters are supplied even when inputs are missing by falling back to deployment_config in `VisualisationModelWrapper`.

## Files
- /workspace/WayveCode/wayve/ai/si/visualisation/bokeh/visualise.py
- /workspace/WayveCode/wayve/ai/si/visualisation/inference_model.py
