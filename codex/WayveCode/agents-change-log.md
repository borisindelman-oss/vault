# Codex Change Log — WayveCode

## Table of Contents
- [2026-01](#2026-01)
- [2025-12](#2025-12)
- [2025-03](#2025-03)

## 2026-01

#### 2026-01-04 — Vault project manager single-file format
- Topic: Project manager skill
- Labels: #codex #vault #obsidian #process
- Branch: none
- PR: none
- Change type: update
- Areas: `~/.codex/skills/`, `~/.codex/prompts/`, `codex/WayveCode/projects/`, `codex/WayveCode/2026/01/Week-1/`
- Changes:
  - [[2026/01/Week-1/2026-01-04-vault-project-manager-single-file]]: summary and file list.
  - Added `projects.md` index and moved projects to a single `project.md` file.
#### 2026-01-03 — LessWrong definition (Notion)
- Topic: LessWrong definition
- Labels: #notion #shadow-gym #reference
- Branch: none
- PR: none
- Change type: docs
- Areas: `codex/WayveCode/2026/01/Week-1/`
- Changes:
  - [[2026/01/Week-1/2026-01-03-lesswrong-definition]]: summary from Shadow Gym page.

#### 2026-01-03 — Add /plan slash command
- Topic: ExecPlan workflow
- Labels: #codex #prompts #process
- Branch: none
- PR: none
- Change type: add
- Areas: `~/.codex/prompts/`, `codex/WayveCode/2026/01/Week-1/`
- Changes:
  - [[2026/01/Week-1/2026-01-03-plan-slash-command]]: added task note.
  - Added `~/.codex/prompts/plan.md` to generate ExecPlans per `~/.codex/PLANS.md`.

#### 2026-01-01 — Parking maneuver filter refactor
- Topic: Parking maneuver filter
- Labels: #parking #sampling #refactor #tests
- Branch: boris/2025-12-30/zak-classifiers-parking-maneuver
- PR: none
- Change type: refactor/test
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`, `codex/WayveCode/2026/01/Week-1/`
- Changes:
  - [[2026/01/Week-1/2026-01-01-parking-maneuver-filter-refactor]]: new task note (see [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]).
  - Added shared parking transition helper and refactored parking window logic.
  - Added test coverage for transition duration filtering.

#### 2026-01-01 — Move Codex notes into Obsidian vault
- Topic: Vault organization
- Labels: #vault #obsidian #codex
- Branch: unknown
- PR: none
- Change type: move/rename
- Areas: `codex/WayveCode/`
- Changes:
  - Moved the change log into `/home/borisindelman/git/vault/codex/WayveCode/`.
  - Renamed task summaries to include dates and updated links: [[2025/12/Week-5/2025-12-29-release-bc-model-summary]], [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]].

#### 2026-01-01 — Move latent actions behavior control guide into Obsidian vault
- Topic: Vault organization
- Labels: #vault #obsidian #notes
- Branch: unknown
- PR: none
- Change type: move/rename
- Areas: `codex/WayveCode/2025/12/Week-4/`
- Changes:
  - [[2025/12/Week-4/2025-12-28-latent-actions-behavior-control-guide]]: moved from repo docs and renamed with date.

#### 2026-01-01 — Add Obsidian vault sync scripts
- Topic: Vault sync
- Labels: #git #sync #automation
- Branch: unknown
- PR: none
- Change type: add
- Areas: `/home/borisindelman/git/vault/`, `/home/borisindelman/.config/systemd/user/`
- Changes:
  - Added `/home/borisindelman/git/vault/.vault-sync.sh`.
  - Added `/home/borisindelman/git/vault/.vault-sync-watch.py`.
  - Added `/home/borisindelman/.config/systemd/user/vault-sync-watch.service` (not enabled here due to missing user bus).

#### 2026-01-01 — Restructure Codex notes by month and week
- Topic: Vault structure
- Labels: #vault #organization
- Branch: unknown
- PR: none
- Change type: restructure
- Areas: `codex/WayveCode/2025/12/Week-*`
- Changes:
  - Adopted `YYYY/MM/Week-N/` folders with date-prefixed filenames.
  - Moved 2025-12 notes into week folders and updated links.

#### 2026-01-01 — Add Wayve logo terminal animation tool
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: add
- Areas: `wayve/ai/parking/tools/`, `wayve/ai/parking/tools/assets/`
- Changes:
  - Added `wayve/ai/parking/tools/wayve_logo_3d_terminal.py` (stdlib PNG loader, no Pillow).
  - Added `wayve/ai/parking/tools/assets/wayve_icon_navy.png` and wired it as the default logo.
  - Added `wayve/ai/parking/tools/BUILD` with `py_binary` target.

#### 2026-01-01 — Refine Wayve logo animation framing
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Cropped the logo to its alpha bounds and square-cropped for 1:1 aspect.
  - Switched to rows-only sizing with auto cols and top-left anchoring.

#### 2026-01-01 — Adjust Wayve logo rotation behavior
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Centered the rotation axis and shifted extrusion to the right.
  - Made the animation rotate rightward only and run indefinitely when duration is 0.

#### 2026-01-01 — Improve Wayve logo spin framing
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Allowed full coin-style spin with signed skew and left/right depth shift.
  - Reserved room for skew/depth to avoid right-edge clipping during rotation.

#### 2026-01-01 — Fix Wayve logo full spin illusion
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Flipped the logo on the backface to avoid the 180° “bounce” effect.
  - Adjusted front-face brightness curve for clearer 360° rotation.

#### 2026-01-01 — Tune Wayve logo scaling and color
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Added auto padding and optional `--scale` to keep the logo visible at small sizes.
  - Made the base color bluer and clamped skew to avoid edge clipping.

#### 2026-01-01 — Fix terminal aspect ratio compensation
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `wayve/ai/parking/tools/`
- Changes:
  - Added `--char-aspect` and auto-calculated cols from rows to correct non-square character cells.

#### 2026-01-01 — Move terminal logo tool to standalone repo
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: move
- Areas: `/home/borisindelman/git/wayve_terminal_logo/`
- Changes:
  - Moved the implementation and logo asset into `/home/borisindelman/git/wayve_terminal_logo/`.
  - Added `pyproject.toml` and README for uv-based usage.

#### 2026-01-01 — Add static render option
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `/home/borisindelman/git/wayve_terminal_logo/`
- Changes:
  - Added `--disable-spin` to render a single frame and exit.

#### 2026-01-01 — Update defaults for terminal logo
- Topic: Terminal animation
- Labels: #tools #terminal #branding
- Branch: unknown
- PR: none
- Change type: update
- Areas: `/home/borisindelman/git/wayve_terminal_logo/`
- Changes:
  - Default rows set to 60 and depth set to 1.

## 2025-12
#### 2025-12-30 — Parking maneuver filter (pred_park_type)
- Topic: Parking maneuver filter
- Labels: #parking #sampling #tests
- Branch: unknown
- PR: none
- Change type: docs/move
- Areas: `wayve/ai/zoo/sampling/`, `wayve/ai/zoo/test/sampling/`
- Changes:
  - [[2025/12/Week-5/2025-12-30-parking-maneuver-filter-task-summary]]: moved task summary into the vault.

#### 2025-12-29 — Trace BC release model
- Topic: Release BC model trace
- Labels: #model #config #data
- Branch: unknown
- PR: none
- Change type: analysis
- Areas: `wayve/ai/si/`
- Changes:
  - Read configs and datamodule implementation for baseline BC release.
- Files:
  - /workspace/WayveCode/wayve/ai/si/configs/baseline/release.py
  - /workspace/WayveCode/wayve/ai/si/config.py
  - /workspace/WayveCode/wayve/ai/si/datamodules/otf.py

#### 2025-12-29 — Add per-task summary requirement
- Topic: Documentation workflow
- Labels: #docs #process #vault
- Branch: unknown
- PR: none
- Change type: update
- Areas: `AGENTS.md`, `codex/WayveCode/`
- Changes:
  - AGENTS.md: added requirement to maintain per-task summaries in the vault.
  - [[2025/12/Week-5/2025-12-29-release-bc-model-summary]]: added task summary.

#### 2025-12-29 — Add release BC mermaid summary
- Topic: Model diagram
- Labels: #docs #mermaid #model
- Branch: unknown
- PR: none
- Change type: add
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: added task summary.

#### 2025-12-29 — Fix Mermaid labels
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: chat-only (no file change)
- Changes:
  - Updated Mermaid diagram in chat to use <br/> and remove parentheses in labels.

#### 2025-12-29 — Add Mermaid to task summary
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram.

#### 2025-12-29 — Add tensor shapes to Mermaid summary
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended Mermaid diagram with shapes.

#### 2025-12-29 — Add ST transformer diagram
- Topic: Model diagram
- Labels: #mermaid #docs
- Branch: unknown
- PR: none
- Change type: update
- Areas: `codex/WayveCode/2025/12/Week-5/`
- Changes:
  - [[2025/12/Week-5/2025-12-29-release-bc-model-mermaid-summary]]: appended ST transformer components diagram.

#### 2025-12-29 — Move Obsidian vault to workspace
- Topic: Vault setup
- Labels: #vault #obsidian #sandbox
- Branch: unknown
- PR: none
- Change type: move
- Areas: `/workspace/WayveCode/vault/codex`, `AGENTS.md`
- Changes:
  - Moved vault root to /workspace/WayveCode/vault/codex.
  - AGENTS.md: updated vault path.

## 2025-03
#### 2025-03-09 — Add Codex change-log workflow
- Topic: Documentation workflow
- Labels: #docs #process #vault
- Branch: unknown
- PR: none
- Change type: update
- Areas: `AGENTS.md`
- Changes:
  - AGENTS.md: added "Change Log (Codex)" section with Obsidian vault path and entry requirements.
- Commands:
  - Edited AGENTS.md via apply_patch.
