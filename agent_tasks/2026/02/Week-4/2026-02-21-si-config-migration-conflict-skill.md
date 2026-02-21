# SI Config Migration Conflict Skill (BC/RL)

## Summary
Added a new Codex skill to standardize how to resolve SI config migration merge conflicts for both BC and RL.

## What was added
- New skill: `.ai/skills/si-config-migration-conflicts/SKILL.md`
- Workflow encoded in the skill:
  - bump config version
  - renumber `migrate_to_v*` to the next available version
  - update migration function map
  - accept incoming existing sample snapshot(s)
  - regenerate a new sample snapshot via bazel script
  - update reference config version fields and migration tests

## BC vs RL differences captured
- BC version source: `wayve/ai/si/config.py` (`bc_version.version_number`)
- RL version source: `wayve/ai/si/configs/store/offline_rl.py` (`rl_config_version.version_number`)
- RL migration tests can import specific migration function names; renumbering may require updating test imports.

## Generation commands documented
- BC: `bazel run //wayve/ai/si/scripts:dump_sample_cfg_for_migration_checks -- --training_stage=bc`
- RL: `bazel run //wayve/ai/si/scripts:dump_sample_cfg_for_migration_checks -- --training_stage=rl`

## Branch / PR
- Branch: `02-12-park-pudo-stopping-mode-heuristic`
- PR: none
