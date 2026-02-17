# Newsletter: Naive parking stopping_mode heuristic (PUDO=0, PARK=1)

## Why we needed this
We wanted a **small, stackable** way to condition parking models on stop intent (park vs PUDO) without reintroducing the full scope of the earlier DILC-to-stopping-mode project. The goal was to add only what we needed for training/model input, keep it behind flags, and keep default behavior unchanged.

In practice, this PR is scoped on top of `02-11-parking_mode_heuristic`, and focuses on:
- adding/using `stopping_mode` as a model input key,
- setting `stopping_mode` inside parking data logic,
- keeping default-off behavior.

## Why this is intentionally naive
This logic is called naive because it does **not** use ground-truth intent labels. It uses simple heuristics:
- parking-window detection from gear/speed,
- hazard-light presence,
- random fallback when not in parking mode.

That makes it fast to roll out and easy to reason about, but not a final labeling strategy.

## Enum values used
For this scoped project we standardized:
- `PUDO = 0`
- `PARK = 1`

Code references:
- `wayve/ai/zoo/data/parking.py` (`STOPPING_MODE_PUDO`, `STOPPING_MODE_PARK`)
- `wayve/ai/zoo/data/keys.py` (`DataKeys.STOPPING_MODE` comment)
- `wayve/ai/zoo/st/input_adaptors/stopping_mode.py` (adaptor value range)

## Exactly how stopping_mode is set
The assignment happens in `wayve/ai/zoo/data/parking.py` in `_add_parking_mode` after `parking_mode` is computed.

1. Feature is active only when `enable_naive_stopping_mode=True`.
2. If active and `additional_parking_indicator_light` is missing, we raise `KeyError`.
3. We compute `parking_mode` from gear neutral windows using `_compute_parking_mode`.
4. Then `_compute_stopping_mode` applies:
   - If `parking_mode=False`: random choice in `{0, 1}`.
   - If `parking_mode=True` and hazard detected in indicator lookahead: `0` (PUDO).
   - If `parking_mode=True` and no hazard: `1` (PARK).
5. If feature flag is off, `stopping_mode` is not written at all.

Hazard detection uses canonical mapping (not hardcoded literals):
- `INDICATOR_STATE_MAPPING[VehicleIndicator.HAZARD.value]`

## Flow sketch
```mermaid
flowchart TD
  A[enable_naive_stopping_mode?] -->|No| Z[Do not write stopping_mode]
  A -->|Yes| B[Compute parking_mode from gear and speed lookahead]
  B --> C{parking_mode at origin?}
  C -->|No| D[stopping_mode = random choice in {0,1}]
  C -->|Yes| E[Check hazard in additional_parking_indicator_light]
  E --> F{hazard present?}
  F -->|Yes| G[stopping_mode = 0 (PUDO)]
  F -->|No| H[stopping_mode = 1 (PARK)]
  D --> I[Write DataKeys.STOPPING_MODE]
  G --> I
  H --> I
```

## Model-side wiring
To consume this signal in ST:
- `wayve/ai/zoo/st/input_adaptors/stopping_mode.py` defines `StoppingModeSTAdaptor`.
- `wayve/ai/zoo/st/input_adaptors/_input_adaptor.py` includes ordering.
- `wayve/ai/zoo/st/models.py` enables it under `use_stopping_mode_adaptor` with `stopping_mode_dropout_probability`.
- `wayve/ai/zoo/st/checkpoints.py` handles compatibility for checkpoints missing adaptor weights.

## Test coverage added for this work
- `wayve/ai/zoo/data/test/test_parking.py`
  - missing indicator guard when feature is enabled,
  - random branch when `parking_mode=False`,
  - park branch (`1`) when parking with no hazard,
  - pudo branch (`0`) when parking with hazard,
  - no `stopping_mode` output when feature is disabled.
- `wayve/ai/zoo/st/test/test_adaptors.py`
- `wayve/ai/zoo/st/test/test_adaptors_params.py`

## Branch context used
- Working branch: `02-12-park-pudo-stopping-mode-heuristic`
- Base for stack alignment: `02-11-parking_mode_heuristic`
- Historical source for selective reuse: `boris/stopping_mode`

The key point: this issue intentionally delivers a narrow, reviewable diff that introduces naive stopping-mode conditioning while keeping behavior behind flags.
