# How to align parking maneuver sampling with real-world behavior (Zak classifiers)

## The story in one paragraph
We had good parking maneuver filters in experimental code, but SI materialization did not use them. That mismatch meant we were sampling the wrong moments, pulling in noisy examples, and missing the maneuvers we actually cared about. This project ports the experimental windowing logic into SI filters, wires in labeled parking/PUDO buckets, and adds tests so the sampling behavior stays stable.

## What we built (plain language)
Think of a parking maneuver as a short movie clip centered on a gear transition. We created filters that reliably find those clips, extend the window when indicators suggest intent, and keep only the slices that match parking or PUDO labels. The result is a reusable SI filter pipeline that mirrors the experimental behavior and a clean bucket inventory that makes sampling predictable.

## Architecture at a glance
- **Core idea:** Detect gear transitions into neutral/park and build a time/dist window around them.
- **Window "extension":** If indicators show intent just before a stop, extend the window backward.
- **Labels:** Use `pred_park_type` labels (1-4 for parking, 7 for drop-off) to separate parking vs PUDO.
- **Hazard signal:** Use hazard indicator light to mark PUDO maneuvers.
- **Masks:** Apply mask sets to drop invalid or out-of-scope data.

## Codebase map (where to look)
- **SI filters and mask sets:** `wayve/ai/zoo/sampling/`
- **Filter tests:** `wayve/ai/zoo/test/sampling/`
- **Bucket inventory:** built into the project config and used by SI sampling
- **Key functions:** `get_parking_indices`, `get_parking_labeled_indices`, `get_pudo_indices`

## Why these decisions (the "because" part)
- **Match experimental logic:** The experimental filters already matched real-world behavior; we preserved their shape rather than rewriting.
- **Clean the gear signal:** Small neutral blips can create false windows, so we clean gear before detecting transitions.
- **Indicator-based extension:** Indicators are the driver telling us, "I am about to park". Use that to avoid cutting the maneuver too short.
- **Separate PUDO buckets:** PUDO has different behavior and requirements, so we isolate it with label 7 and hazard indicators.

## What can go wrong (and how we handled it)
- **Window drift:** If the gear transition is noisy, windows can be offset. Cleaning gear snaps the stop to a reliable entry.
- **Mask mismatch:** Parking and PUDO masks need different exclusions (e.g., PUDO excludes `hazard_indicator` differently). We split base masks to avoid silent contamination.
- **Label ambiguity:** If `pred_park_type` is missing or unknown, sampling can become inconsistent. The filters explicitly check allowed label sets and fall back cautiously.
- **Tests going stale:** Sampling logic drifts easily. We added targeted tests and run them with:
  - `bazel test //wayve/ai/zoo:test_sampling_py_test //wayve/ai/zoo:test_sampling_py_lint_pylint --test_output=errors`

## Lessons that generalize
- **Sampling is a product.** If you change how you sample, you change the model, even when nothing else moves.
- **Trust the signal, but verify.** Indicators and labels are helpful, but they need mask hygiene and tests.
- **Keep changes localized.** The best filter change is one you can reason about in isolation.

## If you extend this project
- Always update both the filter logic and the bucket inventory together.
- Keep parking and PUDO masks separated; shared defaults are not enough.
- When in doubt, add a unit test for the exact edge case you are trying to fix.
