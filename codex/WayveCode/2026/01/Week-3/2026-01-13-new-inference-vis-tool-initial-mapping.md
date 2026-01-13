# New inference vis tool: initial mapping

## Summary
- Read existing SI visualisation flows (Bokeh server, offline scripts, model wrapper, datapipe selection).
- Mapped how model + deployment wrapper + data sources are wired today.
- Proposed reuse plan and MVC structure for the new tool.

## Current solution map
- Entry point: `wayve/ai/si/visualisation/bokeh/visualise.py` orchestrates args, model loading, datapipe, plotter, and server/HTML/MP4 output.
- Model wrapper: `wayve/ai/si/visualisation/inference_model.py` (VisualisationModelWrapper + ModelBuffer) handles casting, camera mapping, deployment wrapper call path, and unbatching outputs.
- Data sources: `wayve/ai/si/visualisation/run_segment_picker.py` parses segments from JSON/YAML/dataset/CLI and builds datapipes via `make_driving_datapipe_for_run_id`.
- Packaging: `wayve/ai/si/visualisation/pack_model.py` creates torch packages from session IDs for inference usage.
- Plotting: `wayve/ai/si/visualisation/bokeh/plotter/*` defines InputPlotter/InputOutputPlotter/ParkingPlotter and required input/output keys.
- Offline renderer: `wayve/ai/si/visualisation/scripts/visualise.py` uses Ray + visualisation.lib for MP4 generation.

## Reuse plan (MVC)
- Model: create an `InferenceModel` wrapper using `ModelBuffer` + `VisualisationModelWrapper` with factories for session/package/ckpt/torchscript.
- Controller: `InferenceController` that binds `DataSource` + `InferenceModel`, caches frames, and exposes `get_frame(idx)`.
- View: Plotly-based views for camera panels, BEV, speed/curvature, indicator/gear, and map; use existing key lists to define required inputs/outputs.
- DataSource: adapter around `segment_picker` + `get_datapipe` to support run id, bucket, and train/val config selection.

## Suggested direction
- Prefer Dash + Plotly for MVC alignment and multi-pane state synchronization.
- Keep Gradio as a fast-prototype fallback if needed.

## Gradio + Plotly vs Dash + Plotly
**Fit for MVC**
- Dash: Strong. Clear separation of layout (View) and callbacks (Controller) with reusable model layer.
- Gradio: OK for single-flow apps, but MVC separation gets blurry with chained event handlers.

**State + caching**
- Dash: Server-side caching patterns (memoization, background callbacks) are well established; easier to coordinate multi-view state.
- Gradio: Simpler state primitives; workable but more friction for complex shared state.

**Multi-pane layouts**
- Dash: Built for dashboard grids and coordinated plots.
- Gradio: Layouts are fine for moderate complexity, harder to manage dense multi-panel visualizations.

**Performance + data volume**
- Dash: Better control over update granularity; easier to optimize per-component updates.
- Gradio: Great for demos, but large per-frame payloads can feel sluggish without more custom work.

**Developer speed**
- Gradio: Fastest to prototype and iterate UI.
- Dash: More boilerplate, but scales better once complexity grows.

**Recommendation**
- Use Dash + Plotly for the main tool (MVC alignment + multi-view sync).
- Optionally build a lightweight Gradio demo that reuses the Plotly view builders for quick internal sharing.

## Diagrams
### MVC components
```mermaid
flowchart LR
  subgraph Model
    IM[InferenceModel]
    MB[ModelBuffer]
    VMW[VisualisationModelWrapper]
    DW[Deployment Wrapper]
  end

  subgraph Controller
    IC[InferenceController]
    FC[Frame Cache]
    PF[Prefetch/Throttle]
  end

  subgraph View
    UI[Dash App]
    VP[Plotly Views]
  end

  subgraph Data
    DS[DataSource]
    SP[segment_picker]
    DP[get_datapipe]
  end

  MB --> VMW --> IM
  DW --> VMW
  DS --> IC
  SP --> DS
  DP --> DS
  IM --> IC
  IC --> UI --> VP
```

### Data and inference flow
```mermaid
sequenceDiagram
  participant U as User
  participant UI as Dash UI
  participant IC as InferenceController
  participant DS as DataSource
  participant IM as InferenceModel
  participant VMW as VisualisationModelWrapper

  U->>UI: Select run/bucket/config + model source
  UI->>IC: load_model(params)
  IC->>IM: from_session_id/from_package/from_ckpt
  IM->>VMW: initialize wrapper

  U->>UI: Scrub frame index
  UI->>IC: get_frame(i)
  IC->>DS: fetch inputs for frame i
  DS-->>IC: inputs
  IC->>IM: infer(inputs)
  IM->>VMW: forward (deployment wrapper path)
  VMW-->>IM: outputs
  IM-->>IC: outputs
  IC-->>UI: inputs + outputs
  UI-->>U: Plotly update
```

## Open questions
- Which plotter types need parity (InputOutput vs Parking)?
- Should the tool support offline HTML/MP4 export like current flows?
- How should train/val config resolve to dataset paths in the UI?
