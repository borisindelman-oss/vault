# Parking stopping_mode (DILC -> PUDO)

## Overview
- **What it is:** Add a new model input `stopping_mode` for parking models, with a wrapper-side mapping from DILC to stop type (PARK vs PUDO).
- **Why it matters:** Lets parking models distinguish park vs pick-up/drop-off using existing DMI plumbing (DILC) while enabling test-time overrides.
- **Primary users:** Parking model training/inference owners; driver interaction / deployment wrapper owners.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-01-20
- **Current priorities:**
  - Document current DILC + driving_controls flow and parking wrapper inputs
  - Identify code touch points for new `stopping_mode` input + adaptor
  - Produce a complete implementation plan (incl. tests/validation)
- **Blockers:**
  - Unknown: source of PUDO labels / how to populate stopping_mode in training data

## Requirements
- **Problem statement:** Parking models need an explicit stop type input (park vs PUDO). Reuse DILC as the on-board toggle; at test time allow overriding via direct `stopping_mode` input.
- **Target users:** Parking model owners, on-board deployment/inference, local tests.
- **Integrations:** Parking deployment wrapper, DMI driving_controls tensor, driver interaction node (optional if adding real DMI field), ST input adaptors.
- **Constraints:** Use parking model + parking deployment wrapper; keep DILC existing behavior intact unless explicitly repurposed for parking; avoid breaking DMI validation.
- **Success criteria:**
  - Parking model accepts `stopping_mode` input (park=0, pudo=1)
  - On-board DILC bit maps to stopping_mode in ParkingDeploymentWrapper
  - Test-time overrides can set stopping_mode without DILC
  - No regressions to existing parking controls (parking_mode, parking_direction, shift_by_wire)

## Design
- **Approach:**
  - Add DataKeys.STOPPING_MODE and a new ST adaptor (similar to parking_mode) with embedding over 2 states.
  - Extend parking model config + ST model builder to optionally include stopping_mode adaptor.
  - Extend ParkingDeploymentWrapperImpl to derive stopping_mode from driving_controls DILC (0=park, 1=pudo), with optional override if stopping_mode already provided in inputs (test path).
  - Update deployment config driving_controls_keys for parking to include DILC (or add new DrivingControlKey if adopting Zak’s DMI changes).
- **Key decisions:**
  - Map DILC OFF->PARK, ON->PUDO (explicit requirement).
  - Keep parking wrapper as source of stopping_mode for on-board; allow override in local tests.
- **Open questions:**
  - Where do PUDO labels live (or how to generate) for training data? No `pudo`/`stopping_mode` fields found in current data pipeline.
  - Should we align with Zak’s DMI changes (new DriverInteractionModelInputs.stopping_mode) or only use DILC mapping? (His branch adds real DMI fields.)

## Build Phases
- **Phase: 1 (Discovery & wiring map)**
  - **Goal:** Map DILC flow + parking wrapper inputs; identify all files to touch.
  - **Work items:**
    - Document DILC plumbing: driver_interaction.proto -> driver_interaction_tensorizer -> driving_controls -> BehaviorCustomizer / wrapper.
    - Document parking wrapper driving_controls handling + parking_mode insertion.
    - Review Zak branch `remotes/origin/zmurez/dmi_stopping_mode` for relevant DMI changes.
  - **Validation:** Notes in this project file with file paths and behaviors.
- **Phase: 2 (Implementation)**
  - **Goal:** Add stopping_mode input + wrapper mapping.
  - **Work items:**
    - Add DataKeys.STOPPING_MODE (shape [B, S] or [B, 1]) in `wayve/ai/zoo/data/keys.py`.
    - Add `StoppingModeSTAdaptor` (embedding size 2) + register in `input_adaptors/__init__.py` and `ADAPTOR_ORDER`.
    - Extend `wayve/ai/zoo/st/models.py` with `use_stopping_mode_adaptor` flag and wire to input adaptors.
    - Extend parking configs (`wayve/ai/si/configs/parking/parking_config.py`) to toggle stopping_mode adaptor (new config flag).
    - Extend training module config (`wayve/ai/si/models/training.py`) to pass `use_stopping_mode` and include it in DeploymentConfig if needed.
    - Update ParkingDeploymentWrapperImpl:
      - Include DILC in `deployment_driving_controls_keys` for parking.
      - Map DILC control (0/1) to DataKeys.STOPPING_MODE.
      - Keep existing controls (parking_mode, parking_direction, shift_by_wire) unchanged.
    - Update visualization/inference helper (`wayve/ai/si/visualisation/inference_model.py`) to map stopping_mode into driving_controls or override path.
  - **Validation:** Unit tests for adaptor, wrapper mapping, driving_controls key handling.
- **Phase: 3 (Optional DMI alignment)**
  - **Goal:** If required, add real DMI stopping_mode inputs (Zak branch style).
  - **Work items:**
    - Extend `driver_interaction.proto` with `StoppingMode` enum + `stopping_mode` field; add new DrivingControlKey(s) (`STOPPING_MODE`, `USER_INITIATED_AUTO_STOPPING`).
    - Update `driver_interaction_tensorizer.cpp`, proto2ros/ros2proto, driver interaction node feature config, and tests.
  - **Validation:** Build proto, update model interface validation tests, ensure DMI field passes through.

## Decisions
- **2026-01-20:** Use DILC as the on-board toggle for stopping_mode (OFF->PARK, ON->PUDO); allow test-time override by setting stopping_mode directly.

## Notes
- **Current DILC flow (main):**
  - DILC is `DrivingControlKey.DILC_MODE` in `wayve/interfaces/protobuf/driver_interaction.proto`.
  - `DrivingControlsTensorizer` maps `dilc_mode` into the driving_controls tensor when DILC_MODE is present.
  - `BehaviorCustomizer` uses DILC to mask `vehicle_indicator_state` (multiply by 0/1).
  - Parking wrapper does not currently include DILC in driving_controls keys (defaults to INITIATE_AUTO_PARKING, PARKING_DIRECTION, ENABLE_SHIFT_BY_WIRE), so DILC is ignored for parking.
- **Parking wrapper inputs (main):**
  - `ParkingDeploymentWrapperImpl` derives `PARKING_MODE`, `PARKING_DIRECTION`, `ENABLE_SHIFT_BY_WIRE` from driving_controls and passes them via DataKeys.
  - `PARKING_MODE` is also inserted in training data via `insert_parking_data` (parking mode heuristic on neutral gear segments).
- **Zak branch (remotes/origin/zmurez/dmi_stopping_mode):**
  - `driver_interaction.proto` adds `StoppingMode` enum and `stopping_mode` field plus new driving controls `USER_INITIATED_AUTO_STOPPING` and `STOPPING_MODE`.
  - `driver_interaction_tensorizer.cpp` maps those into driving_controls.
  - Parking feature registers new parameters for STOPPING_MODE and USER_INITIATED_AUTO_STOPPING.
  - Example snippet (branch):
    - `DrivingControlKey.STOPPING_MODE = 6` and `StoppingMode { PARK=0, PUDO=1 }`.
    - Tensorizer case uses `msg.model_inputs.stopping_mode` with default PARK.
