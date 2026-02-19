# Merge planning: interleaving branch vs latest PUDO branch

Date: 2026-02-18
Repo: `/workspace/WayveCode`
Branches:
- `boris/train/parking_pudo_interleaving_w_radar`
- `boris/train/pudo_15_02_26`
- `origin/main`

## Distance from main (ahead/behind)
Using `git rev-list --left-right --count origin/main...<branch>`:
- `boris/train/parking_pudo_interleaving_w_radar`: behind `3442`, ahead `62`
- `boris/train/pudo_15_02_26`: behind `386`, ahead `126`

(`main` local was behind `origin/main` by 3057 commits, so origin/main used for planning.)

## Direct merge simulation between the two branches
Non-destructive check: `git merge-tree --write-tree --name-only boris/train/parking_pudo_interleaving_w_radar boris/train/pudo_15_02_26`

Conflicts found:
- `wayve/ai/si/config.py`
- `wayve/ai/si/configs/parking/parking_config.py`
- `wayve/ai/si/visualisation/bokeh/plotter/helper.py`
- `wayve/ai/zoo/deployment/deployment_wrapper.py`

## Additional context
Merge-base between the two branches: `54e80040ecf`.
Relative to that merge-base:
- interleaving branch unique commits: `37`
- pudo branch unique commits: `3157`

Interleaving branch touched 13 files since split, mostly deployment/interleaving files.
