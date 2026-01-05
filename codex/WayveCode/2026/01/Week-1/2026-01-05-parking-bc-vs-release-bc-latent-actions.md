# 2026-01-05 — Task Summary — Parking BC vs Release BC (Latent Actions)

## Scope
- Compare ParkingBcTrainCfg (current branch) vs release BC baseline (main).
- Focus on latent action and behavior control differences.
- Provide Mermaid diagrams for each.

## Sources
- /workspace/WayveCode/wayve/ai/si/configs/parking/parking_config.py
- /workspace/WayveCode/wayve/ai/zoo/outputs/output_adaptor.py
- /workspace/WayveCode/wayve/ai/zoo/outputs/latent_action_module.py
- /workspace/WayveCode/wayve/ai/latent_actions/models/outputs_behavior_control.py
- /workspace/WayveCode/wayve/ai/si/config.py (main)
- /workspace/WayveCode/wayve/ai/si/configs/baseline/release.py (main)

## Reference
- [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]

## Hydra-zen config composition
- ParkingBcTrainCfg: make_config(bases=(BCWFMSt100xYoloCfg,), model=parking_bc_cfg, ...).
- parking_bc_cfg: STTrainingModuleCfg(model=ParkingModelCfg(), bc_losses=default_losses_parking, enable_behavior_control=False, use_gear_direction=True, use_parking_mode=True).
- ParkingModelCfg: make_config(bases=(WFMSt100xYoloCfg,), output_adaptor=ParkingOutputAdaptorCfg(), use_gear_direction_adaptor, use_parking_mode_adaptor).
- Release BC baseline: BcBaselineCfg in release.py uses baseline_bc_model (StBcCfg) with WFMStOctober2025Cfg and enable_behavior_control=True.
- WFMStOctober2025Cfg uses BehaviorControlOutputAdaptorCfg from wayve/ai/si/config.py (main).

## Latent action differences (key)
- Parking model uses the new zoo OutputAdaptor with enable_latent_action tied to bc_losses.w_latent_action (1.0) and enable_behavior_control=False.
- Release baseline uses the legacy BehaviorControlOutputAdaptor with w_behavior_control=1.0 and no explicit latent action loss in the release config.
- Both use ActionsDiscretizer with matching parameters (timesteps=2.0, n=(31, 31), radial-exponent, rad_exp=1.7, max_speed=36.0).
- Parking injects a latent action token directly into the token stream to condition outputs; release injects a behavior token computed from top-k latent action samples.
- Parking latent action encoding flips target waypoint x for reverse gear; release behavior control adaptor does not apply gear-direction handling.
- Parking enables gear-direction prediction and parking mode adaptor; release baseline does not enable these heads/adaptors.

## Mermaid — ParkingBcTrainCfg (latent action enabled)
```mermaid
flowchart TD
  Cam["Camera video frames<br/>T=6, stride 0.20s"]
  Route["Route map<br/>si_medium_noise"]
  Indicator["Indicator state"]
  Vehicle["Vehicle state"]
  Gear["Gear direction"]
  ParkMode["Parking mode"]

  Cam --> Preprocess["YOLO preprocessor"]
  Preprocess --> VideoTok["Video adaptor + vision encoder"]
  Route --> RouteTok["Route adaptor"]
  Indicator --> IndTok["Indicator adaptor"]
  Vehicle --> VehTok["Vehicle adaptors"]
  Gear --> GearTok["Gear direction adaptor"]
  ParkMode --> ParkTok["Parking mode adaptor"]

  VideoTok --> InputAdaptor["InputAdaptor<br/>token concat + temporal enc"]
  RouteTok --> InputAdaptor
  IndTok --> InputAdaptor
  VehTok --> InputAdaptor
  GearTok --> InputAdaptor
  ParkTok --> InputAdaptor

  InputAdaptor --> ST["Space-Time Transformer<br/>WFM St100x YOLO"]

  ST --> LatentQ["Latent action query + cross-attn"]
  LatentQ --> LatentHead["Latent action logits"]
  LatentHead --> LatentToken["Latent action token<br/>ActionsDiscretizer"]

  ST --> OutputTokens["Output queries + cross-attn"]
  LatentToken --> OutputTokens

  OutputTokens --> Waypoints["Waypoints"]
  OutputTokens --> IndicatorOut["Indicator predictions"]
  OutputTokens --> GearOut["Gear direction predictions"]
  LatentHead --> LatentLogits["Latent action logits"]
```

## Mermaid — Release BC baseline in main (behavior control)
```mermaid
flowchart TD
  Cam["Camera video frames<br/>T=6, stride 0.20s"]
  Route["Route map<br/>si_medium_noise"]
  Indicator["Indicator state"]
  Vehicle["Vehicle state"]
  StepLane["Step and lane info"]
  WaypointsIn["Waypoints tokens<br/>dropped in BC"]

  Cam --> Preprocess["Reduced blind-spot preprocessor"]
  Preprocess --> VideoTok["Video adaptor + vision encoder"]
  Route --> RouteTok["Route adaptor"]
  Indicator --> IndTok["Indicator adaptor"]
  Vehicle --> VehTok["Vehicle adaptors"]
  StepLane --> StepLaneTok["Step/Lane adaptor"]
  WaypointsIn --> WaypointsTok["Waypoints adaptor"]

  VideoTok --> InputAdaptor["InputAdaptor<br/>token concat + temporal enc"]
  RouteTok --> InputAdaptor
  IndTok --> InputAdaptor
  VehTok --> InputAdaptor
  StepLaneTok --> InputAdaptor
  WaypointsTok --> InputAdaptor

  InputAdaptor --> ST["Space-Time Transformer<br/>WFM October 2025"]

  ST --> BehaviorUncond["Behavior-unconditioned outputs"]
  BehaviorUncond --> TopK["Top-k latent action samples"]
  TopK --> BehaviorLabel["Behavior label"]
  BehaviorLabel --> BehaviorToken["Behavior token"]

  ST --> OutputTokens["Output queries + cross-attn"]
  BehaviorToken --> OutputTokens

  OutputTokens --> Waypoints["Waypoints"]
  OutputTokens --> IndicatorOut["Indicator predictions"]
  OutputTokens --> BehaviorLogits["Behavior control / latent action logits"]
  OutputTokens --> Variance["Waypoint variance"]
```
