# Parking stopping_mode naive heuristic

## Overview
- **What it is:** Add a minimal stopping_mode heuristic path for parking data and model input usage, gated behind new flags (off by default).
- **Why it matters:** We want the core park vs PUDO conditioning signal without pulling in the full prior `boris/stopping_mode` scope.
- **Primary users:** Parking model training owners and data pipeline maintainers.

## Status
- **Phase:** Phase 2
- **Status:** active
- **Last updated:** 2026-02-12
- **Branch:** 02-12-park-pudo-stopping-mode-heuristic
- **Current priorities:**
  - Extend OTF parking lookahead loading with indicator-light data (same path as gear lookahead).
  - Implement naive stopping_mode assignment in `parking.py` under flag control.
  - Add/extend tests for heuristic branches in parking/OTF path.
- **Blockers:**
  - Confirm expected hazard encoding in the loaded indicator field (`"hazard"` string vs numeric enum) in current data.

## Requirements
- **Problem statement:** We need a lightweight stopping_mode target/input path that sets PARK vs PUDO from simple parking heuristics, but must not change existing behavior unless explicitly enabled.
- **Target users:** Parking BC training owners.
- **Integrations:**
  - `wayve/ai/zoo/st/input_adaptors/*` and `wayve/ai/zoo/st/models.py`
  - `wayve/ai/zoo/data/parking.py`
  - `wayve/ai/si/datamodules/otf.py`
  - Parking config flags under `wayve/ai/si/configs/parking/`
- **Constraints:**
  - Flags default to off.
  - Keep existing `parking_mode` behavior unchanged when the new heuristic is disabled.
  - Reuse only minimal code from `boris/stopping_mode`.
- **Success criteria:**
  - A new stopping_mode adaptor is available and only active when enabled by flag.
  - OTF loads additional parking indicator lookahead data when needed for heuristic.
  - Stopping mode logic works as requested:
    - no gear-neutral detection -> random `PUDO/PARK`
    - gear-neutral detected -> `PARK`
    - gear-neutral + hazard indicator -> `PUDO`
  - End-to-end path remains no-op unless flags are enabled.

## Design
- **Approach:**
  - Port the stopping-mode adaptor plumbing from `boris/stopping_mode` (key, adaptor class, registration, model builder args) with defaults set to disabled.
  - Add a dedicated OTF/datapipe flag to gather `additional_parking_indicator_light` alongside existing `additional_parking_gear_direction`/speed lookahead.
  - Add naive stopping_mode assignment in `parking.py` with explicit flag gating; keep route-shortening and other previous-project extras out of scope.
- **Key decisions:**
  - This project intentionally excludes route-shortening logic (`PARKING_ENTRY_DISTANCE_M`, stop-route index/fraction).
  - Naive heuristic is computed in parking data insertion path, not in deployment wrapper.
- **Open questions:**
  - Whether to include a `NA` class fallback now, or keep output strictly `{PARK, PUDO}` for this heuristic pass.

## Build Phases
- **Phase 1: Extract minimal reusable pieces from `boris/stopping_mode`**
  - **Goal:** Identify exact lines/files to port with least surface area.
  - **Work items:**
    - Reference points captured from `boris/stopping_mode`:
      - `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
      - `wayve/ai/zoo/st/input_adaptors/__init__.py`
      - `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py`
      - `wayve/ai/zoo/st/models.py` (use flag + dropout arg)
      - `wayve/ai/zoo/data/keys.py` (`STOPPING_MODE` key)
      - `wayve/ai/si/datamodules/otf.py` (parking indicator gather)
      - `wayve/ai/zoo/data/parking.py` (hazard + gear heuristic)
  - **Validation:**
    - Confirm target branch currently lacks stopping_mode adaptor/key wiring.
  - **Status:** Completed (2026-02-12).

- **Phase 2: Add stopping_mode adaptor with flag-off defaults**
  - **Goal:** Introduce model-side support safely.
  - **Work items:**
    - Add `DataKeys.STOPPING_MODE`.
    - Add `StoppingModeSTAdaptor` and register in adaptor exports/order.
    - Add `use_stopping_mode_adaptor` + dropout arg in ST model builder.
    - Add/extend parking config flags so feature remains disabled by default.
  - **Validation:**
    - Unit/import checks and config sanity test(s).
  - **Status:** Completed (2026-02-12).

- **Phase 3: OTF + parking heuristic wiring**
  - **Goal:** Compute stopping_mode from naive rules when enabled.
  - **Work items:**
    - OTF: add indicator lookahead loading for parking path under flag.
    - parking data: implement requested heuristic with hazard detection and random fallback.
    - Ensure no behavior change when heuristic flag is false.
  - **Validation:**
    - Add/extend regression tests for heuristic branches.

- **Phase 4: End-to-end validation and rollout guardrails**
  - **Goal:** Verify integration behavior and default-off safety.
  - **Work items:**
    - Run targeted Bazel tests for modified modules.
    - Confirm datapipe outputs include stopping_mode only when enabled.
  - **Validation:**
    - Test evidence captured in task note and change log.

## Decisions
- **2026-02-12:**
  - **Decision:** Start from branch `02-12-park-pudo-stopping-mode-heuristic`, use `boris/stopping_mode` only as a source of minimal reusable snippets.
  - **Rationale:** Keeps this project small and avoids carrying full historical scope.
- **2026-02-12:**
  - **Decision:** Keep all new behavior behind explicit flags that default to off.
  - **Rationale:** Prevents accidental training/inference behavior changes during integration.
- **2026-02-12:**
  - **Decision:** Add explicit BC/RL config migrations for stopping-mode adaptor fields and bump config versions.
  - **Rationale:** Keeps legacy config loading stable while introducing new model arguments.

## Notes
- Reference project: [[projects/parking-stopping-mode-dilc]]
- This task is a scoped subset of that project, focused on naive heuristic labeling and adaptor plumbing only.
