# Interleaving models in parking deployment wrapper

## Overview
- **What it is:** Extend the parking deployment wrapper to interleave between the baseline driving model and the parking/PUDA model based on heuristics (e.g., end-of-route).
- **Why it matters:** Enables correct model switching for parking scenarios on-vehicle, meeting new deployment needs.
- **Primary users:** Not specified yet.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-02-03
- **Current priorities:**
  - Review Zach's branch `z_mores/puda` for existing changes.
  - Identify required wrapper changes to support model interleaving.
  - Define switching heuristics and the model-selection interface.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Run two models on-vehicle (baseline driving + parking/PUDA) and switch to parking/PUDA when heuristics like end-of-route trigger. Extend the parking deployment wrapper to support this.
- **Target users:** Not specified yet.
- **Integrations:** Parking deployment wrapper; reference branch `z_mores/puda`.
- **Constraints:** TBD.
- **Success criteria:** Demonstrate interleaving between baseline and parking/PUDA models in the deployment wrapper.

## Design
- **Approach:** Extend the parking deployment wrapper to support model interleaving; start from `z_mores/puda` and adapt as needed.
- **Key decisions:** TBD.
- **Open questions:** Testing strategy; exact heuristics; rollout/validation gates.

## Build Phases
- **Phase:** Phase 1
  - **Goal:** Implement initial interleaving support in the wrapper.
  - **Work items:** Review `z_mores/puda`, map wrapper flow, add switching hook, define config/heuristics (TBD).
  - **Validation:** Demonstrate model switching in a test environment (details TBD).

## Decisions
- **2026-02-03:**
  - **Decision:** Start from Zach's `z_mores/puda` branch as the baseline reference.
  - **Rationale:** It already targets the parking/PUDA deployment path.

## Notes
- Testing plan not defined yet.
