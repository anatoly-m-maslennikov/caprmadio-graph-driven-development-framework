---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "GRAPH_UI/Goal"
  depends_on:
    - "APPS"
    - "GRAPH_SERVER"
version: 1
updated_at: "2026-09-23 04:20:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Provide an Optional Graph Interface

GRAPH_UI **must** own the optional human-facing interface over GRAPH_SERVER and **must not** become a prerequisite for headless graph access, Tools, **or** MCP.
