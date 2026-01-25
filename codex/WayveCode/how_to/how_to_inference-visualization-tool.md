# How to build an end-to-end inference visualization tool (new vis tool)

## The story in one paragraph
Engineers need to *see* what the model is doing, not just read metrics. The current Bokeh tool gets us part of the way, but we want a clean MVC-style tool that can run end-to-end inference on demand, swap data sources, and render interactive plots in a consistent way. This project maps the existing pipeline and proposes a new architecture using Dash + Plotly.

## What we built (plain language)
We defined an MVC layout: a model runner, a data source interface, a controller to glue them together, and Plotly views for rendering. The early plan is to reuse the existing SI visualization stack for inference while we build a more flexible front-end.

## Architecture at a glance
- **InferenceModel:** Wraps model loading + inference; returns a standard dict keyed by `DataKeys`.
- **DataSource:** Reads batches by run id, bucket, or train/val config.
- **Controller:** Orchestrates loading, running, and passing outputs to views.
- **Views:** Plotly-based renderers (with optional lightweight Gradio demo).

## Codebase map (where to look)
- **Existing visualizer (reference):** `wayve/ai/si/visualisation/bokeh/visualise.py`
- **Model loading paths:**
  - `pack_model.load_inference_model_from_session_id` (deployment wrapper)
  - `inference_model.load_ingested_model_from_session_id` (TorchScript)
- **Visualization wrapper:** `VisualisationModelWrapper`

## Why these decisions (the "because" part)
- **MVC split:** Keeps the inference logic testable and the UI replaceable.
- **Dash + Plotly:** Good balance between interactivity and maintainability for internal tools.
- **Reuse existing loaders:** We already have robust model-loading paths; no need to reinvent.

## Known gaps and risks
- **Plotter parity:** Parking vs InputOutput views may diverge; plan for a shared library of plot builders.
- **Export parity:** Offline HTML/MP4 export needs parity with the existing tool.
- **Config resolution:** Train/val config resolution is still an open design question.

## Lessons that generalize
- **Start by mapping the current system.** The fastest tool is the one that reuses the existing inference stack.
- **Standardize outputs.** A single `DataKeys`-based output contract keeps plots composable.
- **Separate UI from compute.** You can swap a UI later; swapping inference logic is painful.

## If you extend this project
- Decide the canonical data source interface (run id vs config vs bucket) and keep it stable.
- Add a small smoke test that loads a model and verifies a known output key (e.g., `POLICY_WAYPOINTS`).
- Keep the plotting code thin and reusable so new plots do not require controller changes.
