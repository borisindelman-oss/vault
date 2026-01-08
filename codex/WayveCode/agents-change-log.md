# Codex Change Log — WayveCode

## Table of Contents
- [2026-01](#2026-01)
- [2025-12](#2025-12)

## 2026-01
#### 2026-01-08 — Parking waypoints scatter plot
- Topic: Parking waypoint plot
- Labels: #parking #viz #bokeh
- Branch: boris/parking_fixed_reverse_acc
- PR: none
- Change type: update
- Areas: `wayve/ai/si/visualisation/bokeh/plotter/`, `wayve/ai/si/visualisation/bokeh/`, `codex/WayveCode/projects/`
- Changes:
  - [[2026/01/Week-2/2026-01-08-parking-waypoints-scatter-plot]]: added XY scatter plot for policy waypoints, server mode for visualiser, and paused the parking maneuver filter project.

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
