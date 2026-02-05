# Codex Change Log — WayveCode

## Table of Contents
- [2026-02](#2026-02)
- [2026-01](#2026-01)
- [2025-12](#2025-12)

## 2026-02
> [!note] 2026-02

> #### 2026-02-05 — Interleaved deploy wrapper
- Topic: route interleaving deploy wrapper + session-id resolution
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/si/`, `wayve/ai/zoo/deployment/`
- Changes:
  - [[2026/02/Week-1/2026-02-05-interleaved-deploy-wrapper]]: generated TorchScript-friendly route wrapper, updated deploy script to use it, added switching heuristics (latched near‑end‑of‑route, auto‑park, reverse gear, 5 mph hysteresis), wired parking nav inputs, defined end‑of‑route as no‑route for parking mode, disabled parking wrapper end‑of‑route triggering, and emitted `interleaved_id`/`interleaved_event` debug outputs.
> #### 2026-02-04 — Interleaving wrapper debug signals
- Topic: interleaving wrapper debug outputs + radar arg fix
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/zoo/deployment/`, `wayve/ai/si/`
- Changes:
  - [[2026/02/Week-1/2026-02-04-interleaving-wrapper-debug-signals]]: added interleaving debug outputs, split radar and baseline-input wrapper variants, and refreshed output keys.
> #### 2026-02-04 — Deploy interleaved run
- Topic: deploy interleaved for parking/baseline session
- Labels: #parking #deployment #interleaving #run
- Branch: current
- PR: none
- Change type: run
- Areas: `wayve/ai/si/`
- Changes:
  - [[2026/02/Week-1/2026-02-04-deploy-interleaved-run]]: ran `deploy_interleaved` to generate the interleaved TorchScript model under `/tmp/interleaved_sessions`.
> #### 2026-02-03 — Interleaving models project docs
> - Topic: interleaving baseline + parking/PUDA models
> - Labels: #parking #deployment #interleaving #docs
> - Branch: none
> - PR: none
> - Change type: docs
> - Areas: `codex/WayveCode/projects/`, `codex/WayveCode/how_to/`
> - Changes:
>   - [[2026/02/Week-1/2026-02-03-interleaving-models-project]]: added project deep dive, mermaid update, and new how-to chapter.

## 2026-01
#### 2026-01-25 — How-to project writeups
- Topic: project how-to writeups and index
- Labels: #docs #how-to #projects
- Branch: none
- PR: none
- Change type: docs
- Areas: `codex/WayveCode/how_to/`
- Changes:
  - [[2026/01/Week-4/2026-01-25-how-to-writeups]]: added how-to index and writeups for active/paused projects.

#### 2026-01-22 — Timestamp offset conversion (Zak branch)
- Topic: timestamp offset → timestamp_unixus
- Labels: #timestamp #data #zak
- Branch: none
- PR: none
- Change type: analysis
- Areas: `codex/WayveCode/2026/01/Week-4/`
- Changes:
  - [[2026/01/Week-4/2026-01-22-timestamp-offset-conversion]]: documented Zak-branch conversion logic and microsecond offset note.

#### 2026-01-21 — Parking route shortening
- Topic: parking route shortening
- Labels: #parking #otf #route-map
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/lib/data/pipes/`, `wayve/ai/zoo/data/`, `wayve/ai/si/datamodules/`, `wayve/ai/si/configs/parking/`, `codex/WayveCode/projects/`
- Changes:
  - [[2026/01/Week-4/2026-01-21-parking-route-shortening]]: truncate route polyline near parking entry before map generation.

#### 2026-01-21 — Parking OTF end-of-route blackout
- Topic: parking OTF augmentation
- Labels: #parking #otf #augmentation
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/data/`, `wayve/ai/si/datamodules/`, `wayve/ai/si/configs/parking/`, `codex/WayveCode/projects/`
- Changes:
  - [[2026/01/Week-4/2026-01-21-parking-otf-eor-blackout]]: added end-of-route blackout augmentation for parking frames.

#### 2026-01-21 — stopping_mode adaptor (Stage 1)
- Topic: stopping_mode input adaptor
- Labels: #parking #model #input #stopping_mode
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/st/`, `wayve/ai/zoo/data/`, `wayve/ai/si/configs/parking/`, `wayve/ai/si/models/`, `codex/WayveCode/projects/`
- Changes:
  - [[2026/01/Week-4/2026-01-21-stopping-mode-adaptor-stage1]]: implemented the new stopping_mode adaptor and wired it through configs/tests.

#### 2026-01-17 — WFM→BC→RL mermaid diagrams
- Topic: WFM/BC/RL architecture and losses
- Labels: #model #wfm #bc #rl #mermaid #analysis
- Branch: none
- PR: none
- Change type: analysis
- Areas: `wayve/ai/foundation/models/world_model/`, `wayve/ai/zoo/`, `wayve/ai/si/`, `codex/WayveCode/2026/01/Week-3/`
- Changes:
  - [[2026/01/Week-3/2026-01-17-wfm-bc-rl-mermaid-diagrams]]: added mermaid diagrams for WFM→BC→RL flow, layer reuse, losses, and WFM model comparison (Oct 0.5B vs 7B vs Dec 2025 vs YOLO), plus Excalidraw link.

#### 2026-01-13 — Parking hazard filter updates
- Topic: Parking maneuver hazard filter
- Labels: #parking #sampling #filters #tests
- Branch: boris/2025-12-30/zak-classifiers-parking-maneuver
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`
- Changes:
  - [[2026/01/Week-3/2026-01-13-parking-hazard-filter-updates]]: added hazard indicator light filter, cleaned gear in parking indices, and aligned default hazard masking.

#### 2026-01-13 — Inference model design (MVC)
- Topic: New inference visualization tool
- Labels: #viz #inference #design
- Branch: none
- PR: none
- Change type: docs
- Areas: `codex/WayveCode/projects/`
- Project: [[codex/WayveCode/projects/new-inference-vis-tool]]
- Changes:
  - [[2026/01/Week-3/2026-01-13-inference-model-design]]: documented InferenceModel plan and smoke test.

#### 2026-01-13 — New inference vis tool mapping
- Topic: New inference visualization tool
- Labels: #viz #inference #planning
- Branch: none
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/visualisation/`, `codex/WayveCode/projects/`
- Project: [[codex/WayveCode/projects/new-inference-vis-tool]]
- Changes:
  - [[2026/01/Week-3/2026-01-13-new-inference-vis-tool-initial-mapping]]: mapped current visualisation flow and proposed MVC reuse plan.

#### 2026-01-08 — Parking waypoints scatter plot
- Topic: Parking waypoint plot
- Labels: #parking #viz #bokeh
- Branch: boris/parking_fixed_reverse_acc
- PR: none
- Change type: update
- Areas: `wayve/ai/si/visualisation/bokeh/plotter/`, `wayve/ai/si/visualisation/bokeh/`, `codex/WayveCode/projects/`
- Changes:
  - [[2026/01/Week-2/2026-01-08-parking-waypoints-scatter-plot]]: added XY scatter plot for policy waypoints, live on-demand server mode with slider/timestamps/buttons, wrapped models with parking deployment wrapper, and paused the parking maneuver filter project.

#### 2026-01-06 — Parking WFM Update closed
- Topic: Parking WFM Update closure
- Labels: #parking #project
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `codex/WayveCode/projects/`
- Project: [[codex/WayveCode/projects/parking-wfm-update]]
- Changes:
  - Closed the project pending formal December WFM release and added re-creation checklist.

#### 2026-01-06 — Parking WFM December 2025 modes
- Topic: Parking WFM December 2025 modes
- Labels: #parking #model #config
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/si/config.py`, `wayve/ai/si/configs/parking/`
- Project: [[codex/WayveCode/projects/parking-wfm-update]]
- Changes:
  - [[2026/01/Week-1/2026-01-06-parking-wfm-december-2025-mode]]: added December 2025 WFM base and parking modes.

#### 2026-01-06 — Parking reverse constant-accel waypoints
- Topic: Parking reverse waypoint override
- Labels: #parking #deployment #inference
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/deployment/`
- Changes:
  - [[2026/01/Week-1/2026-01-06-parking-reverse-constant-accel-waypoints]]: override reverse-to-reverse waypoints with constant acceleration.

#### 2026-01-06 — Parking WFM October 2025 modes
- Topic: Parking WFM October 2025 modes
- Labels: #parking #model #config
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/si/configs/parking/`
- Project: [[codex/WayveCode/projects/parking-wfm-update]]
- Changes:
  - [[2026/01/Week-1/2026-01-06-parking-wfm-october-2025-mode]]: added October 2025 WFM parking configs and modes.

#### 2026-01-05 — Parking BC vs release BC latent actions
- Topic: Parking BC vs release BC
- Labels: #parking #model #latent-actions #analysis #mermaid
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/configs/parking/`, `wayve/ai/si/configs/baseline/`, `wayve/ai/zoo/outputs/`, `wayve/ai/latent_actions/models/`
- Changes:
  - [[2026/01/Week-1/2026-01-05-parking-bc-vs-release-bc-latent-actions]]: compare latent action pathways and add mermaid diagrams.

## 2025-12
#### 2025-12-30 — Parking maneuver filter (pred_park_type)
- Topic: Parking maneuver filter
- Labels: #parking #sampling #tests
- Branch: unknown
- PR: none
- Change type: docs/move
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`
- Changes:
  - [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]: moved task summary into the vault.

#### 2025-12-29 — Trace BC release model
- Topic: Release BC model trace
- Labels: #model #config #data
- Branch: unknown
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/`
- Changes:
  - Read configs and datamodule implementation for baseline BC release.
- Files:
  - /workspace/WayveCode/wayve/ai/si/configs/baseline/release.py
  - /workspace/WayveCode/wayve/ai/si/config.py
  - /workspace/WayveCode/wayve/ai/si/datamodules/otf.py

#### 2025-12-29 — Add release BC mermaid summary
- Topic: Model diagram
- Labels: #docs #mermaid #model
- Branch: unknown
- PR: none
- Change type: add
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: added task summary.

#### 2025-12-29 — Add ST transformer diagram
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended ST transformer components diagram.
