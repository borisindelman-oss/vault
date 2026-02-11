# The Route Map Signal — Newsletter Edition

## The question that keeps coming back
We use `map_route` sums to decide **near end-of-route** and **no-route**. But what do those numbers actually mean? If the threshold is `5e4`, is that big or tiny? What does a “route signal” correspond to in meters?

This issue matters because the interleaving wrapper uses route signal to decide when to switch into parking mode. If we choose a bad threshold, we either switch too early (parking takes over prematurely) or too late (never gets the handoff it needs).

## One sentence summary
**The route map span is `2 * map_scale_m` meters, and a `route_signal` of `5e4` means only a few hundred bright route pixels remain in the image.**

## The map span in meters
From the route map config:
- `map_scale_m` is the **radius of surrounding context**.
- So the full map span is **`2 * map_scale_m` meters** in both width and height.

Examples from `get_route_map_options`:
- `si`: `map_scale_m = 300` → span ≈ **600 m**.
- `si_medium_noise`: `map_scale_m = 1200` → span ≈ **2400 m**.

The ego position is vertically offset by `map_offset` (fraction of image height). For `si_medium_noise`, `map_offset=0.625`, so the ego sits lower in the image and there’s **more forward context** than backward.

## What the route signal actually is
In the interleaving wrapper we compute:
- `route_signal = map_route.float()[:, :2].sum(dim=(1,2,3))`

That means:
- We sum **only the first two channels** (typically red + green) of the raw route map image.
- Input is **uint8** pixels (0–255), so a fully bright pixel contributes 255.

### What does `5e4` mean?
A threshold of `5e4` roughly corresponds to:
- `5e4 / 255 ≈ 196` fully bright pixels.

So `5e4` is the **"almost empty route"** regime. It’s not a long visible path — it’s just a thin or tiny remnant of route signal.

## A concrete mental model
Assume `si_medium_noise` (512×512 map, span ≈ 2400 m). If you had:
- A **1‑pixel‑wide fully bright green line** from top to bottom, the sum would be:
  - `512 * 255 ≈ 130,560`

That is well above `5e4`.

So `5e4` is **not** a full route visible — it’s more like the last few fragments remaining.

## Why this matters for switching
This is why we use two thresholds:
- **`near_end_of_route_sum_thresh`** (e.g. `5e4`) for *"route is nearly gone"*.
- **`end_of_route_sum_thresh`** (default `0`) for *"route is gone"*.

That gives the interleaving wrapper enough runway to:
- latch “near end” early,
- stay latched through noise and map fluctuations,
- and force parking mode when the route is completely absent.

## Quick reference
- **Span** = `2 * map_scale_m`
- **`route_signal`** = sum of red+green pixels
- **`5e4`** ≈ 196 bright pixels
- **Default no‑route** threshold = `0`

## Suggested next step
If you want exact calibration for a specific run, grab the deployment config used for that session and compute:
- `px_per_meter = image_size_px / (2 * map_scale_m)`
- expected sum for a typical route stripe

That gives you a concrete way to pick thresholds tied to physical distance rather than just “magic numbers.”
