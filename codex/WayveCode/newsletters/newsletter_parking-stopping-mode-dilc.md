# Newsletter: teach parking models the difference between PARK and PUDO (stopping_mode)

## The story in one paragraph
If you tell a driver "park" versus "drop off," they plan the maneuver differently. Our parking models needed the same clarity. We introduced a new input, `stopping_mode`, and wired it to the on-board DILC toggle so the model can tell the difference between a true park and a pick-up/drop-off (PUDO). The trick was to do this without breaking existing DMI behavior, while still enabling test-time overrides and good training targets.

## What we built (plain language)
We added a new model input that carries intent (park vs PUDO). On-board, that intent comes from the DILC toggle inside `driving_controls`. In training and local tests, we can also inject `stopping_mode` directly. To teach the model, we generate labels on-the-fly using parking detection and hazard lights, and we shorten the route map near the stopping point so the model sees a plausible destination.

## Architecture at a glance
- **Intent signal:** DILC bit in `driving_controls` maps to `stopping_mode` (OFF=park, ON=pudo).
- **Model input:** `stopping_mode` goes through a dedicated ST adaptor with a 3-state embedding (NA/PARK/PUDO).
- **Training targets:** On-the-fly parking detection + hazard indicator determine PUDO vs PARK for most samples.
- **Map context:** Route polyline is truncated near the stop so the map looks like the route ends there.
- **Overrides:** Local tests can pass `stopping_mode` directly to bypass DILC.

## Codebase map (where the pieces live)
- **Signal definition:** `wayve/ai/zoo/data/keys.py` (DataKeys.STOPPING_MODE)
- **Model input adaptor:** `wayve/ai/zoo/st/input_adaptors/` (StoppingModeSTAdaptor) and `wayve/ai/zoo/st/models.py`
- **Parking configs:** `wayve/ai/si/configs/parking/parking_config.py`
- **Training data (OTF):** `wayve/ai/zoo/data/parking.py` and `wayve/ai/si/datamodules/otf.py`
- **Route map truncation:** `wayve/ai/lib/data/pipes/routes.py` and `wayve/ai/lib/routes.py`
- **Deployment wrapper:** `wayve/ai/zoo/deployment/deployment_wrapper.py`
- **Driving controls plumbing:** `wayve/ai/si/models/training.py`
- **Visualization impact:** `wayve/ai/si/visualisation/inference_model.py` (load with missing weights)

## Why these decisions (the "because" part)
- **Use DILC for intent:** It already exists on-board and fits the "park vs PUDO" choice without inventing new UI.
- **Allow override:** Tests need to set intent without depending on DMI state; the wrapper respects a provided `stopping_mode`.
- **Route shortening:** If the map still shows a full route past the stop, the model learns the wrong story. Truncating the polyline makes the destination feel real.
- **Hazard-based labeling:** Hazard lights are a good proxy for PUDO; we used them to derive PUDO labels on-the-fly.
- **90/10 mix:** 90% of samples get route shortening + hazard-based labels; 10% keep the full route and randomize intent so the model sees both modes.

## What can go wrong (and how we handled it)
- **"Where are the PUDO labels?"** This was an open question. We solved it by generating targets on-the-fly until proper labels are available.
- **Missing weights in older checkpoints:** When adding `stopping_mode`, older checkpoints do not have adaptor weights. The visualization loader uses `strict=False` to avoid breaking.
- **Indicator gating side effects:** DILC also gates indicator state in some wrappers. For parking, we default to *not* masking indicator state (`use_dilc_indicator_state=False`).
- **Route map edge cases:** If the polyline becomes empty, the map can go black. The truncation logic uses a stop index and jitter to keep a valid map.

## Lessons that generalize
- **Ship intent early, even if labels lag.** You can still teach the model by generating interim targets and refining later.
- **Prefer thin, reversible hooks.** The wrapper mapping is small and easy to reason about; it keeps behavior change localized.
- **Protect test-time experimentation.** Overrides are not a hack; they are an explicit design goal.
- **Guard the data story.** The model learns from what the map and inputs imply, not from what we wish they meant.

## If you extend this project
- Add new intent states only if you can define stable labels and update adaptor embeddings.
- Keep the DILC mapping documented and tested so on-board behavior stays predictable.
- When you touch route shortening, verify the map output for empty or near-empty polylines.
