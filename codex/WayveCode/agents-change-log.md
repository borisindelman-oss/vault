# Codex Change Log — WayveCode

## Table of Contents
- [2026-01](#2026-01)
- [2025-12](#2025-12)
- [2025-03](#2025-03)

## 2026-01
> [!summary]- 2026-01 entries
> #### 2026-01-01 — Move Codex notes into Obsidian vault
> - Topic: Vault organization
> - Labels: vault, obsidian, codex
> - Change type: move/rename
> - Areas: `codex/WayveCode/`
> - Changes:
>   - Moved the change log into `/home/borisindelman/git/vault/codex/WayveCode/`.
>   - Renamed task summaries to include dates and updated links: [[2025/12/Week-5/2025-12-29-release-bc-model-summary]], [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]].
>
> #### 2026-01-01 — Move latent actions behavior control guide into Obsidian vault
> - Topic: Vault organization
> - Labels: vault, obsidian, notes
> - Change type: move/rename
> - Areas: `codex/WayveCode/2025/12/Week-4/`
> - Changes:
>   - [[2025/12/Week-4/2025-12-28-latent-actions-behavior-control-guide]]: moved from repo docs and renamed with date.
>
> #### 2026-01-01 — Add Obsidian vault sync scripts
> - Topic: Vault sync
> - Labels: git, sync, automation
> - Change type: add
> - Areas: `/home/borisindelman/git/vault/`, `/home/borisindelman/.config/systemd/user/`
> - Changes:
>   - Added `/home/borisindelman/git/vault/.vault-sync.sh`.
>   - Added `/home/borisindelman/git/vault/.vault-sync-watch.py`.
>   - Added `/home/borisindelman/.config/systemd/user/vault-sync-watch.service` (not enabled here due to missing user bus).
>
> #### 2026-01-01 — Restructure Codex notes by month and week
> - Topic: Vault structure
> - Labels: vault, organization
> - Change type: restructure
> - Areas: `codex/WayveCode/2025/12/Week-*`
> - Changes:
>   - Adopted `YYYY/MM/Week-N/` folders with date-prefixed filenames.
>   - Moved 2025-12 notes into week folders and updated links.

## 2025-12
> [!summary]- 2025-12 entries
> #### 2025-12-30 — Parking maneuver filter (pred_park_type)
> - Topic: Parking maneuver filter
> - Labels: parking, sampling, tests
> - Change type: docs/move
> - Areas: `codex/WayveCode/2025/12/Week-5/`
> - Changes:
>   - [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]: moved task summary into the vault.
>   - [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-change-log]]: moved change log into the vault.
>
> #### 2025-12-29 — Trace BC release model
> - Topic: Release BC model trace
> - Labels: model, config, data
> - Change type: analysis
> - Areas: `wayve/ai/si/`
> - Changes:
>   - Read configs and datamodule implementation for baseline BC release.
> - Files:
>   - /workspace/WayveCode/wayve/ai/si/configs/baseline/release.py
>   - /workspace/WayveCode/wayve/ai/si/config.py
>   - /workspace/WayveCode/wayve/ai/si/datamodules/otf.py
>
> #### 2025-12-29 — Add per-task summary requirement
> - Topic: Documentation workflow
> - Labels: docs, process, vault
> - Change type: update
> - Areas: `AGENTS.md`, `codex/WayveCode/`
> - Changes:
>   - AGENTS.md: added requirement to maintain per-task summaries in the vault.
>   - [[2025/12/Week-5/2025-12-29-release-bc-model-summary]]: added task summary.
>
> #### 2025-12-29 — Add release BC mermaid summary
> - Topic: Model diagram
> - Labels: docs, mermaid, model
> - Change type: add
> - Areas: `codex/WayveCode/2025/12/Week-5/`
> - Changes:
>   - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: added task summary.
>
> #### 2025-12-29 — Fix Mermaid labels
> - Topic: Model diagram
> - Labels: mermaid, docs
> - Change type: update
> - Areas: chat-only (no file change)
> - Changes:
>   - Updated Mermaid diagram in chat to use <br/> and remove parentheses in labels.
>
> #### 2025-12-29 — Add Mermaid to task summary
> - Topic: Model diagram
> - Labels: mermaid, docs
> - Change type: update
> - Areas: `codex/WayveCode/2025/12/Week-5/`
> - Changes:
>   - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram.
>
> #### 2025-12-29 — Add tensor shapes to Mermaid summary
> - Topic: Model diagram
> - Labels: mermaid, docs
> - Change type: update
> - Areas: `codex/WayveCode/2025/12/Week-5/`
> - Changes:
>   - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram with shapes.
>
> #### 2025-12-29 — Add ST transformer diagram
> - Topic: Model diagram
> - Labels: mermaid, docs
> - Change type: update
> - Areas: `codex/WayveCode/2025/12/Week-5/`
> - Changes:
>   - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended ST transformer components diagram.
>
> #### 2025-12-29 — Move Obsidian vault to workspace
> - Topic: Vault setup
> - Labels: vault, obsidian, sandbox
> - Change type: move
> - Areas: `/workspace/WayveCode/vault/codex`, `AGENTS.md`
> - Changes:
>   - Moved vault root to /workspace/WayveCode/vault/codex.
>   - AGENTS.md: updated vault path.

## 2025-03
> [!summary]- 2025-03 entries
> #### 2025-03-09 — Add Codex change-log workflow
> - Topic: Documentation workflow
> - Labels: docs, process, vault
> - Change type: update
> - Areas: `AGENTS.md`
> - Changes:
>   - AGENTS.md: added "Change Log (Codex)" section with Obsidian vault path and entry requirements.
> - Commands:
>   - Edited AGENTS.md via apply_patch.
