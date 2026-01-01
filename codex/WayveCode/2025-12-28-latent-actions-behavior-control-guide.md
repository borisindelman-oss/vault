# 2025-12-28 — Latent Actions & Behavior Control Implementation Guide

## Overview

This guide provides a comprehensive walkthrough of the latent action and behavioral control system in the Wayve driving model. This system enables the model to predict discrete "actions" from a learned vocabulary and condition its outputs on behavioral preferences.

---

## 1. ActionsDiscretizer: The 31×31 Grid

**Location:** `wayve/ai/zoo/autoregressive.py:386-483`

### How the Grid Works

The system creates **31×31 = 961 discrete actions** over waypoint space:

```python
ActionsDiscretizer(
    timesteps=(2.0,),           # 2 seconds ahead
    n=(31, 31),                 # 31x31 grid
    space="waypoints",          # (x,y) coordinates
    mapping="radial-exponent",  # Denser near vehicle
    rad_exp=1.7,
    max_speed=36.0              # m/s (~130 km/h)
)
```

**Physical extent at 2.0s:**
- **X (forward):** 0 to 72 meters
- **Y (lateral):** -36 to +36 meters

### Encoding: Waypoints → Indices

**Step 1: Normalize**
```python
ij0 = xy / scale  # Scale to [0,1]
```

**Step 2: Apply radial-exponent mapping**
```python
r = (x² + y²)^0.5        # Radius
t = atan2(y, x)          # Angle
r = r^(1/1.7)            # Power transform → denser near center
```

This creates denser sampling near the vehicle and sparser sampling at distance.

**Step 3: Quantize to grid**
```python
ij = (ij0 * 30).round().long()           # [0-30] integers
index = row * 31 + col                    # Flatten: 0-960
residual = ij0 - ij                       # Keep fractional part
```

### Decoding: Indices → Waypoints

The `decode()` method reverses the process:
1. Convert index to (row, col)
2. Add residuals for refinement
3. Apply inverse radial transform
4. Scale to physical units

---

## 2. BehaviorModule: Computing Driving Style

**Location:** `wayve/ai/latent_actions/models/outputs.py:118-179`

### The Behavior Codebook

```python
class BehaviorModule(nn.Module):
    def __init__(self, input_size, num_behavior_control_bins=20, top_k=10):
        self.behavior_codebook = nn.Embedding(20, input_size)
```

20 discrete bins representing slow (0) to fast (19) driving styles.

### How Behavior Labels Are Computed (Training)

**Step 1: Get top-10 predicted trajectories** (behavior-unconditioned)
```python
top_k_waypoints = outputs['behavior_unconditioned.top_k_sampled.policy_waypoints']
top_k_logits = outputs['behavior_unconditioned.top_k_latent_action_logits']
```

**Step 2: Compute mean speeds**
```python
top_k_speeds = compute_mean_speed(top_k_waypoints)    # [B, 10]
gt_speed = compute_mean_speed(policy_waypoints)       # [B]
```

**Step 3: Find percentile**
```python
# Where does ground truth fall in the predicted distribution?
percentile = compute_percentile_vectorized(
    top_k_speeds, top_k_logits, gt_speed
)  # Result: [0.0, 1.0]
```

**Result:** A continuous value where:
- **0.0** = GT is slower than all predictions (conservative)
- **0.5** = GT is at median
- **1.0** = GT is faster than all predictions (aggressive)

### Encoding to Token

```python
bin = (percentile.clamp(0, 0.9999) * 20).long()  # 0-19
behavior_token = behavior_codebook[bin]           # Learned embedding
```

---

## 3. OutputAdaptor: The Full Forward Pass

**Location:** `wayve/ai/zoo/outputs/output_adaptor.py:32-451`

### Architecture

```python
class OutputAdaptor:
    # Learnable components:
    queries                              # Output queries for cross-attention
    cross_attention                      # Final cross-attention
    latent_action_module                 # 961-action predictor + codebook
    latent_action_cross_attention
    behavior_label_encoder               # 20-bin codebook
    output_heads                         # Waypoint, indicator heads
```

### Forward Pass Flow

```python
def forward(self, inputs, outputs):
    tokens = outputs['output_tokens']  # From vision encoder [B, N, D]

    # STEP 1: Compute behavior label (training only)
    if training:
        # Run behavior-unconditioned branch first
        outputs = compute_behavior_label(inputs, outputs)
    else:
        # Use fixed value (default 0.65)
        inputs['behavior_label'] = 0.65

    # STEP 2: Add behavior token to ALL tokens
    behavior_token = behavior_label_encoder(inputs, outputs)
    tokens = tokens + behavior_token.expand(...)

    # STEP 3: Predict & condition on latent action
    # 3a. Cross-attend to get latent action prediction
    la_tokens = latent_action_cross_attention(la_query, tokens)

    # 3b. Predict logits over 961 actions
    logits = linear(la_tokens)  # [B, 1, 961]

    # 3c. Select action
    if training:
        action_idx = privileged_latent_action  # Ground truth
    else:
        action_idx = argmax(logits)  # Predicted

    # 3d. Add latent action embedding to ALL tokens
    la_token = latent_action_codebook[action_idx]
    tokens = tokens + la_token.expand(...)

    # STEP 4: Final output generation
    output_tokens = cross_attention(queries, tokens)
    waypoints = waypoint_head(output_tokens)
    indicators = indicator_head(output_tokens)

    return {'policy_waypoints': waypoints, ...}
```

---

## 4. LatentActionModule Details

**Location:** `wayve/ai/zoo/outputs/latent_action_module.py:26-76`

```python
class LatentActionModule:
    def __init__(self, num_latent_actions=961, input_size=256):
        # Predicts distribution over 961 actions
        self.latent_action_policy_output_head = nn.Linear(256, 961)

        # Embedding table: action index → learned token
        self.latent_action_codebook = nn.Embedding(961, 256)

        # Query for cross-attention
        self.latent_action_query = nn.Parameter(...)
```

**Forward:**
```python
def forward(self, tokens, inputs, outputs):
    # Predict logits
    logits = self.policy_output_head(tokens)  # [B, 1, 961]

    # Select action
    if 'privileged_latent_action' in outputs:
        action = outputs['privileged_latent_action']  # Training
    else:
        action = torch.argmax(logits, dim=-1)         # Inference

    # Return embedding
    return self.latent_action_codebook(action)
```

---

## 5. Training vs Inference

### Training Flow

```
Images + GT Waypoints
         ↓
   Vision Encoder
         ↓
   output_tokens
         ↓
   ┌─────────────┴────────────┐
   ↓                          ↓
[Encode GT Waypoint]  [Behavior-Unconditioned]
   ↓                          ↓
privileged_latent_action  Sample Top-10
   |                          ↓
   |                    Compute Behavior Label
   |                          |
   └──────────┬───────────────┘
              ↓
      Add Behavior Token
      tokens += behavior_embedding
              ↓
      Latent Action Module
      (uses GT action, not predicted)
      tokens += latent_action_embedding
              ↓
      Cross-Attention + Heads
              ↓
      predicted_waypoints
              ↓
      Compute Losses:
      - Waypoint L1/L2
      - Latent action cross-entropy
      - Behavior distillation
```

### Inference Flow

```
Images
   ↓
Vision Encoder
   ↓
output_tokens
   ↓
Add Behavior Token (0.65 default)
tokens += behavior_codebook[13]
   ↓
Latent Action Module:
  1. Predict 961 logits
  2. argmax → action_idx
  3. tokens += latent_action_codebook[action_idx]
   ↓
Cross-Attention + Heads
   ↓
predicted_waypoints
```

### Key Differences

| Aspect | Training | Inference |
|--------|----------|-----------|
| **Latent Action** | Ground truth (teacher forcing) | argmax of predicted logits |
| **Behavior Label** | Computed from GT vs predictions | Fixed 0.65 or user-specified |
| **Unconditioned Branch** | Runs to compute label | Skipped |

---

## 6. Design Rationale

### Why Latent Actions?

1. **Reduces multimodality**: Instead of predicting continuous waypoints directly (which can be multimodal), the model first predicts a discrete "intention" from 961 options, then decodes it.
2. **Enables controllability**: The discrete action space can be manipulated at inference (e.g., sample alternatives, apply constraints).
3. **Simplifies learning**: Cross-entropy loss on discrete actions is often easier to optimize than regression on continuous trajectories.

### Why Behavior Control?

1. **User-controllable driving style**: Operators can adjust aggressiveness without retraining.
2. **Handles distributional shift**: The behavior label captures where the expert demonstration falls in the model's predicted distribution, enabling self-supervised learning of driving style.
3. **Decouples perception from policy**: The encoder learns "what's possible", behavior control learns "what to prefer".

### Why the Two-Stage Training?

During training, the behavior-unconditioned branch runs first to establish a baseline distribution of possible trajectories. The behavior label is computed by comparing ground truth to this distribution. This self-supervised signal trains the behavior codebook to meaningfully control speed/aggressiveness.

---

## 7. Code Reference Summary

| Component | File | Lines |
|-----------|------|-------|
| **ActionsDiscretizer** | `wayve/ai/zoo/autoregressive.py` | 386-483 |
| encode() | `wayve/ai/zoo/autoregressive.py` | 441-450 |
| decode() | `wayve/ai/zoo/autoregressive.py` | 452-462 |
| inputs_to_indices() | `wayve/ai/zoo/autoregressive.py` | 671-736 |
| indices_to_inputs() | `wayve/ai/zoo/autoregressive.py` | 739-811 |
| **BehaviorModule** | `wayve/ai/latent_actions/models/outputs.py` | 118-179 |
| BehaviorLabelEncoder | `wayve/ai/zoo/outputs/behavior_control.py` | 193-239 |
| BehaviorLabelCalculator | `wayve/ai/zoo/outputs/behavior_control.py` | 9-191 |
| compute_mean_speed() | `wayve/ai/latent_actions/models/outputs.py` | 739-757 |
| compute_percentile_vectorized() | `wayve/ai/latent_actions/models/outputs.py` | 760-851 |
| **LatentActionModule** | `wayve/ai/zoo/outputs/latent_action_module.py` | 26-76 |
| LatentActionPolicyOutputHead | `wayve/ai/zoo/outputs/latent_action_module.py` | 11-24 |
| **OutputAdaptor** | `wayve/ai/zoo/outputs/output_adaptor.py` | 32-451 |
| **Config** | `wayve/ai/si/configs/latent_actions/output_adaptor.py` | 9-19 |

---

## 8. Key Configuration

**Location:** `wayve/ai/si/configs/latent_actions/output_adaptor.py:9-19`

```python
ActionsDiscretizerCfg = builds(
    ActionsDiscretizer,
    timesteps=(2.0,),              # Single 2-second prediction
    n=(31, 31),                    # 31x31 = 961 actions
    space="waypoints",
    mapping="radial-exponent",     # Non-uniform density
    rad_exp=1.7,                   # Radial exponent
    grid_shape="square",
    scale_per_timestep=True,
    max_speed=36.0,                # ~130 km/h
)

BehaviorControlOutputAdaptorCfg = builds(
    BehaviorControlOutputAdaptor,
    input_size="${..token_size}",
    future_frames="${future_frames}",
    future_stride_sec="${future_stride_sec}",
    auxiliary_waypoint_variance_output=True,
    delta_waypoints=True,
    latent_action_encoder=ActionsDiscretizerCfg(),
    behavior_control_top_k=10,
    num_behavior_control_bins=20,
)
```

---

## 9. Key Takeaways

- The system uses **961 discrete latent actions** (31×31 grid) with radial-exponent mapping for non-uniform density
- **Behavior control** uses a **20-bin codebook** to condition driving style from conservative (0) to aggressive (19)
- Default inference behavior is **0.65** (bin 13), representing moderately aggressive driving
- During **training**, ground truth actions are used (teacher forcing); during **inference**, predicted actions are used (argmax)
- The behavior label is **self-supervised**: computed by comparing ground truth to the model's own predicted distribution
- Both behavior and latent action embeddings are **added to all tokens** before final output generation

This architecture enables controllable, multimodal trajectory prediction through discrete action spaces and learned behavior conditioning.
