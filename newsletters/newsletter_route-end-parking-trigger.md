# Newsletter: Triggering parking at end-of-route without retraining (wrapper route-end)

## The story in one paragraph
Sometimes the driver reaches the end of a planned route and the model should switch into parking mode, even if the training data never explicitly taught it to. This project adds an inference-only hook in the parking deployment wrapper so the model can treat "end of route" as a legitimate reason to park, using a lightweight map-route signal instead of retraining.

## What we built (plain language)
We detect when the route map looks "finished" (its route signal is mostly gone), and then we allow that to flip parking mode inside the deployment wrapper. Think of it as a quiet stage direction: "The route is over, you may park now." It is a runtime behavior, not a training change.

## Architecture at a glance
- **Signal:** Use the map_route image as a proxy for "end of route".
- **Heuristic:** Sum channels in the route map to detect a low-signal (end) state.
- **Wrapper-only:** The change lives in the parking deployment wrapper; no training data changes.
- **Configurable:** Intended to be gated by a flag or config with a clear threshold.

## Codebase map (where to look)
- **Parking wrapper:** `wayve/ai/zoo/deployment/deployment_wrapper.py`
- **Existing reference logic:** `wayve/ai/experimental/compile.py` (Zak flow)
- **Map inputs:** `map_route` in model inputs

## Why these decisions (the "because" part)
- **Inference-only scope:** We want the behavior without destabilizing training or data pipelines.
- **Map-route heuristic:** It is already available at inference time and cheap to compute.
- **Config gate:** Allows controlled rollout and prevents surprises on non-parking models.

## What can go wrong (and how we plan to avoid it)
- **Threshold sensitivity:** If the sum threshold is too high or low, we will park too early or not at all. This needs a clear spec and tests.
- **Wrong wrapper:** If multiple wrappers touch parking state, we must pick the correct one and avoid duplicated logic.
- **Behavior drift:** A always-on end-of-route trigger can change behavior in places we do not expect. This should be flag-gated.

## Lessons that generalize
- **Runtime hooks are powerful.** They let you change behavior quickly, but they must be explicit and testable.
- **Heuristics should be owned.** If a heuristic exists in experimental code, bring it under versioned, testable control.

## If you extend this project
- Decide the exact threshold and document it (and why).
- Add tests for both end-of-route and not-end-of-route cases.
- Keep the behavior gated behind a config so it can be toggled per deployment.
