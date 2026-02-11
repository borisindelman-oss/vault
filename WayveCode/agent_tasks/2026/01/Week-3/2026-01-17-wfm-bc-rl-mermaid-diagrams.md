# WFM -> BC -> RL (Oct 2025) — Mermaid diagrams

## Sources (code anchors)
- `/workspace/WayveCode/wayve/ai/foundation/models/world_model/config/releases/v1_2_0_550M.yml`
- `/workspace/WayveCode/wayve/ai/foundation/models/world_model/config/releases/v1_2_0_7B.yml`
- `/workspace/WayveCode/wayve/ai/foundation/models/world_model/config/builders.py`
- `/workspace/WayveCode/wayve/ai/zoo/st/models.py`
- `/workspace/WayveCode/wayve/ai/zoo/st/checkpoints.py`
- `/workspace/WayveCode/wayve/ai/zoo/outputs/output_adaptor.py`
- `/workspace/WayveCode/wayve/ai/si/config.py`
- `/workspace/WayveCode/wayve/ai/si/losses/bc_loss_module.py`
- `/workspace/WayveCode/wayve/ai/si/configs/store/offline_rl.py`
- `/workspace/WayveCode/wayve/ai/si/models/offline_rl.py`
- `/workspace/WayveCode/wayve/ai/si/offline_rl/rl_critic_network.py`

## WFM Oct 2025 (v1_2_0_550M) — components + I/O
```mermaid
flowchart TB
  subgraph WFM_Oct_2025_0p5B[WFM v1_2_0_550M - World Model]
    IN[Inputs<br/>camera_images T16 stride 0.2s<br/>route_map indicator speed speed_limit<br/>pose country driving_side<br/>waypoints step_lane_info] --> PRE[BatchPreprocessor + Image Preprocess<br/>crop undistort normalize]
    PRE --> TOK[Image Tokenizer<br/>ResNet101 VQ-8K frozen]
    TOK --> INAD[InputAdaptor<br/>video + state tokens + dropout]
    INAD --> ENC[ST Transformer Encoder<br/>large 0.5B cosine_attn_10 patch_stem]
    ENC --> WM[WorldModel Head - Transformer]
    WM --> OUT[Outputs<br/>predicted future image tokens]
    OUT --> LOSS[Loss<br/>image_tokens_cross_entropy 1.0]
  end
```

## BC (wfm_october_2025_bc) — components + I/O
```mermaid
flowchart TB
  subgraph BC_WFM_Oct[BC - WFM October 2025 backbone]
    IN[Inputs<br/>6 cameras incl FFT<br/>route_map speed speed_limit pose<br/>indicator step_lane_info<br/>waypoints + vehicle state] --> PRE[ReducedBlindSpot Preprocess]
    PRE --> INAD[InputAdaptor<br/>video + state tokens]
    INAD --> ENC[ST Transformer Encoder<br/>from WFM Oct checkpoint]
    ENC --> OA[BehaviorControl OutputAdaptor<br/>waypoints indicator behavior control]
    OA --> OUT[Outputs<br/>POLICY_WAYPOINTS POLICY_INDICATOR_WEIGHTS<br/>POLICY_WAYPOINT_DELTA_LOG_VARIANCES<br/>POLICY_LATENT_ACTION_LOGITS<br/>BEHAVIOR_LABEL POLICY_TIME_DELTA]
    OUT --> LOSS[BC Losses<br/>waypoints + waypoint_log_likelihood<br/>indicator + behavior_control]
  end
```

## RL (wfm_oct_rl) — components + I/O
```mermaid
flowchart TB
  subgraph RL_WFM_Oct[Offline RL - TD3 C51]
    IN[Inputs<br/>state + next_state SARSA<br/>waypoints indicators rewards] --> SE[StateEncoder<br/>preprocess + input_adaptor<br/>frozen copy from BC]
    SE --> TOK[input_tokens + radar_tokens]
    TOK --> POL[Policy<br/>BC encoder + BC output adaptor<br/>trainable]
    POL --> POUT[Policy Outputs<br/>waypoints indicator latent action]
    TOK --> CRIT[RLCriticNetwork<br/>STPretrainedQTransformer<br/>encoder copied from BC]
    POUT --> CRIT
    CRIT --> Q[Q logits / Q values<br/>C51 optional]
    Q --> LOSS[RL Losses<br/>TD3 C51 critic + TD3 actor<br/>actor reg vs BC]
  end
```

## Layer reuse across stages
```mermaid
flowchart LR
  WFM[WFM Oct 2025 checkpoint<br/>v1_2_0_550M or 7B] -->|load input_adaptor + encoder| BC[BC model<br/>wfm_october_2025_bc]
  WFM -.->|WM head not loaded| BC

  BC -->|load full model| RL_POLICY[RL Policy TD3 actor]
  BC -->|copy encoder| RL_CRITIC[RL Critic Q-Nets]

  BC -->|input_adaptor copy frozen| RL_STATE[RL StateEncoder]
```

## Loss comparison (stage-level)
```mermaid
flowchart LR
  WFM[WFM Oct 2025] --> L1[image_tokens_cross_entropy]
  BC[BC] --> L2[waypoints + waypoint_log_likelihood<br/>indicator + behavior_control]
  RL[RL] --> L3[TD3 C51 critic<br/>TD3 actor<br/>actor reg vs BC<br/>optional latent_action top_k]
```

## WFM model comparison (Oct 0.5B vs Oct 7B vs Dec 2025 vs YOLO)
```mermaid
flowchart TB
  subgraph OCT_0p5B[Oct 2025 - 0.5B v1_2_0_550M]
    O05[st_transformer_size large 0.5B 16 heads<br/>qk_norm cosine_attn_10<br/>patch_stem true<br/>wm_head transformer<br/>loss image_tokens_ce<br/>preprocess foundation batch_preprocessor]
  end

  subgraph OCT_7B[Oct 2025 - 7B v1_2_0_7B]
    O7[st_transformer_size 7B_d4096_l25<br/>qk_norm cosine_attn_10<br/>patch_stem true<br/>wm_head transformer<br/>loss image_tokens_ce<br/>preprocess foundation batch_preprocessor]
  end

  subgraph DEC_2025[Dec 2025 - WFMStDecember2025Cfg SI]
    D25[preprocess December2025PreprocessCfg<br/>qk_norm l2<br/>patch_stem true<br/>step_lane true<br/>automation_state true<br/>gear_direction true<br/>output_adaptor BehaviorControl]
  end

  subgraph YOLO[YOLO pre-Dec - WFMSt100xYoloCfg SI]
    Y[preprocess StPreprocess image_range 0..256<br/>qk_norm none<br/>patch_stem true<br/>automation_state true<br/>mlp_type clipped_swiglu<br/>output_adaptor default from StLargeModelCfg]
  end

  OCT_0p5B --- OCT_7B
  OCT_7B --- DEC_2025
  DEC_2025 --- YOLO
```

## Notes
- Oct 0.5B and Oct 7B are foundation WFM release configs (world-model pretraining).
- Dec 2025 and YOLO are SI WFM configs used for driving BC RL (space-time model + behavior control adaptor).
- BC is initialized from Oct 2025 WFM by loading input_adaptor + encoder only (no WM head). RL then loads the full BC model and copies encoder weights into the critic.

## Excalidraw
- [[2026/01/Week-3/2026-01-17-wfm-bc-rl-excalidraw]]
