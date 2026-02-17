# Parking stopping_mode naive heuristic

## Overview
- **What it is:** A small, flag-gated stopping_mode path for parking, scoped as a subset of [[projects/parking-stopping-mode-dilc]].
- **Why it matters:** We need park vs PUDO conditioning for training without bringing back the full DILC/wrapper project scope.
- **Primary users:** Parking model training owners and data-pipeline maintainers.

## Status
- **Phase:** Phase 3
- **Status:** active
- **Last updated:** 2026-02-17
- **Branch:** 02-12-park-pudo-stopping-mode-heuristic
- **PR:** #96911
- **Current priorities:**
  - Keep this PR stack minimal and clean on top of `02-11-parking_mode_heuristic`.
  - Keep behavior strictly default-off unless explicit flags are enabled.
  - Document exact heuristic semantics and enum values for reviewers.
- **Blockers:**
  - None.

## Requirements
- **Problem statement:** Add a lightweight stopping_mode signal for parking with deterministic heuristic behavior and no behavior change unless enabled.
- **Target users:** Parking BC training owners.
- **Integrations:**
  - `wayve/ai/zoo/data/parking.py`
  - `wayve/ai/zoo/data/keys.py`
  - `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
  - `wayve/ai/zoo/st/models.py`
  - `wayve/ai/zoo/st/checkpoints.py`
- **Constraints:**
  - Flags default to off.
  - Relative to `02-11-parking_mode_heuristic`, this branch only adds stopping-mode pieces and hazard-based assignment in parking data; no extra OTF churn.
  - Keep the logic intentionally simple (naive), not label-perfect.
- **Success criteria:**
  - `DataKeys.STOPPING_MODE` is available end-to-end when enabled.
  - `stopping_mode` adaptor can be enabled in ST model config, default remains disabled.
  - Heuristic matches requested behavior exactly.

### Exact stopping_mode assignment (current logic)
- Preconditions:
  - `enable_naive_stopping_mode=True`.
  - `additional_parking_gear_direction` and `additional_parking_vehicle_speed` exist.
  - `additional_parking_indicator_light` exists (otherwise raise `KeyError`).
- Rule 1: If `parking_mode=False` at origin, set stopping_mode randomly to `{0, 1}`.
- Rule 2: If `parking_mode=True` and hazard appears in `additional_parking_indicator_light`, set stopping_mode to `0` (PUDO).
- Rule 3: If `parking_mode=True` and hazard is not present, set stopping_mode to `1` (PARK).
- Rule 4: If `enable_naive_stopping_mode=False`, do not write `DataKeys.STOPPING_MODE`.

## Design
- **Approach:**
  - Reuse minimal adaptor wiring from `boris/stopping_mode`.
  - Compute parking_mode first from gear/speed lookahead, then derive stopping_mode from parking_mode + indicator lookahead.
  - Keep indicator handling robust by using canonical mapping (`INDICATOR_STATE_MAPPING[VehicleIndicator.HAZARD.value]`) instead of hardcoded literal values.
- **Why this is naive:**
  - It is heuristic-based, not based on ground-truth stop intent labels.
  - It uses random assignment when parking mode is not active.
- **Enum values (this project):**
  - `PUDO = 0`
  - `PARK = 1`

## Build Phases
- **Phase 1: Extract minimal reusable pieces from `boris/stopping_mode`**
  - **Goal:** Identify exact files/lines to port with minimum scope.
  - **Status:** Completed (2026-02-12).

- **Phase 2: Add stopping_mode adaptor with flag-off defaults**
  - **Goal:** Add model-side support safely.
  - **Status:** Completed (2026-02-12).

- **Phase 3: Parking heuristic wiring for stopping_mode**
  - **Goal:** Set stopping_mode from parking window + hazard rule.
  - **Status:** Completed (2026-02-17).
  - **Validation:** Parking+ST tests for missing-indicator guard, random fallback, park/pudo branches, adaptor coverage.

- **Phase 4: Rollout guardrails and stacked-PR hygiene**
  - **Goal:** Keep diffs clean relative to `02-11-parking_mode_heuristic` and preserve default-off behavior.
  - **Status:** In progress.

## Decisions
- **2026-02-12:** Keep all new behavior behind explicit flags defaulting to off.
- **2026-02-17:** Use stopping_mode enum values `0=pudo`, `1=park` to match the expected project convention.
- **2026-02-17:** Detect hazard via `INDICATOR_STATE_MAPPING[VehicleIndicator.HAZARD.value]` rather than hardcoded numeric literals.
- **2026-02-17:** Apply hazard only when `parking_mode=True`; otherwise keep random branch.

## Notes
- Reference project: [[projects/parking-stopping-mode-dilc]]
- This project intentionally excludes full DILC/wrapper logic and keeps only minimal training/data-model plumbing.
