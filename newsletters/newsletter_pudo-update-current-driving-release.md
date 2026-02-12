# Newsletter: PUDO update to current driving release

Branch: `boris/train/pudo_11_02_26`

## Summary
- Data: use release driving data and add PUDO data, with `93% driving / 7% PUDO`.
- Architecture: align parking/PUDO with release behavior+navigation path.
- Model deltas: add parking/PUDO-specific input adaptors (`gear_direction`, `parking_mode`) and keep gear-direction output head in the parking/PUDO adaptor stack.

## Config-level changes
- Release baseline config:
  - `wayve/ai/si/configs/baseline/release.py`
- Parking/PUDO training config:
  - `wayve/ai/si/configs/parking/parking_config.py`
- Output adaptor / heads:
  - `wayve/ai/zoo/outputs/output_adaptor.py`
  - `wayve/ai/zoo/outputs/gear_direction_output_head.py`
- ST + input adaptor paths:
  - `wayve/ai/zoo/st/input_adaptors/gear_direction.py`
  - `wayve/ai/zoo/st/input_adaptors/parking_mode.py`

## Model components diagram (release-aligned, with parking/PUDO additions)
```mermaid
flowchart LR
    A[Release Data Buckets<br/>BC driving set] --> B[Parking BC Datamodule]
    A2[PUDO Buckets<br/>7% sampling] --> B

    B --> C[Input Adaptors]
    C --> D[ST Backbone]
    D --> E[Output Adaptors]
    E --> F[Heads]

    C1[Release Inputs<br/>behavior + navigation] --> C
    C2[Parking/PUDO Add<br/>gear_direction + parking_mode] --> C

    F1[Release Heads<br/>waypoints + indicators] --> F
    F2[Parking/PUDO Add<br/>gear_direction head] --> F

    classDef add fill:#ffe6cc,stroke:#d97904,color:#222,stroke-width:2px;
    class A2,C2,F2 add;
```

## Takeaway
Parking/PUDO now follows the release-style model path (behavior + nav) and differs mainly in data mix plus the parking/PUDO-specific gear/parking-mode IO additions.
