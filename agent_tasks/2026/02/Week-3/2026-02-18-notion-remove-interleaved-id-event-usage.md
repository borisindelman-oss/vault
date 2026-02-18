# Notion update: remove active interleaved id/event usage note

Date: 2026-02-18
Page: Newsletter - Interleaving Models in the Parking Deployment Wrapper
URL: https://www.notion.so/wayve/Newsletter-Interleaving-Models-in-the-Parking-Deployment-Wrapper-30503da5d69a813aa0f7d021923994f5

## Change made
Updated Section 6 to reflect current behavior:
- removed active emission/usage of `interleaved_id` and `interleaved_event` in wrapper output contract
- clarified we monitor switching via wrapper logs/prints
- documented structured-testing telemetry reason:
  - SW robot interleaving uses those signals to aggregate per-model metrics
  - emitting them here would interfere with metric attribution
- kept knowledge documented for future intentional re-enable with telemetry-owner coordination.
