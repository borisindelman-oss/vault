# How to interleave baseline + parking/PUDA models in the deployment wrapper

Think of interleaving like a relay race: the baseline model runs first, then hands the baton to the parking/PUDA model when the “end-of-route/parking” signal fires. The key is that **the wrapper emits the signal**, but **the runner performs the switch**.

## The big idea
- **Python wrapper** (parking deployment wrapper) computes a boolean `interleave_control` output.
- **InterleavedModelRunner** (C++) consumes that output and decides when to switch between model runners.
- **ROS `InterleaveControl`** is published for observability; it is not the switch trigger.

## Architecture in practice (where to look)
- Wrapper signal generation (Python):
  - `wayve/ai/zoo/deployment/deployment_wrapper.py` → `ParkingWrapper`
- Runner selection + switching (C++):
  - `wayve/robot/nodes/inference_node/model_runner/backends/interleaved_model_runner/*`
  - `wayve/robot/nodes/inference_node/model_runner/select_model_runner.cpp`
- Interleave control plumbing:
  - `wayve/interfaces/protobuf/interleave_control.proto`
  - `wayve/robot/nodes/inference_node/model_runner/dmi/outputs/interleave_control/*`
  - `wayve/robot/nodes/inference_node/types/forward_pass_result.hpp`

## How switching works (short version)
1. **Wrapper creates `interleave_control`**:
   - `interleave_control = ~parking` where `parking` is true if end-of-route, parking pose present, non-drive gear, or auto-parking control.
2. **InterleavedModelRunner evaluates policy**:
   - In `InterleavedModelRunner::createForwardPass()`, it calls `policy_->next()` when idle.
   - On a switch event it sets:
     - `primary_runner_` (current model)
     - `secondary_runner_` (new model)
     - `transition_state_ = SWITCH_START_PENDING`
3. **Transition lifecycle**:
   - `SWITCH_START` → `MODEL_ACTIVE_WARMUP` → `SWITCH_FINISH_CACHE_WARMED`
   - Driving plan output is suppressed during warmup until switch finish.

## How models are initialized
- In `createModelRunner()` (`select_model_runner.cpp`), `model_configs` is a vector of `ModelDeploymentConfig`.
- Each config becomes a `RunnerProfile { runner, artefact_id }`.
- The **order of `model_configs` defines the switch indices** (runner 0, runner 1, …).

## Policy choice (what decides when to switch)
- If outputs include `interleave_control`, it uses `ModelControlledSwitchPolicy`:
  - **Falling edge** semantics: switch only on true → false.
- Otherwise, it falls back to `TimeBasedRandomSwitchPolicy`.

## Why this matters for our project
- For our use case, the **wrapper is the right place to implement the heuristic** (end-of-route, parking pose, etc).
- The **runner is already designed to handle interleaving**, so we should wire the control output correctly and let the runner switch.

## Testing ideas (early, lightweight)
- Smoke test: verify `interleave_control` toggles when heuristics trigger.
- Transition check: confirm `InterleavedEvent` sequence in logs during a switch.
- Output sanity: ensure driving plan is suppressed during warmup and resumes after `SWITCH_FINISH`.

## Pitfalls to avoid
- Switching logic in ROS is a dead end: ROS publishes for observability only.
- Avoid updating policy from the secondary model during transitions (the code already prevents this).
- Ensure model interface formats match across configs; interleaving validates equality.

## Lessons learned
- Treat the wrapper as a **signal generator**, not a switch.
- The runner owns the actual handoff; keep the heuristics simple and deterministic.
- Interleaving has a warmup cost—plan for a brief DP suppression window.
