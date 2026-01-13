# New Inference Vis Tool

## Overview
- **What it is:** MVC-based visualization tool to run end-to-end model inference with interactive plots.
- **Why it matters:** Provides consistent, flexible visualization for model behavior across datasets and configs.
- **Primary users:** ML researchers and engineers.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-01-13
- **Current priorities:**
  - Review existing `bokeh/visualise.py` under `wayve/ai/si` (data/model usage).
  - Map data source inputs (run id, bucket, train/val config) and model execution path (deployment wrapper + TorchScript).
  - Draft initial architecture and framework recommendation (Gradio+Plotly vs Dash+Plotly).
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Build a new visualization tool for end-to-end model inference with flexible data sources and MVC structure.
- **Target users:** Internal model developers and researchers.
- **Integrations:** Deployment wrapper; TorchScript model; data sources via run id, bucket, train/val configs.
- **Constraints:** MVC architecture; evaluate Gradio+Plotly vs Dash+Plotly; reuse/learn from existing `visualise.py`.
- **Success criteria:** Tool can run the model end-to-end, swap data sources, and produce interactive visualizations usable by engineers.

## Design
- **Approach:** MVC split (InferenceModel + DataSource + InferenceController + Plotly views), reuse existing model wrapper/datapipe/plotter keys.
- **Key decisions:** Prefer Dash + Plotly for the main tool; optionally add a lightweight Gradio demo reusing Plotly view builders.
- **Open questions:** Plotter parity (InputOutput vs Parking), offline HTML/MP4 export parity, and train/val config resolution strategy.

## Build Phases
- **Phase:**
  - **Goal:**
  - **Work items:**
  - **Validation:**

## Decisions
- **2026-01-12:**
  - **Decision:**
  - **Rationale:**

## Notes
- [[2026/01/Week-3/2026-01-13-new-inference-vis-tool-initial-mapping]]
