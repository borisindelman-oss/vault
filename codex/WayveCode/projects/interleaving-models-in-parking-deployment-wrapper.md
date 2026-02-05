# Interleaving models in parking deployment wrapper

## Overview
- **What it is:** Build a single deployable model that interleaves baseline driving and parking/PUDA models inside a new wrapper.
- **Why it matters:** On‑vehicle inference should see a standard model session ID, while we switch between two models internally.
- **Primary users:** Not specified yet.

## Status
- **Phase:** Phase 2
- **Status:** active
- **Last updated:** 2026-02-05
- **Current priorities:**
  - Validate upload path and DMI config generation for the interleaved wrapper.
  - Decide final output directory strategy (`/mnt/remote` vs workspace output).
  - Add regression checks for input/output key mismatches.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Use two already‑compiled TorchScript models (baseline + parking/PUDA) and ship a single deployable model that switches internally based on parking mode / route heuristics.
- **Target users:** Not specified yet.
- **Integrations:** Parking deployment wrapper; session‑ID loaded models; deploy upload pipeline.
- **Constraints:**
  - Session IDs load TorchScript artifacts; interleaving must produce a new TorchScript artifact.
  - Both models must share an identical deployment interface.
- **Success criteria:** A new session ID uploads successfully and behaves like a standard model, while switching internally.

## Design
- **Approach:**
  - Build a route‑interleaving wrapper with a fixed, static signature for the baseline + parking pair.
  - Package baseline + parking TorchScript models into a single artifact and save via `save_compiled_model`.
  - Use unioned deployment config (inputs + outputs), with optional outputs filled via none tokens.
- **Key decisions:**
  - Use wrapper‑level interleaving (no `interleave_control`).
  - Load both models from session IDs externally, then pass them into the wrapper.
  - Infer primary wrapper input keys from `model.forward` to avoid missing nav‑instruction inputs.
- **Open questions:**
  - Exact switch predicate: parking mode only vs parking mode OR end‑of‑route.
  - How strict to be on deployment_config mismatches.

## Build Phases
- **Phase:** Phase 1
  - **Goal:** Wrapper‑level interleaving with a deployable combined model.
  - **Work items:** Implement wrapper + packer + config checks.
  - **Validation:** Smoke test compile + run.
- **Phase:** Phase 2
  - **Goal:** Harden deploy path for session IDs and production packaging.
  - **Work items:** Upload validation, strict input/output matching, add regression guardrails.
  - **Validation:** Successful upload + DMI config generation without manual fixes.

## Decisions
- **2026-02-03:**
  - **Decision:** Use wrapper‑level interleaving and package as a single TorchScript artifact.
  - **Rationale:** Vehicle/sim expect a standard model session; session IDs are TorchScript.
- **2026-02-03:**
  - **Decision:** Do not use `interleave_control` or InterleavedModelRunner for this path.
  - **Rationale:** We are interleaving inside the wrapper and shipping a single model artifact.
- **2026-02-05:**
  - **Decision:** Generate a wrapper with unioned output keys and optional fields filled using none tokens.
  - **Rationale:** Baseline and parking outputs differ; TorchScript requires a stable output schema.
- **2026-02-05:**
  - **Decision:** Replace codegen with a static wrapper class tied to the baseline + parking signatures.
  - **Rationale:** We only need one model pair; static code is simpler and easier to reason about.
- **2026-02-05:**
  - **Decision:** Infer primary wrapper input keys from `model.forward`.
  - **Rationale:** Deployment config input keys can omit nav‑instruction args required by the wrapper.
- **2026-02-05:**
  - **Decision:** Fallback to ingested model when session config is unreadable on `/mnt/remote`.
  - **Rationale:** Config YAML can be missing or blocked by storage permissions; we still need a deploy path.

## Notes
- Working deploy runs:
  - `DEV_VM=0 TMPDIR=/workspace/tmp bazel run //wayve/ai/si:deploy_interleaved_models -- --baseline_model_session_id session_2026_01_15_13_16_36_si_candidate_2026_5_3_baseline_rl_with_refreshed_data_with_aac --session_id session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix _retrace2 --dilc_on --enable_parking --with_temporal_caching true`
  - Output: `/mnt/remote/azure_session_dir/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc_retrace2/traces/model-000100000.torchscript`

### Findings: how `zmurez/pudo` implements interleaving (reference)
- Interleaving is done in C++ via `InterleavedModelRunner` with transition events and warmup.
- Policy selection:
  - `interleave_control` output → `ModelControlledSwitchPolicy` (falling‑edge switch).
  - Otherwise → `TimeBasedRandomSwitchPolicy`.
- Switching happens in `InterleavedModelRunner::createForwardPass()` and finalizes in `completeTransition()`.
- Runner initialization lives in `createModelRunner()`; runner indices are based on `model_configs` ordering.
- `InterleaveControl` is wired end‑to‑end (proto → DMI output handler → ROS publication).
- Parking wrapper in that branch emits `interleave_control = ~parking` using heuristics.
- Deployment ops note (per Naman Rawal, lead for this area): interleaving is standard for TRT models via a 2‑model experiment; Torchscript SW interleaving isn’t supported in console today.

### Findings: interleaving wrapper on main (Torch)
- `wayve/ai/zoo/deployment/interleaved_wrapper.py` defines `InterleavedModelWrapper` + `InterleavedDrivingOutput`.
- Outputs include:
  - `interleaved_id` → current model index.
  - `interleaved_event` → swap flag (1 on swap, 0 otherwise).
- These are **debug/telemetry outputs**, not switch triggers.
  - Torch interleaved testing parses them from debug tensors to reconstruct model episodes.
  - In contrast, TRT interleaving publishes **`InterleavedEvent` proto messages** (`SWITCH_START`, `MODEL_ACTIVE_WARMUP`, `SWITCH_FINISH_CACHE_WARMED`) from C++.
- Actionable for this project: we should emit `interleaved_id`/`interleaved_event` for logging visibility, but switching stays inside the wrapper.

### Plan: wrapper‑level interleaving (our implementation)

#### 1) New interleaving wrapper
- Add `InterleavingDeploymentWrapperImpl` in `wayve/ai/zoo/deployment/deployment_wrapper.py`.
- It holds two sub‑wrappers:
  - Baseline: `DeploymentWrapperImpl`
  - Parking: `ParkingDeploymentWrapperImpl`
- Forward signature = union of inputs (parking needs gear position + driving_controls).
- Switch predicate: `parking_mode` and/or end‑of‑route heuristic (TBD).
- Output: `OnBoardDrivingOutput` (parking output already includes `policy_gear_position`).
- Optional: include `interleaved_id` + `interleaved_event` for debug logging (swap visibility).

#### 2) Model provisioning (session IDs → one artifact)
- Load baseline + parking **TorchScript** models via `load_ingested_model(session_id)`.
- Validate both deployment configs are compatible (input/output keys, frames, radar, etc.).
- Pass both ScriptModules into `InterleavingDeploymentWrapperImpl`.
- Compile to a **single TorchScript artifact** (new session ID).

#### 3) Deploy‑like packaging + upload
- Add a new script (or extend packer) that mirrors deploy’s upload flow:
  - Inputs: `--baseline_session_id`, `--parking_session_id`, `--output_dir`, `--suffix`, `--upload`.
  - Uses `compile_and_save_model(...)` + `upload_compiled_model(...)` so it appears as a standard model.
- Ensure we pass deploy‑time wrapper options consistently:
  - `deployment_country`, `deployment_vehicle_model_override`, `dilc_on`, `deployment_driving_controls_keys`, `enable_radar_input`.
- Temporal caching: must already match in the compiled session IDs (cannot be toggled post‑compile).

```mermaid
flowchart TD
    A[Baseline Session ID] --> B[Load TorchScript]
    C[Parking/PUDA Session ID] --> D[Load TorchScript]
    B --> E[InterleavingDeploymentWrapperImpl]
    D --> E
    E --> F[Compile to Single TorchScript]
    F --> G[Upload as New Session ID]
    G --> H[Vehicle Inference Uses Standard Session]
```

```mermaid
flowchart TD
    A["ParkingWrapper - Python"] -->|interleave_control| B["InterleavedModelRunner"]
    B --> C{InterleavePolicy}
    C -->|ModelControlledSwitchPolicy| D["Runner selection"]
    C -->|TimeBasedRandomSwitchPolicy| D
    D --> E["InterleavingForwardPass"]
    E --> F["Driving plan + InterleavedEvent"]
    E --> G["InterleaveControl output"]
    F --> H["InferenceNode outputs"]
    G --> H
    style A fill:#FFE8CC,stroke:#CC8B00,color:#000
```
