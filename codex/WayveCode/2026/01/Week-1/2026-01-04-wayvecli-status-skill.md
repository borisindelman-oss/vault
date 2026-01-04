# Wayvecli status skill

## Summary
- Created the `wayvecli-status` skill with the Bazel wrapper, examples, and help discovery guidance.
- Packaged the skill to `/workspace/WayveCode/wayvecli-status.skill`.
- Attempted `wayvecli job list`; build failed due to no disk space while downloading CUDA.

## Details
- Command: `cd /workspace/WayveCode/ && bazel --output_user_root=/workspace/WayveCode/.bazel_root run --ui_event_filters=-info,-stdout,-stderr --noshow_progress //tools/wayvecli:wayvecli -- job list`
- Error: `write (No space left on device)` while downloading `cuda_12.8_x86_64.tar.gz` from Artifactory.
- Command: `cd /workspace/WayveCode/ && bazel run --ui_event_filters=-info,-stdout,-stderr --noshow_progress //tools/wayvecli:wayvecli -- job list`
- Error: `cannot open lockfile '/workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/lock' for writing: (error: 13): Permission denied`.

## Files
- `/home/borisindelman/git/assests/codex/skills/wayvecli-status/SKILL.md`
- `~/.codex/skills/wayvecli-status/SKILL.md`
- `/workspace/WayveCode/wayvecli-status.skill`
