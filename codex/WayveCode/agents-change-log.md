# Codex Change Log — WayveCode

## 2026-01-01 — Move Codex notes into Obsidian vault
- Context: Relocate prior Codex task notes into the Obsidian vault and normalize filenames.
- Changes:
  - Moved the change log into `/home/borisindelman/git/vault/codex/WayveCode/`.
  - Renamed task summaries to include dates and updated links: [[2025-12-29-release-bc-model-summary]], [[2025-12-29-release-bc-model-mermaid-summary]].

## 2026-01-01 — Move latent actions behavior control guide into Obsidian vault
- Context: Bring prior latent-actions guide into the vault for Obsidian use.
- Changes:
  - [[2025-12-28-latent-actions-behavior-control-guide]]: moved from repo docs and renamed with date.

## 2025-03-09 — Add Codex change-log workflow
- Context: Update repository guidelines to require an Obsidian change log.
- Changes:
  - AGENTS.md: added "Change Log (Codex)" section with Obsidian vault path and entry requirements.
- Commands:
  - Edited AGENTS.md via apply_patch.

## 2025-12-29 — Trace BC release model
- Context: Identify release BC mode and summarize model/data components.
- Changes:
  - Read configs and datamodule implementation for baseline BC release.
- Files:
  - /workspace/WayveCode/wayve/ai/si/configs/baseline/release.py
  - /workspace/WayveCode/wayve/ai/si/config.py
  - /workspace/WayveCode/wayve/ai/si/datamodules/otf.py

## 2025-12-29 — Add per-task summary requirement
- Context: Add per-task summary file requirement and capture release BC summary.
- Changes:
  - AGENTS.md: added requirement to maintain per-task summaries in the vault.
  - [[2025-12-29-release-bc-model-summary]]: added task summary.

## 2025-12-29 — Add release BC mermaid summary
- Context: Provide a high-level mermaid diagram of the release BC model.
- Changes:
  - [[2025-12-29-release-bc-model-mermaid-summary]]: added task summary.

## 2025-12-29 — Fix Mermaid labels
- Context: Mermaid parse error due to label formatting.
- Changes:
  - Updated Mermaid diagram in chat to use <br/> and remove parentheses in labels.

## 2025-12-29 — Add Mermaid to task summary
- Context: User asked to include the Mermaid diagram in the summary.
- Changes:
  - [[2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram.

## 2025-12-29 — Add tensor shapes to Mermaid summary
- Context: Provide a Mermaid diagram with tensor shapes.
- Changes:
  - [[2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram with shapes.

## 2025-12-29 — Add ST transformer diagram
- Context: Provide a component-level diagram for the space-time transformer.
- Changes:
  - [[2025-12-29-release-bc-model-mermaid-summary]]: appended ST transformer components diagram.

## 2025-12-29 — Move Obsidian vault to workspace
- Context: Relocate the vault to avoid sandbox escalation.
- Changes:
  - Moved vault root to /workspace/WayveCode/vault/codex.
  - AGENTS.md: updated vault path.
