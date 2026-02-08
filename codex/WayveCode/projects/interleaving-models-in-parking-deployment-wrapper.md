# Interleaving models in parking deployment wrapper

## Overview
- **What it is:** A single deployable interleaving model that runs baseline driving or parking wrapper outputs behind one deployment wrapper interface.
- **Why it matters:** Vehicle/sim consume one session ID, while model selection happens inside the wrapper.
- **Primary users:** Parking + deployment validation workflows (sim/HIL/model CI).

## Status
- **Phase:** Phase 2
- **Status:** active
- **Last updated:** 2026-02-08
- **Current priorities:**
  - Confirm switching-path stability in HIL (both trigger-based and periodic switch test mode).
  - Keep deploy flow parity with `deploy.py` argument/init behavior.
  - Track and resolve runtime failures related to flash-attention path on switch.
- **Blockers:**
  - HIL still failing in some switch-path variants (`This Python function is annotated to be ignored and cannot be run` from perceiver flash-attention path).

## Requirements
- **Problem statement:** Build one model artifact that can switch between baseline driving and parking behavior while preserving deploy-time compatibility.
- **Target users:** Deployment engineers validating model behavior in sim/HIL.
- **Integrations:** `deploy_interleaved_models.py`, `RouteInterleavingWrapperImpl`, model ingest/upload path, model CI.
- **Constraints:**
  - Keep stable output schema for TorchScript.
  - Keep wrapper interface compatible with existing deploy/runtime expectations.
  - Preserve nav/gear/control input handling across both branches.
- **Success criteria:**
  - Upload succeeds and session is runnable by validation tools.
  - No crash when branch switches.
  - Debug telemetry (`interleaved_id`, `interleaved_event`) shows expected transitions.

## Design
- **Approach:**
  - `RouteInterleavingWrapperImpl` inherits `DeploymentWrapperBase` and implements `_forward_with_additional_inputs(...)`.
  - `make_wrapper_class(...)` generates the public `forward(...)` signature.
  - Wrapper decides model branch, calls chosen sub-wrapper, and emits a fixed `RouteInterleavingOutput`.
- **Model load modes (current decision):**
  - `--primary_model_load_mode`: `wrapper|ingested`
  - `--baseline_model_load_mode`: `wrapper|ingested`
  - `torchscript` mode removed for symmetry and simpler behavior.
- **Switching modes:**
  - Normal: heuristic-based decision (`near_end` latch, initiate auto-park, reverse gear, speed hysteresis).
  - Debug: `--switch_every_n_forwards N` forces periodic branch toggles.
- **Cache warmup:**
  - `--num_cache_warmup_frames` controls how many frames return cached output after switch.
  - `0` disables cached warmup output reuse.
- **Debug outputs:**
  - `interleaved_id`: active branch (`0` baseline, `1` parking).
  - `interleaved_event`: `1` on switch frame, else `0`.

## Build Phases
- **Phase:** Phase 1
  - **Goal:** First deployable interleaving wrapper and successful compile/upload.
  - **Validation:** TorchScript compiles, deploy output generated.
- **Phase:** Phase 2
  - **Goal:** Runtime robustness during branch switching in model CI/HIL.
  - **Validation:** Forward-pass stability for switching scenarios.

## Decisions
- **2026-02-05:**
  - **Decision:** Use wrapper-level interleaving and ship as one model artifact.
  - **Rationale:** Keep runtime integration identical to single-session deploy model consumption.
- **2026-02-05:**
  - **Decision:** Emit `interleaved_id` and `interleaved_event`.
  - **Rationale:** Provide direct observability of branch state and transitions.
- **2026-02-08:**
  - **Decision:** Standardize both model load modes to `wrapper|ingested`.
  - **Rationale:** Remove asymmetric behavior and keep both model paths configurable in the same way.
- **2026-02-08:**
  - **Decision:** Keep periodic switch mode and cache warmup controls as first-class CLI options.
  - **Rationale:** Needed for deterministic switch testing and switch-path debugging in HIL.

## Notes
- Notable upload variants used in validation:
  - `__interleaved6`: known good reference for current branch behavior.
  - `interleaved_every_30`: periodic switching variant (exposed switch-path runtime failure in HIL).
  - `__interleaved_every_30_2`: follow-up periodic switching variant under test.
  - `interleaving_30_no_cache`: periodic switching with `num_cache_warmup_frames=0`.
- Console link (latest no-cache periodic upload):
  - `https://console.sso.wayve.ai/model/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bcinterleaving_30_no_cache`
