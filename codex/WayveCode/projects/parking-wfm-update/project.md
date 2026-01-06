# Parking WFM Update

## Overview
- **What it is:** Update the parking model config to use the latest world model config and align training defaults with release settings.
- **Why it matters:** Avoid config mismatches that previously caused bugs and ensure parking training uses the approved world model.
- **Primary users:** Parking model training owners and release stakeholders.

## Status
- **Phase:** Phase 1 - Discovery
- **Status:** active
- **Last updated:** 2026-01-06
- **Current priorities:**
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
-
