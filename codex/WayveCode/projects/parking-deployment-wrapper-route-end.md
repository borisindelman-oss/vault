# Parking deployment wrapper route-end parking mode

## Overview
- **What it is:** Add an inference-only capability in the parking deployment wrapper to trigger parking mode at end-of-route using map-route signal.
- **Why it matters:** Aligns on-road behavior with end-of-route parking expectations without training-time changes.
- **Primary users:** Parking model owners, deployment/runtime owners.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-01-19
- **Current priorities:**
  - Confirm desired behavior and threshold for end-of-route detection from map_route.
  - Identify exact wrapper(s) to modify and whether to gate behind a config/flag.
  - Add/adjust tests to cover end-of-route parking activation behavior.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** End-of-route should be allowed to trigger parking mode at inference time in the deployment wrapper (not training).
- **Target users:** Deployment wrapper consumers, robot inference pipeline users.
- **Integrations:** Parking deployment wrapper, map_route input, driving_controls inputs.
- **Constraints:** Inference-only; avoid impacting training datasets or non-parking models; minimize behavior change behind a flag if needed.
- **Success criteria:** End-of-route parking trigger works as intended in deployment wrapper; tests updated; behavior is controlled and documented.

## Design
- **Approach:** Add optional end-of-route trigger in parking wrapper using map_route signal; make threshold/enable configurable.
- **Key decisions:** Use map_route image sum heuristic; gate via wrapper config or deployment flag.
- **Open questions:**
  - Exact threshold and channels for end-of-route detection?
  - Should this be always-on or flag-gated per deployment?
  - Which wrapper(s) need this (ParkingWrapper only or other wrappers too)?

## Build Phases
- **Phase:** Phase 1
  - **Goal:** Finalize design + implementation plan.
  - **Work items:**
    - Locate current end-of-route logic in zmurez/trt and align intended behavior.
    - Decide config surface and defaults.
  - **Validation:** Code review + unit/integration tests as available.

## Decisions
- **2026-01-19:**
  - **Decision:** Create project to add end-of-route parking trigger capability to parking deployment wrapper.
  - **Rationale:** Capture scope and plan changes from existing conversation.

## Notes
- Found in zmurez/trt: route-end parking heuristic in `wayve/ai/experimental/compile.py` (Zak flow).
```
end_of_route = map_route[0, :2].sum() < 2.5e4
parking = (driving_controls[0, 0] == 1) | end_of_route | parking_position_selected
```
- Route map colours: road fill black, road lines blue, route green; close-distance route can be red when distance_based_colour_coding is enabled. The end-of-route heuristic sums channels 0/1 (red+green), so it ignores blue road lines and reacts to route/ego/close-distance colouring.
- Source branch reference: origin/zmurez/trt contains end-of-route parking trigger in experimental compile and parking wrapper.
