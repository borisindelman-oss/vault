# WFM → BC → RL (Oct 2025) — Mermaid diagrams

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
  subgraph WFM_Oct_2025_0p5B[WFM v1_2_0_550M — World Model]
    IN[Inputs\n- camera_images (T=16, stride 0.2s)\n- route_map, indicator, speed, speed_limit\n- pose, country, driving_side\n- waypoints, step/lane info] --> PRE[BatchPreprocessor + Image Preprocess<br/>(crop/undistort/normalize)]
    PRE --> TOK[Image Tokenizer\nResNet101 VQ-8K (frozen)]
    TOK --> INAD[InputAdaptor\n(video + state tokens, dropout)]
    INAD --> ENC[ST Transformer Encoder\nlarge / 0.5B, cosine_attn_10, patch_stem]
    ENC --> WM[WorldModel Head (Transformer)]
    WM --> OUT[Outputs\n- predicted future image tokens]
    OUT --> LOSS[Loss\nimage_tokens_cross_entropy = 1.0]
  end
```

## BC (wfm_october_2025_bc) — components + I/O
```mermaid
flowchart TB
  subgraph BC_WFM_Oct[BC — WFM October 2025 backbone]
    IN[Inputs\n- 6 cameras (incl FFT)\n- route_map, speed, speed_limit, pose\n- indicator, step/lane info\n- waypoints + vehicle state] --> PRE[ReducedBlindSpot Preprocess]
    PRE --> INAD[InputAdaptor<br/>(video + state tokens)]
    INAD --> ENC[ST Transformer Encoder\n(from WFM Oct checkpoint)]
    ENC --> OA[BehaviorControl OutputAdaptor<br/>(waypoints + indicator + behavior control)]
    OA --> OUT[Outputs\n- POLICY_WAYPOINTS\n- POLICY_INDICATOR_WEIGHTS\n- POLICY_WAYPOINT_DELTA_LOG_VARIANCES\n- POLICY_LATENT_ACTION_LOGITS\n- BEHAVIOR_LABEL, POLICY_TIME_DELTA]
    OUT --> LOSS[BC Losses\nwaypoints + log-likelihood + indicator\n+ behavior_control]
  end
```

## RL (wfm_oct_rl) — components + I/O
```mermaid
flowchart TB
  subgraph RL_WFM_Oct[Offline RL — TD3/C51]
    IN[Inputs\n- state + next_state/* (SARSA)\n- waypoints / indicators / rewards] --> SE[StateEncoder\n(preprocess + input_adaptor)\n(frozen copy from BC)]
    SE --> TOK[input_tokens (+ radar_tokens)]
    TOK --> POL[Policy\nBC encoder + BC output adaptor\n(trainable)]
    POL --> POUT[Policy Outputs\nwaypoints / indicator / latent action]
    TOK --> CRIT[RLCriticNetwork\nSTPretrainedQTransformer<br/>(encoder copied from BC)]
    POUT --> CRIT
    CRIT --> Q[Q logits / Q values<br/>(C51 optional)]
    Q --> LOSS[RL Losses\nTD3/C51 critic + TD3 actor\n+ actor reg vs BC]
  end
```

## Layer reuse across stages
```mermaid
flowchart LR
  WFM[WFM Oct 2025 checkpoint\n(v1_2_0_550M or 7B)] -->|load input_adaptor + encoder| BC[BC model (wfm_october_2025_bc)]
  WFM -.->|WM head NOT loaded| BC

  BC -->|load full model| RL_POLICY[RL Policy (TD3 actor)]
  BC -->|copy encoder| RL_CRITIC[RL Critic Q-Nets]

  BC -->|input_adaptor copy (frozen)| RL_STATE[RL StateEncoder]
```

## Loss comparison (stage‑level)
```mermaid
flowchart LR
  WFM[WFM Oct 2025] --> L1[image_tokens_cross_entropy]
  BC[BC] --> L2[waypoints + waypoint_log_likelihood\n+ indicator + behavior_control]
  RL[RL] --> L3[TD3/C51 critic\n+ TD3 actor\n+ actor reg vs BC\n(+ optional latent-action top‑k)]
```

## WFM model comparison (Oct 0.5B vs Oct 7B vs Dec 2025 vs YOLO)
```mermaid
flowchart TB
  subgraph OCT_0p5B[Oct 2025 — 0.5B (v1_2_0_550M)]
    O05[st_transformer_size: large (0.5B/16 heads)\nqk_norm: cosine_attn_10\npatch_stem: true\nwm_head: transformer\nloss: image_tokens_ce\npreprocess: foundation batch_preprocessor]
  end

  subgraph OCT_7B[Oct 2025 — 7B (v1_2_0_7B)]
    O7[st_transformer_size: 7B_d4096_l25\nqk_norm: cosine_attn_10\npatch_stem: true\nwm_head: transformer\nloss: image_tokens_ce\npreprocess: foundation batch_preprocessor]
  end

  subgraph DEC_2025[Dec 2025 — WFMStDecember2025Cfg (SI)]
    D25[preprocess: December2025PreprocessCfg\nqk_norm: l2\npatch_stem: true\nstep/lane: true\nautomation_state: true\ngear_direction: true\noutput_adaptor: BehaviorControl]
  end

  subgraph YOLO[Pre‑Dec “YOLO” — WFMSt100xYoloCfg (SI)]
    Y[preprocess: StPreprocess (image_range 0..256)\nqk_norm: None\npatch_stem: true\nautomation_state: true\nmlp_type: clipped_swiglu\noutput_adaptor: default (from StLargeModelCfg)]
  end

  OCT_0p5B --- OCT_7B
  OCT_7B --- DEC_2025
  DEC_2025 --- YOLO
```

## Notes
- Oct 0.5B and Oct 7B are **foundation WFM release configs** (world‑model pretraining).
- Dec 2025 and YOLO are **SI WFM configs** used for driving/BC/RL (space‑time model + behavior control adaptor).
- BC is initialized from Oct 2025 WFM by loading **input_adaptor + encoder only** (no WM head). RL then loads the full BC model and copies encoder weights into the critic.
