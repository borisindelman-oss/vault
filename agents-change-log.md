# Codex Change Log — WayveCode

## Table of Contents
- [2026-02](#2026-02)
- [2026-01](#2026-01)
- [2025-12](#2025-12)

## 2026-02
> [!note] 2026-02

> #### 2026-02-12 — PUDO train fix: OutputAdaptor behavior-control init
- Topic: fix `parking_bc_train_release_2026_5_4` startup failure in OutputAdaptor construction
- Labels: #parking #pudo #training #config #output-adaptor
- Branch: boris/train/pudo_11_02_26
- PR: none
- Change type: code
- Areas: `wayve/ai/si/configs/parking/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-12-pudo-train-output-adaptor-fix]]: investigated Datadog logs for `black-flamingo-fiery-125307`, fixed missing `latent_action_encoder` in `ParkingOutputAdaptorCfg` while keeping `enable_latent_action=False`, and validated with `bazel test //wayve/ai/si:test_config`.
> #### 2026-02-11 — PUDO hazard indicator enablement
- Topic: enable hazard as an indicator class in parking/PUDO model outputs
- Labels: #parking #pudo #indicator #losses #outputs #tests
- Branch: boris/train/pudo_11_02_26
- PR: none
- Change type: code
- Areas: `wayve/ai/si/configs/parking/`, `wayve/ai/zoo/outputs/`, `wayve/ai/zoo/losses/`, `wayve/ai/zoo/outputs/test/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-11-pudo-hazard-indicator-enable]]: set parking output adaptor indicator classes to 4 (hazard enabled), made indicator CE losses class-count aware in BC/KD paths, kept default non-parking behavior at 3 classes, and added output-head regression coverage.
> #### 2026-02-11 — PUDO parking wrapper parity (single wrapper)
- Topic: keep parking deployment in a single wrapper while adding driving-parity + end-of-route behavior
- Labels: #parking #pudo #deployment #wrapper #tests
- Branch: boris/train/pudo_11_02_26
- PR: none
- Change type: code
- Areas: `wayve/ai/zoo/deployment/`, `wayve/ai/si/models/`, `wayve/ai/si/test/`, `wayve/ai/si/configs/parking/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-11-pudo-parking-wrapper-parity]]: merged behavior-control/navigation/indicator support into `ParkingDeploymentWrapperImpl` (no new wrapper class), ported end-of-route parking trigger with `5.5e2` threshold (~5m), updated deployment selection logic and regression tests, hardened wrapper codegen default-arg handling, renamed parking train mode alias for release visibility, and enforced parking deployment defaults to behavior-control + navigation (rejecting explicit parking-only config).
> #### 2026-02-11 — PUDO bucket root and binary update
- Topic: align parking/PUDO data roots and binary with current migration plan
- Labels: #parking #pudo #datamodule #config
- Branch: boris/train/pudo_11_02_26
- PR: none
- Change type: code
- Areas: `wayve/ai/si/configs/parking/`, `projects/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-11-pudo-bucket-root-and-binary-update]]: set `materialised/si/parking/dev/2026_02_03_10_30_34_server_parking_pudo_buckets_bc` as root for legacy driving/PUDO/parking-validation buckets, kept `DS_26_01_06_SERVER_GEN2_IPACE` only for `dc_high_lateral_acceleration_uk`, `dc_high_lateral_acceleration_usa`, and `pre_ca_all_gen1`, bumped `binary_version` to `3.0.1`, and re-normalized driving scale to keep 93% driving target.
> #### 2026-02-11 — Vault structure reorg
- Topic: remove `codex/` and `WayveCode/` layers and normalize task/project layout
- Labels: #vault #structure #docs #migration
- Branch: none
- PR: none
- Change type: docs
- Areas: `~/.codex/AGENTS.md`, `~/.codex/skills/project-manager/SKILL.md`, `agent_tasks/`, `projects/`, `projects.md`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-11-vault-structure-reorg]]: flattened `vault/codex/WayveCode` into `vault/`, relocated date-based notes under `agent_tasks/YYYY/MM/Week-N/`, moved `newsletter_index.md` to vault top-level, updated instruction/skill path contracts, and rewrote vault links/paths to the top-level layout.
> #### 2026-02-10 — Model info finder script extraction in repo skill
- Topic: split inline skill commands into reusable shell scripts
- Labels: #skill #model-catalogue #refactor #docs
- Branch: skill/model-info-finder
- PR: none
- Change type: code
- Areas: `.ai/skills/model-info-finder/`, `agent_tasks/2026/02/Week-2/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-10-model-info-finder-skill-script-extraction]]: added helper + per-workflow `.sh` entrypoints, renamed helper to `model_catalogue_api_helpers.sh` for clearer discoverability, rewrote `SKILL.md` to use script calls instead of inlined command blocks, removed `MODEL_CATALOGUE_TOKEN` handling, and added explicit missing dependency prompts plus script-evolution guidance.
> #### 2026-02-09 — Model info finder skill cleanup
- Topic: simplify and harden model lookup skill commands
- Labels: #skill #model-catalogue #model-ci #refactor
- Branch: current
- PR: none
- Change type: code
- Areas: `~/.codex/skills/model-info-finder/`, `agent_tasks/2026/02/Week-2/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-09-model-info-finder-skill-cleanup]]: rewrote skill into helper-based workflows, reduced duplicated command blocks, added explicit no-match/ambiguous/no-build handling, and validated nickname->Model CI->Buildkite logs->Shadow Gym flow.
> #### 2026-02-09 — Model info finder: Model CI + Shadow Gym debug flow
- Topic: expand model lookup skill for build status and failure triage
- Labels: #skill #model-catalogue #model-ci #buildkite #shadow-gym
- Branch: current
- PR: none
- Change type: code
- Areas: `~/.codex/skills/model-info-finder/`, `agent_tasks/2026/02/Week-2/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-09-model-info-finder-modelci-shadowgym]]: added nickname/full-id model resolution, latest Model CI build summary, failed-job Buildkite log retrieval, Eval Studio execution-id check, and Shadow Gym execution/metadata lookup (with robust empty/non-array handling and zsh-safe job-id iteration).
> #### 2026-02-09 — How-to to newsletter migration
- Topic: vault docs migration from `how_to` chapters to newsletter issues
- Labels: #docs #vault #newsletter #migration
- Branch: none
- PR: none
- Change type: docs
- Areas: `newsletters/`, `agent_tasks/2026/02/Week-2/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-09-how-to-newsletter-migration]]: moved and renamed all `how_to` pages to `newsletter` pages, updated index and internal links, and removed the old `how_to` directory.
> #### 2026-02-08 — Interleaving production-docs refresh
- Topic: interleaving deployment docs aligned to intended production design
- Labels: #parking #deployment #interleaving #docs
- Branch: current
- PR: none
- Change type: docs
- Areas: `projects/`, `newsletters/`, `agent_tasks/2026/02/Week-2/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-08-interleaving-load-modes-and-switch-debug]]: updated project and newsletter docs to keep `zmurez/pudo` and `main interleaved_wrapper.py` reference notes, restored switching-flow mermaid diagrams, and focused content on intended production switching behavior (not temporary debug variants).
> #### 2026-02-08 — Interleaved compile vs Zak comparison
- Topic: route interleaving compile parity with `zmurez/pudo`
- Labels: #parking #deployment #interleaving #torchscript #debug
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/zoo/deployment/`, `wayve/ai/si/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-08-interleaved-compile-vs-zak]]: compared wrapper/compile flow with Zak’s `compile_with_baseline.py`, replaced `torch.jit.Attribute` routing state with plain Python attributes to match eager+script behavior, and validated deploy compile success with `__interleaved4_check2`.
> #### 2026-02-08 — Model info finder skill
- Topic: codex skill for model-catalogue lookup
- Labels: #skill #model-catalogue #cli #automation
- Branch: none
- PR: none
- Change type: code
- Areas: `~/.codex/skills/model-info-finder/`
- Changes:
  - [[agent_tasks/2026/02/Week-2/2026-02-08-model-info-finder-skill]]: created and simplified `model-info-finder` into a curl-only skill with nickname/author lookup, basic/deep flows, mandatory `console_url`, table-formatted summaries, `commit_id` extraction from `session_path/git.hash`, mandatory licensing fields (`license_count`, `licenses`) in deep summaries, and per-run console links (`run_url`) for checkpoint runs.
> #### 2026-02-05 — Interleaved deploy wrapper
- Topic: route interleaving deploy wrapper + session-id resolution
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/si/`, `wayve/ai/zoo/deployment/`
- Changes:
  - [[agent_tasks/2026/02/Week-1/2026-02-05-interleaved-deploy-wrapper]]: generated TorchScript-friendly route wrapper, updated deploy script to use it, added switching heuristics (latched near‑end‑of‑route, auto‑park, reverse gear, 5 mph hysteresis), wired parking nav inputs, defined end‑of‑route as no‑route for parking mode, disabled parking wrapper end‑of‑route triggering, emitted `interleaved_id`/`interleaved_event` debug outputs, and validated `_retrace13` output.
> #### 2026-02-05 — Route map signal thresholds
- Topic: route map signal thresholds + map span interpretation
- Labels: #route-map #docs #thresholds
- Branch: none
- PR: none
- Change type: docs
- Areas: `newsletters/`
- Changes:
  - [[agent_tasks/2026/02/Week-1/2026-02-05-route-map-signal-thresholds]]: added newsletter-style how-to explaining map span, route signal sums, and `5e4` threshold intuition; updated how-to index.
> #### 2026-02-05 — Bokeh visualise interleaving wrapper
- Topic: bokeh visualise uses route-interleaving wrapper
- Labels: #visualisation #interleaving #parking
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/si/visualisation/`
- Changes:
  - [[agent_tasks/2026/02/Week-1/2026-02-05-visualise-interleaving-wrapper]]: added baseline session support and route thresholds for interleaved visualisation, disabled parking end-of-route trigger, and ensured driving parameters/controls are supplied when missing.
> #### 2026-02-04 — Interleaving wrapper debug signals
- Topic: interleaving wrapper debug outputs + radar arg fix
- Labels: #parking #deployment #interleaving #torchscript
- Branch: current
- PR: none
- Change type: code
- Areas: `wayve/ai/zoo/deployment/`, `wayve/ai/si/`
- Changes:
  - [[agent_tasks/2026/02/Week-1/2026-02-04-interleaving-wrapper-debug-signals]]: added interleaving debug outputs, split radar and baseline-input wrapper variants, and refreshed output keys.
> #### 2026-02-04 — Deploy interleaved run
- Topic: deploy interleaved for parking/baseline session
- Labels: #parking #deployment #interleaving #run
- Branch: current
- PR: none
- Change type: run
- Areas: `wayve/ai/si/`
- Changes:
  - [[agent_tasks/2026/02/Week-1/2026-02-04-deploy-interleaved-run]]: ran `deploy_interleaved` to generate the interleaved TorchScript model under `/tmp/interleaved_sessions`.
> #### 2026-02-03 — Interleaving models project docs
> - Topic: interleaving baseline + parking/PUDA models
> - Labels: #parking #deployment #interleaving #docs
> - Branch: none
> - PR: none
> - Change type: docs
> - Areas: `projects/`, `newsletters/`
> - Changes:
>   - [[agent_tasks/2026/02/Week-1/2026-02-03-interleaving-models-project]]: added project deep dive, mermaid update, and new how-to chapter.

## 2026-01
#### 2026-01-25 — How-to project writeups
- Topic: project how-to writeups and index
- Labels: #docs #how-to #projects
- Branch: none
- PR: none
- Change type: docs
- Areas: `newsletters/`
- Changes:
  - [[agent_tasks/2026/01/Week-4/2026-01-25-how-to-writeups]]: added how-to index and writeups for active/paused projects.

#### 2026-01-22 — Timestamp offset conversion (Zak branch)
- Topic: timestamp offset → timestamp_unixus
- Labels: #timestamp #data #zak
- Branch: none
- PR: none
- Change type: analysis
- Areas: `agent_tasks/2026/01/Week-4/`
- Changes:
  - [[agent_tasks/2026/01/Week-4/2026-01-22-timestamp-offset-conversion]]: documented Zak-branch conversion logic and microsecond offset note.

#### 2026-01-21 — Parking route shortening
- Topic: parking route shortening
- Labels: #parking #otf #route-map
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/lib/data/pipes/`, `wayve/ai/zoo/data/`, `wayve/ai/si/datamodules/`, `wayve/ai/si/configs/parking/`, `projects/`
- Changes:
  - [[agent_tasks/2026/01/Week-4/2026-01-21-parking-route-shortening]]: truncate route polyline near parking entry before map generation.

#### 2026-01-21 — Parking OTF end-of-route blackout
- Topic: parking OTF augmentation
- Labels: #parking #otf #augmentation
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/data/`, `wayve/ai/si/datamodules/`, `wayve/ai/si/configs/parking/`, `projects/`
- Changes:
  - [[agent_tasks/2026/01/Week-4/2026-01-21-parking-otf-eor-blackout]]: added end-of-route blackout augmentation for parking frames.

#### 2026-01-21 — stopping_mode adaptor (Stage 1)
- Topic: stopping_mode input adaptor
- Labels: #parking #model #input #stopping_mode
- Branch: boris/stopping_mode
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/st/`, `wayve/ai/zoo/data/`, `wayve/ai/si/configs/parking/`, `wayve/ai/si/models/`, `projects/`
- Changes:
  - [[agent_tasks/2026/01/Week-4/2026-01-21-stopping-mode-adaptor-stage1]]: implemented the new stopping_mode adaptor and wired it through configs/tests.

#### 2026-01-17 — WFM→BC→RL mermaid diagrams
- Topic: WFM/BC/RL architecture and losses
- Labels: #model #wfm #bc #rl #mermaid #analysis
- Branch: none
- PR: none
- Change type: analysis
- Areas: `wayve/ai/foundation/models/world_model/`, `wayve/ai/zoo/`, `wayve/ai/si/`, `agent_tasks/2026/01/Week-3/`
- Changes:
  - [[agent_tasks/2026/01/Week-3/2026-01-17-wfm-bc-rl-mermaid-diagrams]]: added mermaid diagrams for WFM→BC→RL flow, layer reuse, losses, and WFM model comparison (Oct 0.5B vs 7B vs Dec 2025 vs YOLO), plus Excalidraw link.

#### 2026-01-13 — Parking hazard filter updates
- Topic: Parking maneuver hazard filter
- Labels: #parking #sampling #filters #tests
- Branch: boris/2025-12-30/zak-classifiers-parking-maneuver
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`
- Changes:
  - [[agent_tasks/2026/01/Week-3/2026-01-13-parking-hazard-filter-updates]]: added hazard indicator light filter, cleaned gear in parking indices, and aligned default hazard masking.

#### 2026-01-13 — Inference model design (MVC)
- Topic: New inference visualization tool
- Labels: #viz #inference #design
- Branch: none
- PR: none
- Change type: docs
- Areas: `projects/`
- Project: [[projects/new-inference-vis-tool]]
- Changes:
  - [[agent_tasks/2026/01/Week-3/2026-01-13-inference-model-design]]: documented InferenceModel plan and smoke test.

#### 2026-01-13 — New inference vis tool mapping
- Topic: New inference visualization tool
- Labels: #viz #inference #planning
- Branch: none
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/visualisation/`, `projects/`
- Project: [[projects/new-inference-vis-tool]]
- Changes:
  - [[agent_tasks/2026/01/Week-3/2026-01-13-new-inference-vis-tool-initial-mapping]]: mapped current visualisation flow and proposed MVC reuse plan.

#### 2026-01-08 — Parking waypoints scatter plot
- Topic: Parking waypoint plot
- Labels: #parking #viz #bokeh
- Branch: boris/parking_fixed_reverse_acc
- PR: none
- Change type: update
- Areas: `wayve/ai/si/visualisation/bokeh/plotter/`, `wayve/ai/si/visualisation/bokeh/`, `projects/`
- Changes:
  - [[agent_tasks/2026/01/Week-2/2026-01-08-parking-waypoints-scatter-plot]]: added XY scatter plot for policy waypoints, live on-demand server mode with slider/timestamps/buttons, wrapped models with parking deployment wrapper, and paused the parking maneuver filter project.

#### 2026-01-06 — Parking WFM Update closed
- Topic: Parking WFM Update closure
- Labels: #parking #project
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `projects/`
- Project: [[projects/parking-wfm-update]]
- Changes:
  - Closed the project pending formal December WFM release and added re-creation checklist.

#### 2026-01-06 — Parking WFM December 2025 modes
- Topic: Parking WFM December 2025 modes
- Labels: #parking #model #config
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/si/config.py`, `wayve/ai/si/configs/parking/`
- Project: [[projects/parking-wfm-update]]
- Changes:
  - [[agent_tasks/2026/01/Week-1/2026-01-06-parking-wfm-december-2025-mode]]: added December 2025 WFM base and parking modes.

#### 2026-01-06 — Parking reverse constant-accel waypoints
- Topic: Parking reverse waypoint override
- Labels: #parking #deployment #inference
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/zoo/deployment/`
- Changes:
  - [[agent_tasks/2026/01/Week-1/2026-01-06-parking-reverse-constant-accel-waypoints]]: override reverse-to-reverse waypoints with constant acceleration.

#### 2026-01-06 — Parking WFM October 2025 modes
- Topic: Parking WFM October 2025 modes
- Labels: #parking #model #config
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: update
- Areas: `wayve/ai/si/configs/parking/`
- Project: [[projects/parking-wfm-update]]
- Changes:
  - [[agent_tasks/2026/01/Week-1/2026-01-06-parking-wfm-october-2025-mode]]: added October 2025 WFM parking configs and modes.

#### 2026-01-05 — Parking BC vs release BC latent actions
- Topic: Parking BC vs release BC
- Labels: #parking #model #latent-actions #analysis #mermaid
- Branch: soham/12-18-Parking-model
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/configs/parking/`, `wayve/ai/si/configs/baseline/`, `wayve/ai/zoo/outputs/`, `wayve/ai/latent_actions/models/`
- Changes:
  - [[agent_tasks/2026/01/Week-1/2026-01-05-parking-bc-vs-release-bc-latent-actions]]: compare latent action pathways and add mermaid diagrams.

## 2025-12
#### 2025-12-30 — Parking maneuver filter (pred_park_type)
- Topic: Parking maneuver filter
- Labels: #parking #sampling #tests
- Branch: unknown
- PR: none
- Change type: docs/move
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`
- Changes:
  - [[agent_tasks/2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]: moved task summary into the vault.

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
- Areas: `agent_tasks/2025/12/Week-5/`
- Changes:
  - [[agent_tasks/2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: added task summary.

#### 2025-12-29 — Add ST transformer diagram
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: `agent_tasks/2025/12/Week-5/`
- Changes:
  - [[agent_tasks/2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended ST transformer components diagram.
