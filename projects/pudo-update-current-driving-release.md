# PUDO update to current driving release

## Overview
- **What it is:** A follow-up project connected to [Parking WFM Update](projects/parking-wfm-update) to align the PUDO (Pick Up / Drop Off) stack with the current driving release.
- **Why it matters:** We need architecture and data-bucket parity with the current driving release while preserving PUDO/parking behavior needed for robotaxi pickup and dropoff.
- **Primary users:** Training/inference engineers working on parking + PUDO deployment and model release readiness.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-02-11
- **Current priorities:**
  - Create the execution checklist and lock source branches/files for comparison.
  - Confirm branch baseline (`boris/train/pudo_11_02_26`) vs `main` for major changes.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Update PUDO to the current driving release with matching architecture and data buckets, while reusing validated parking/PUDO behaviors.
- **Target users:** Robotaxi PUDO model owners and deployment/training maintainers.
- **Integrations:**
  - `release.py` (current driving release reference)
  - `parking_config.py` from `boris/train/parking_pudo` (bucket source)
  - deployment wrapper end-of-route implementation
  - `otf.py` parking-flag path
- **Constraints:**
  - Work branch: `boris/train/pudo_11_02_26`
  - Keep close alignment with `main` unless required deviations are documented.
- **Success criteria:**
  - Architecture alignment documented and validated.
  - PUDO buckets sourced from `boris/train/parking_pudo` and integrated.
  - End-of-route wrapper behavior ported/verified.
  - `otf.py` parking-flag flow verified as expected for parking/PUDO.

## Design
- **Approach:** Incremental parity pass: baseline diff vs `main`, model/release summaries, then targeted config/wrapper/OTF updates.
- **Key decisions:**
  - Treat current driving `release.py` as primary reference.
  - Treat `boris/train/parking_pudo` `parking_config.py` as bucket source of truth for this migration.
- **Open questions:**
  - Are there any mainline release architecture changes after branch cut that must be backported first?
  - Do PUDO buckets need adaptation for current training data schemas?

## Build Phases
- **Phase: Phase 1 - Discovery and parity mapping**
  - **Goal:** Establish exact deltas and lock implementation plan.
  - **Work items:**
    - [ ] Diff `boris/train/pudo_11_02_26` vs `main` and flag dramatic release/training changes.
    - [ ] Summarize current parking model architecture (as baseline relative to PUDO).
    - [ ] Summarize current driving release in `release.py`.
    - [ ] Pull and summarize PUDO bucket definitions from `boris/train/parking_pudo` `parking_config.py`.
    - [ ] Compare current parking buckets vs PUDO buckets and list required config edits.
    - [ ] Identify deployment wrapper end-of-route implementation to reuse/port.
    - [ ] Verify `otf.py` parking-flag behavior is equivalent/compatible for this migration.
    - [ ] Produce final action order for implementation + validation.
  - **Validation:**
    - [ ] Checklist reviewed and accepted before code changes.

- **Phase: Phase 2 - Implementation + validation**
  - **Goal:** Apply changes and verify training/deployment behavior.
  - **Work items:**
    - [ ] Implement approved config/wrapper/OTF updates.
    - [ ] Run targeted checks/tests and compare against expected PUDO behavior.
  - **Validation:**
    - [ ] All agreed checks pass.

## Decisions
- **2026-02-11:**
  - **Decision:** Start from branch `boris/train/pudo_11_02_26`, check drift to `main`, and use `boris/train/parking_pudo` bucket config as migration source.
  - **Rationale:** Minimizes integration risk while preserving known-good PUDO bucket definitions and current release alignment.

## Notes
- PUDO = Pick Up / Drop Off for the robotaxi solution.
- Latest prior training reference branch: `boris/train/parking_pudo`.
