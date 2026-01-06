# Parking WFM Update

## Overview
- **What it is:** Update the parking model config to use the latest world model config and align training defaults with release settings.
- **Why it matters:** Avoid config mismatches that previously caused bugs and ensure parking training uses the approved world model.
- **Primary users:** Parking model training owners and release stakeholders.

## Status
- **Phase:** Phase 1 - Discovery
- **Status:** archived
- **Last updated:** 2026-01-06
- **Current priorities:**
  - Project closed pending formal December WFM release.
  - Locate the December release world model config in Notion and confirm its name.
  - Compare BCWFMSt100xYoloCfg vs WFMStOctober2025Cfg defaults used in parking training.
  - Align training module config (STTrainingModuleCfg vs StBcCfg) and document differences.
  - Plan changes on branch soham/12-18-Parking-model before mainline merge.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Parking training is using BCWFMSt100xYoloCfg and STTrainingModuleCfg, while release uses WFMStOctober2025Cfg and StBcCfg, creating mismatched defaults and prior bugs.
- **Target users:** Parking model trainers and release owners who need consistent configs.
- **Integrations:** WayveCode repo, branch soham/12-18-Parking-model, W&B project parking, Notion release notes for December world model.
- **Constraints:** Changes must be applied on the branch (parking model not in main); preserve training stability; align with December release if available.
- **Success criteria:** Parking training config uses the latest approved world model config (WFMStOctober2025Cfg or December release equivalent) and the release-aligned training module defaults (StBcCfg), with a successful training run logged in W&B.

## Design
- **Approach:** Identify the config entry point for parking training, update the world model config to the latest release, and switch training module defaults to match StBcCfg.
- **Key decisions:** Pending confirmation of December release config from Notion.
- **Open questions:** Is there a December release world model config that supersedes WFMStOctober2025Cfg?

## Build Phases
- **Phase:** Discovery and alignment (Phase 1)
  - **Goal:** Confirm target configs and alignment gaps before code changes.
  - **Work items:** Find release configs in Notion; diff current vs release configs; draft change list.
  - **Validation:** Document the intended changes and get confirmation.

## Decisions
- **2026-01-06:**
  - **Decision:** Adopt the simplified project template sections for this project.
  - **Rationale:** Keep project tracking light-weight and focused.

## Notes
- Project closed after local revert; waiting for formal December release.
- December re-creation checklist:
  - Add WFMStDecember2025Cfg (checkpoint from release) in wayve/ai/si/config.py using load_multi_input_sttransformer_from_wfm_october_pretraining.
  - Add wfm_space_time_december_2025_bc_cfg and BCWFMStDecember2025Cfg, then mode_store name wfm_december_2025_bc.
  - Add parking_bc_wfm_december_2025_cfg + debug cfg using StBcCfg with parking overrides in wayve/ai/si/configs/parking/parking_config.py.
  - Add parking_bc_train_wfm_december_2025 / parking_bc_debug_wfm_december_2025 modes for A/B comparison.
- Reference: [[2026/01/Week-1/2026-01-06-parking-wfm-december-2025-mode]]
- [[2026/01/Week-1/2026-01-06-parking-wfm-october-2025-mode]]
- [[2026/01/Week-1/2026-01-06-parking-wfm-december-2025-mode]]
