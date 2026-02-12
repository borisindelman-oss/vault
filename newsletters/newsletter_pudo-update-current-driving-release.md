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

## Model components diagram (`torch.nn.Module` only)
```mermaid
flowchart LR
    A[InputAdaptor nn.Module] --> B[MIMOSTTransformer / ST backbone nn.Module]
    B --> C[OutputAdaptor nn.Module]

    A1[Behavior inputs adaptor<br/>nn.Module] --> A
    A2[Navigation inputs adaptor<br/>nn.Module] --> A
    A3[GearDirection adaptor<br/>nn.Module] --> A
    A4[ParkingMode adaptor<br/>nn.Module] --> A

    C1[Waypoint head<br/>nn.Module] --> C
    C2[Indicator head<br/>nn.Module] --> C
    C3[GearDirection head<br/>nn.Module] --> C

    classDef add fill:#ffe6cc,stroke:#d97904,color:#222,stroke-width:2px;
    class A3,A4,C3 add;
```

## Takeaway
Parking/PUDO now follows the release-style model path (behavior + nav) and differs mainly in data mix plus the parking/PUDO-specific gear/parking-mode IO additions.
