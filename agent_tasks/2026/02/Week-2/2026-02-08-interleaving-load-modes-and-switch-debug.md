# Interleaving docs refresh (production design)

## Scope
- Refreshed project and how-to docs for the interleaving deployment wrapper.
- Restored reference notes that must remain:
  - `zmurez/pudo` interleaving compile approach.
  - `main` branch `interleaved_wrapper.py` telemetry conventions.
- Re-centered documentation on intended production behavior instead of temporary debugging variants.

## Updated content
- Documented intended model load-mode configuration for both branches:
  - `wrapper|ingested`
- Documented intended switching mechanism:
  - near-end (latched), initiate-auto-park, reverse gear, end-of-route/no-route, speed hysteresis.
- Restored mermaid switching diagram describing end-to-end branch selection flow.
- Preserved interleaving telemetry outputs as part of target behavior:
  - `interleaved_id`
  - `interleaved_event`

## Notes
- Project page: `projects/interleaving-models-in-parking-deployment-wrapper`
- How-to page: `newsletters/newsletter_interleaving-models-in-parking-deployment-wrapper`
