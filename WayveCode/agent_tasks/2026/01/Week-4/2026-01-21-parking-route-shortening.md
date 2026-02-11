# 2026-01-21 — Task Summary — Parking route shortening (Stage 2)

- Status: done
- Goal: Truncate route polylines near parking entry to simulate end-of-route without blackouts.

## Progress
- Added parking entry distance annotation in `insert_parking_data_with_route_shortening`.
- Routed `enable_route_shortening_for_parking` through OTF and into `insert_map_data`.
- Truncated decoded route polylines (and speed limits) in `RouteMapFetcher` prior to map generation.
- Added `PARKING_ENTRY_DISTANCE_M` key for downstream use.

## Tests
- Not run.

## Files
- `wayve/ai/zoo/data/parking.py`
- `wayve/ai/zoo/data/keys.py`
- `wayve/ai/zoo/data/driving.py`
- `wayve/ai/lib/data/pipes/routes.py`
- `wayve/ai/si/datamodules/otf.py`
- `wayve/ai/si/configs/parking/parking_config.py`
- `wayve/ai/zoo/data/README.md`
