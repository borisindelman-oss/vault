# Model Info Finder Skill

## Summary
- Created a new Codex skill: `model-info-finder`.
- Scope v1:
- Lookup by `nickname` and `author`.
- Output modes: `basic` and `deep`.

## What Was Added
- `~/.codex/skills/model-info-finder/SKILL.md`
- `~/.codex/skills/model-info-finder/scripts/model_info.py`
- `~/.codex/skills/model-info-finder/references/model-catalogue-endpoints.md`
- `~/.codex/skills/model-info-finder/agents/openai.yaml`

## Validation
- Skill structure validation:
- `python3 .../skill-creator/scripts/quick_validate.py ~/.codex/skills/model-info-finder`
- Result: `Skill is valid!`

## Smoke Tests
- Nickname basic:
- `python3 ~/.codex/skills/model-info-finder/scripts/model_info.py --by nickname --query idealistic-opossum-cyan --mode basic --limit 1`
- Result: 1 model returned.

- Nickname deep:
- `python3 ~/.codex/skills/model-info-finder/scripts/model_info.py --by nickname --query idealistic-opossum-cyan --mode deep --limit 1`
- Result: deep details fetched successfully.

- Author basic:
- `python3 ~/.codex/skills/model-info-finder/scripts/model_info.py --by author --query boris --mode basic --limit 3`
- Result: 0 matches in current dataset for this query.

## Notes
- Script uses only Python stdlib (`urllib`) so it works without `requests`.
- Deep mode calls `/v3/model/<model_id>` per search hit.
