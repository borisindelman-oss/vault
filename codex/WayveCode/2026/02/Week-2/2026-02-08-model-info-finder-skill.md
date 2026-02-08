# Model Info Finder Skill

## Summary
- Created a new Codex skill: `model-info-finder`.
- Simplified it to curl-only usage (no Python helper script, no extra reference/UI files).
- Scope:
- Lookup by `nickname` and `author`.
- Modes: `basic` search and `deep` details via model ID.

## What Was Added
- `~/.codex/skills/model-info-finder/SKILL.md`

## Curl Flows In Skill
- Nickname basic:
- `GET /v2/models/search`
- Author basic:
- `POST /v2/models`
- Deep details:
- `GET /v3/model/<model_id>` after selecting an ID from basic output.

## Notes
- Skill now contains one file only: `SKILL.md`.
- All instructions are explicit curl commands, as requested.
- Updated summary rules:
- Every summary must include `console_url`.
- Summaries should be pretty-printed as a table (`jq` + `column`).
- Deep summaries must include `commit_id`.
- `commit_id` resolution order:
- 1) `<metadata.session_path>/git.hash`
- 2) parse `+_provenance_metadata.git_commit_hash` from `metadata.run_command`
- 3) `unknown`
