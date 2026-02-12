# 2026-02-12 — Naive stopping_mode project setup and plan

## Summary
- Created a new project page: [[projects/parking-stopping-mode-naive-heuristic]].
- Set active project to `parking-stopping-mode-naive-heuristic`.
- Scoped this work as a minimal subset of [[projects/parking-stopping-mode-dilc]].
- Inspected `boris/stopping_mode` for reusable pieces and mapped only required files.

## Requested Scope
- Add stopping_mode input adaptor with a flag (default off).
- Add naive stopping mode logic in OTF/parking path:
  - no gear-neutral detection -> random `PUDO/PARK`
  - gear-neutral detected -> `PARK`
  - gear-neutral + hazard indicator -> `PUDO`
- Extend parking lookahead data with indicator state (parallel to gear lookahead).
- Keep all new behavior flag-gated and off by default.

## Reuse Map From `boris/stopping_mode`
- `wayve/ai/zoo/st/input_adaptors/stopping_mode.py`
- `wayve/ai/zoo/st/input_adaptors/__init__.py`
- `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py`
- `wayve/ai/zoo/st/models.py` (`use_stopping_mode_adaptor`, dropout arg)
- `wayve/ai/zoo/data/keys.py` (`STOPPING_MODE` key)
- `wayve/ai/si/datamodules/otf.py` (parking indicator gather)
- `wayve/ai/zoo/data/parking.py` (hazard + gear heuristic)

## Target Branch
- Working branch: `02-12-park-pudo-stopping-mode-heuristic`

## Next Execution Stages
1. Add adaptor + model/config flag plumbing (default off).
2. Add OTF indicator lookahead loading for parking under flag.
3. Add naive stopping_mode assignment in `parking.py` under flag.
4. Add/adjust tests and validate with targeted Bazel test targets.
