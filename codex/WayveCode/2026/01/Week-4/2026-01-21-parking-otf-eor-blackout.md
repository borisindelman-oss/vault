# 2026-01-21 — Task Summary — Parking OTF end-of-route blackout (Stage 2)

- Status: done
- Goal: Extend parking OTF augmentation to black out the route map 90% of the time on parking frames while keeping 10% parking button behavior.

## Progress
- Extended `insert_parking_data_with_end_of_route_blackout` to apply the 10/90 split and optionally zero map route (and speed limits when present).
- Moved parking insertion after map generation in OTF to ensure blackout operates on map inputs.
- Added `enable_end_of_route_blackout` flag to OTF datamodule and parking config (train only).
- Updated data README to reflect the new function name.

## Tests
- Not run (randomized behavior; no deterministic tests added).

## Files
- `wayve/ai/zoo/data/parking.py`
- `wayve/ai/zoo/data/README.md`
- `wayve/ai/si/datamodules/otf.py`
- `wayve/ai/si/configs/parking/parking_config.py`
