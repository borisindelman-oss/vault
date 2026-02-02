# Model CLI tool

## Overview
- **What it is:** A Python CLI for searching models, fetching details, and presenting results cleanly.
- **Why it matters:** Gives ML engineers quick, reliable model lookup without opening Console.
- **Primary users:** ML engineers.

## Status
- **Phase:** Phase 1
- **Status:** active
- **Last updated:** 2026-02-02
- **Current priorities:**
  - Define CLI commands (search, details, author quick search).
  - Implement model-catalogue API client + auth handling.
  - Add pretty output formatting (tables, JSON).
- **Blockers:**
  - Success criteria TBD.

## Requirements
- **Problem statement:** Provide a CLI that can search models, retrieve details, and display results in a readable format.
- **Target users:** ML engineers.
- **Integrations:** model-catalogue API; likely Databricks for evaluation/experiment/performance lookup.
- **Constraints:** Python.
- **Success criteria:** TBD.

## Design
- **Approach:** Build a lightweight Python CLI (requests-based) with a thin API wrapper and formatted output.
- **Key decisions:**
  - Use model-catalogue REST endpoints directly.
  - Support quick search across id/nickname/author (Console parity).
  - Accept bearer token via env var.
- **Open questions:**
  - Exact success criteria.
  - Databricks integration scope.
  - Preferred output format (table vs JSON by default).

## Build Phases
- **Phase:** Phase 1
  - **Goal:** CLI scaffold + model search and detail commands.
  - **Work items:**
    - CLI entrypoint + command routing.
    - Search endpoint and details endpoint wrappers.
    - Output formatting helpers.
  - **Validation:**
    - Manual run against model-catalogue API with sample queries.

## Decisions
- **2026-02-02:**
  - **Decision:** Start with direct REST calls matching Console behavior.
  - **Rationale:** Faster to deliver and consistent with existing UI.

## Notes
- **Base examples (Jupyter snippets):**

```python
import os
import requests

BASE_URL = "https://model-catalogue-api.azr.internal.wayve.ai"
TOKEN = os.environ.get("MODEL_CATALOGUE_TOKEN")  # set if required

headers = {}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

params = {
      "search": "idealistic-opossum-cyan",
      "limit": 5,
      "ingested_only": "true",
  }

resp = requests.get(f"{BASE_URL}/v2/models/search", params=params, headers=headers, timeout=30)
resp.raise_for_status()
results = resp.json()

# Pick the model ID from the result (often id or model_session_id), then:

model_id = results[0].get("id") or results[0].get("model_session_id")

details = requests.get(
    f"{BASE_URL}/v3/model/{model_id}",
    headers=headers,
    timeout=30,
)
details.raise_for_status()
details.json()


search = "boris"

payload = {
    "page": 0,
    "items_per_page": 25,
    "sort": "ingested_at",
    "sort_direction": "DESC",
    "archived": False,
    "filters": [
        {
            "items": [
                {"id": 0, "columnField": "id", "operatorValue": "contains", "value": search},
                {"id": 1, "columnField": "nickname", "operatorValue": "contains", "value": search},
                {"id": 2, "columnField": "author", "operatorValue": "contains", "value": search},
            ],
            "linkOperator": "or",  # <-- must be lowercase
        }
    ],
}

resp = requests.post(f"{BASE_URL}/v2/models", json=payload, headers=headers, timeout=30)
resp.raise_for_status()
resp.json()
```
