# 2026-01-08 — Task Summary — Parking Waypoints Scatter Plot

## Scope
- Add a simple XY scatter plot for policy waypoints in the parking Bokeh plotter.
- Allow Bokeh visualiser to run as a server when no output path is provided.
- Pause the parking maneuver filter project while switching to the visualization task.

## Changes
- Added a new "Policy Waypoints" plot and rendered policy waypoints as an XY scatter graph.
- Added live Bokeh server mode (no file) when `--output_path` is omitted, with index slider and timestamp display.
- Updated project registry/status to paused for the parking maneuver filter project.

## Files
- /workspace/WayveCode/wayve/ai/si/visualisation/bokeh/plotter/parking_plotter.py
- /workspace/WayveCode/wayve/ai/si/visualisation/bokeh/visualise.py
- /workspace/WayveCode/wayve/ai/si/visualisation/bokeh/README.md
- /home/borisindelman/git/vault/codex/WayveCode/projects/zak-classifiers-parking-maneuver.md
- /home/borisindelman/git/vault/codex/WayveCode/projects/projects.json
- /home/borisindelman/git/vault/codex/WayveCode/projects/projects.md
- /home/borisindelman/git/vault/codex/WayveCode/projects/active-project.txt

## Notes
- No tests run.
- Branch: boris/parking_fixed_reverse_acc.
