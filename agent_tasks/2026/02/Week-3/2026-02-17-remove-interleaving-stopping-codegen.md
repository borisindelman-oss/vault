# Remove Legacy Interleaving Stopping Codegen

- Date: 2026-02-17
- Branch: `boris/train/parking_pudo_interleaving`
- PR: none
- Type: code

## Summary
Removed legacy route interleaving codegen module that is no longer referenced by deployment paths.

## Changes
- Deleted `wayve/ai/zoo/deployment/interleaving_stopping_codegen.py`.

## Validation
- Searched repository for references to:
  - `interleaving_stopping_codegen`
  - `build_route_interleaving_wrapper_codegen`
  - `make_route_interleaving_wrapper_class`
  - `route_interleaving_wrapper_codegen`
- No references remain.
