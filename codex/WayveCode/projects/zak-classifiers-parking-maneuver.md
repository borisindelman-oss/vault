# Zak classifiers parking maneuver

## Overview
- **What it is:** Port experimental parking maneuver windowing logic into SI materialization as a reusable filter with tests.
- **Why it matters:** Aligns SI sampling with experimental parking behavior and reduces bad parking samples.
- **Primary users:** Parking model owners, data/annotation pipeline maintainers.

## Status
- **Phase:** Phase 3
- **Status:** paused
- **Last updated:** 2026-01-08
- **Current priorities:**
  - Validate the existing branch implementation and close any gaps vs experimental logic.
  - Run/repair tests for the parking maneuver filter path.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Experimental parking maneuver filters live outside SI materialization; need a reusable SI filter and tests.
- **Target users:** SI materialization users, parking maneuver pipeline owners.
- **Integrations:** SI filters (`wayve/ai/zoo`), annotation loading, unit tests.
- **Constraints:** Keep behavior consistent with experimental logic; avoid broad refactors.
- **Success criteria:** Filter behavior matches experimental logic; tests pass on target suite.

## Design
- **Approach:** Reuse experimental parking maneuver mask logic in SI filters and wire pred_park_type annotations.
- **Key decisions:** Use SI filter helper + targeted unit test; keep changes localized.
- **Open questions:** Any remaining deltas between experimental sampler filters and SI filter behavior?

## Build Phases
- **Phase:** Phase 3
  - **Goal:** Validate and finalize filter + tests.
  - **Work items:**
    - Verify the branch implementation against experimental references.
    - Run SI filter tests and fix failures.
  - **Validation:** `bazel test //wayve/ai/zoo:test_sampling_py_test //wayve/ai/zoo:test_sampling_py_lint_pylint --test_output=errors`

## Decisions
- **2026-01-08:**
  - **Decision:** Continue from existing branch `boris/2025-12-30/zak-classifiers-parking-maneuver`.
  - **Rationale:** Prior work already implemented the filter and test skeleton.

## Notes
- Source task summary: 2025-12-30 parking maneuver filter task summary.
