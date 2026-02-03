# Interleaving models in parking deployment wrapper

## Overview
- **What it is:** Extend the parking deployment wrapper to interleave between the baseline driving model and the parking/PUDA model based on heuristics (e.g., end-of-route).
- **Why it matters:** Enables correct model switching for parking scenarios on-vehicle, meeting new deployment needs.
- **Primary users:** Not specified yet.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-02-03
- **Current priorities:**
  - Review Zach's branch `zmurez/pudo` for existing changes.
  - Identify required wrapper changes to support model interleaving.
  - Define switching heuristics and the model-selection interface.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Run two models on-vehicle (baseline driving + parking/PUDA) and switch to parking/PUDA when heuristics like end-of-route trigger. Extend the parking deployment wrapper to support this.
- **Target users:** Not specified yet.
- **Integrations:** Parking deployment wrapper; reference branch `zmurez/pudo`.
- **Constraints:** TBD.
- **Success criteria:** Demonstrate interleaving between baseline and parking/PUDA models in the deployment wrapper.

## Design
- **Approach:** Extend the parking deployment wrapper to support model interleaving; start from `zmurez/pudo` and adapt as needed.
- **Key decisions:** TBD.
- **Open questions:** Testing strategy; exact heuristics; rollout/validation gates.

## Build Phases
- **Phase:** Phase 1
  - **Goal:** Implement initial interleaving support in the wrapper.
  - **Work items:** Review `zmurez/pudo`, map wrapper flow, add switching hook, define config/heuristics (TBD).
  - **Validation:** Demonstrate model switching in a test environment (details TBD).

## Decisions
- **2026-02-03:**
  - **Decision:** Start from Zach's `zmurez/pudo` branch as the baseline reference.
  - **Rationale:** It already targets the parking/PUDA deployment path.

## Notes
- Testing plan not defined yet.

### Summary: `zmurez/pudo` interleaving implementation
- Adds an interleaved model runner backend that manages multiple model runners, warmup, and transition events.
- Interleaving policy selection:
  - If model outputs include `interleave_control`, the runner uses a `ModelControlledSwitchPolicy` (falling-edge switch semantics).
  - Otherwise, it falls back to a `TimeBasedRandomSwitchPolicy`.
- Switching happens in `InterleavedModelRunner::createForwardPass()`:
  - Calls `policy_->next()` when `transition_state_ == IDLE`.
  - Sets `primary_runner_` (old), `secondary_runner_` (new), and initializes the transition state.
  - Alternates runners during transition and finalizes in `completeTransition()`.
- Runner initialization and model selection live in `createModelRunner()`:
  - `model_configs` (vector of `ModelDeploymentConfig`) define the runners and their indices.
  - Each config becomes a `RunnerProfile` with `runner` + `artefact_id`.
- Transition lifecycle is explicit (events): `SWITCH_START` → `MODEL_ACTIVE_WARMUP` → `SWITCH_FINISH_CACHE_WARMED`.
  - Secondary runner publishes events; driving plan is suppressed during warmup/transition except at `SWITCH_FINISH`.
  - Only the primary runner updates the interleave policy during transitions to avoid oscillation.
- `InterleaveControl` is threaded end-to-end:
  - New proto `InterleaveControl` + DMI output handler + ROS publication on `robot/inference/interleave_control`.
  - `ForwardPassResult` carries `interleave_control`, which feeds the model-controlled policy.
- Parking deployment wrapper changes:
  - New `ParkingWrapper` creates a `ParkingOutput` that includes `interleave_control`.
  - The wrapper sets `interleave_control = ~parking` using heuristics: end-of-route, parking pose present, non-drive gear, or auto-parking control.
  - In `wayve/ai/si/models/deployment.py`, the wrapper is hard-swapped to `ParkingWrapper` (commented out `make_wrapper_class`).

```mermaid
flowchart TD
    A[ParkingWrapper (Python)] -->|interleave_control bool| B[InterleavedModelRunner]
    B --> C{InterleavePolicy}
    C -->|ModelControlledSwitchPolicy (falling-edge switch)| D[Runner selection]
    C -->|TimeBasedRandomSwitchPolicy| D
    D --> E[InterleavingForwardPass]
    E --> F[Driving plan + InterleavedEvent]
    E --> G[InterleaveControl output]
    F --> H[InferenceNode outputs]
    G --> H
    style A fill:#FFE8CC,stroke:#CC8B00,color:#000
```
