# Waypoint clamping in deployment wrapper

## Overview
- **What it is:** Move default waypoint clamping from `waypoints_heads.py` into deployment wrappers (non-parking).
- **Why it matters:** Centralizes postprocessing so parking gear-based clamp can override; avoids incorrect clamping when predicted gear is available.
- **Primary users:** Deployment wrappers for non-parking driving models.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-02-01
- **Current priorities:**
  - Verify tests and downstream behavior
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Default waypoint clamping currently lives in `waypoints_heads.py`, which can’t access predicted gear; clamping should be performed in deployment wrappers with parking overriding.
- **Target users:** Deployment outputs for non-parking wrappers.
- **Integrations:** `wayve/ai/zoo/deployment/deployment_wrapper.py`, `wayve/ai/zoo/outputs/waypoints_heads.py`.
- **Constraints:** Parking wrapper keeps its own gear-based clamp; no double-clamping.
- **Success criteria:** Default clamp applied in deployment wrappers, parking override preserved, head clamp removed.

## Design
- **Approach:** Add a shared clamp helper in deployment wrapper base and call it in non-parking wrappers before converting outputs.
- **Key decisions:** Skip gear-direction check per user request.
- **Open questions:**
  - None

## Build Phases
- **Phase:** Phase 1
  - **Goal:** Implement shared clamp in deployment wrappers.
  - **Work items:**
    - Add helper to deployment wrapper base
    - Apply helper to non-parking wrappers
    - Remove head clamp
    - Add/adjust tests if needed
  - **Validation:** Tests pass; parking behavior unchanged.

## Decisions
- **2026-02-01:**
  - **Decision:** Keep clamp centralized in deployment wrapper base and skip gear-direction check.
  - **Rationale:** Parking has dedicated clamp; default clamp should not be in head.
- **2026-02-01:**
  - **Decision:** Name helper `_clamp_waypoints_for_direction`.
  - **Rationale:** Covers both gear-based and default clamp behavior.

## Notes
- Discovery details skipped at user request.
- Implemented shared clamp in deployment wrappers; removed head clamp.
