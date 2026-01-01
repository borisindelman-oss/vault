# 2025-12-29 — Task Summary — Release BC Model Mermaid

## Scope
- Goal: Provide a high-level mermaid diagram for the release BC model (inputs, layers, outputs).

## Sources
- Model config: `/workspace/WayveCode/wayve/ai/si/configs/baseline/release.py`
- WFM model + preprocess config: `/workspace/WayveCode/wayve/ai/si/config.py`
- ST model assembly: `/workspace/WayveCode/wayve/ai/zoo/st/models.py`
- Behavior control output adaptor: `/workspace/WayveCode/wayve/ai/latent_actions/models/outputs_behavior_control.py`

## Deliverable
- Mermaid diagram shared in chat response.

## Update
- Provided a Mermaid-safe label variant (use <br/> and avoid parentheses).

## Mermaid Diagram
```mermaid
flowchart TD
  Cam["Camera video frames<br/>6 frames, C6T0.2s"]
  Route["Route map / nav context<br/>si_medium_noise"]
  Indicator["Indicator state"]
  Vehicle["Vehicle state<br/>speed, pose/odometry"]
  StepLane["Step & lane info<br/>nav adaptor"]
  WaypointsIn["Waypoints tokens<br/>always dropped in BC config"]

  Cam --> Preprocess["Reduced blind-spot preprocessor<br/>crop/scale/intrinsics"]
  Preprocess --> VideoTok["Video adaptor + vision encoder<br/>ViT backbone to tokens"]
  Route --> RouteTok["Route adaptor to tokens"]
  Indicator --> IndTok["Indicator adaptor to tokens"]
  Vehicle --> SpeedTok["Speed adaptor to tokens"]
  Vehicle --> PoseTok["Pose adaptor to tokens"]
  Vehicle --> SpeedLimitTok["Speed limit adaptor to tokens"]
  StepLane --> StepLaneTok["Step/Lane adaptor to tokens"]
  WaypointsIn --> WaypointsTok["Waypoints adaptor to tokens"]

  VideoTok --> InputAdaptor["InputAdaptor<br/>token concat + temporal encoding"]
  RouteTok --> InputAdaptor
  IndTok --> InputAdaptor
  SpeedTok --> InputAdaptor
  PoseTok --> InputAdaptor
  SpeedLimitTok --> InputAdaptor
  StepLaneTok --> InputAdaptor
  WaypointsTok --> InputAdaptor

  InputAdaptor --> ST["Space-Time Transformer<br/>WFM large"]

  ST --> Out["Behavior Control Output Adaptor"]
  Out --> Waypoints["Future waypoints"]
  Out --> IndicatorOut["Indicator predictions"]
  Out --> Behavior["Behavior control / latent action logits"]
  Out --> Variance["Waypoint variance<br/>auxiliary head"]
```

## Mermaid Diagram With Shapes
```mermaid
flowchart TD
  Cam["Camera video frames<br/>B x T x C x H x W<br/>T=6"]
  Route["Route map / nav context<br/>B x Hm x Wm"]
  Indicator["Indicator state<br/>B x T"]
  Vehicle["Vehicle state<br/>speed/pose/odom<br/>B x T x Fv"]
  StepLane["Step & lane info<br/>B x T x Fs"]
  WaypointsIn["Waypoints tokens<br/>B x T x Fw<br/>always dropped"]

  Cam --> Preprocess["Reduced blind-spot preprocessor<br/>resize/crop/intrinsics"]
  Preprocess --> VideoTok["Video adaptor + vision encoder<br/>tokens: B x T x Nv x D"]
  Route --> RouteTok["Route adaptor<br/>tokens: B x T x Nr x D"]
  Indicator --> IndTok["Indicator adaptor<br/>tokens: B x T x Ni x D"]
  Vehicle --> SpeedTok["Speed adaptor<br/>tokens: B x T x Ns x D"]
  Vehicle --> PoseTok["Pose adaptor<br/>tokens: B x T x Np x D"]
  Vehicle --> SpeedLimitTok["Speed limit adaptor<br/>tokens: B x T x Nsl x D"]
  StepLane --> StepLaneTok["Step/Lane adaptor<br/>tokens: B x T x Nl x D"]
  WaypointsIn --> WaypointsTok["Waypoints adaptor<br/>tokens: B x T x Nw x D"]

  VideoTok --> InputAdaptor["InputAdaptor<br/>concat + temporal enc<br/>tokens: B x T x N x D"]
  RouteTok --> InputAdaptor
  IndTok --> InputAdaptor
  SpeedTok --> InputAdaptor
  PoseTok --> InputAdaptor
  SpeedLimitTok --> InputAdaptor
  StepLaneTok --> InputAdaptor
  WaypointsTok --> InputAdaptor

  InputAdaptor --> ST["Space-Time Transformer<br/>tokens: B x T x N x D"]

  ST --> Out["Behavior Control Output Adaptor"]
  Out --> Waypoints["Future waypoints<br/>B x Tf x 2"]
  Out --> IndicatorOut["Indicator predictions<br/>B x Tf"]
  Out --> Behavior["Behavior control / latent action logits<br/>B x K"]
  Out --> Variance["Waypoint variance<br/>B x Tf x 2"]
```

## ST Transformer Components Diagram
```mermaid
flowchart TD
  In["Input tokens<br/>B x T x N x D"] --> Pad["Optional padding sink tokens<br/>sequence length multiple"]
  Pad --> Blocks["STTransformer stack<br/>L x STBlock"]
  Blocks --> LN["Final LayerNorm"]
  LN --> Out["Output tokens<br/>B x T x N x D"]

  subgraph STBlock["STBlock"]
    SAIn["Tokens<br/>B x T x N x D"] --> SAReshape["Reshape for spatial attn<br/>B*T x N x D"]
    SAReshape --> SALN["LayerNorm"] --> SASA["Self-Attn spatial<br/>non-causal"] --> SAReshapeBack["Restore B x T x N x D"]

    SAReshapeBack --> TAReshape["Permute for temporal attn<br/>B*N x T x D"]
    TAReshape --> TALN["LayerNorm"] --> TASA["Self-Attn temporal<br/>causal"] --> TAReshapeBack["Restore B x T x N x D"]

    TAReshapeBack --> FFN["LayerNorm + MLP"] --> BlockOut["Residual outputs"]
  end
```
