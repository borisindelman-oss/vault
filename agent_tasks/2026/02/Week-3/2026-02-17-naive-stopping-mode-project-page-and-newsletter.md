# 2026-02-17 — Naive stopping_mode project page + newsletter refresh

## Summary
- Updated the active project page [[projects/parking-stopping-mode-naive-heuristic]] with the exact stopping-mode decision rules and current phase metadata.
- Added a new newsletter issue: [[newsletters/newsletter_parking-stopping-mode-naive-heuristic]].
- Updated the newsletter index to include the new issue.

## What was clarified
- `stopping_mode` enum values are documented as:
  - `0 = PUDO`
  - `1 = PARK`
- Assignment logic is now explicitly documented:
  - `parking_mode=False` -> random `{0,1}`
  - `parking_mode=True` + hazard -> `0`
  - `parking_mode=True` + no hazard -> `1`
- The docs now state that behavior is flag-gated and default-off.

## Files updated
- `projects/parking-stopping-mode-naive-heuristic.md`
- `projects/projects.json`
- `projects.md`
- `newsletters/newsletter_parking-stopping-mode-naive-heuristic.md`
- `newsletter_index.md`
