---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "GRAPH_SERVER/Goal"
  depends_on:
    - "APPS"
version: 1
updated_at: "2026-09-23 04:20:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serve the Derived Graph Headlessly

GRAPH_SERVER **must** own the rebuildable non-authoritative graph read model **and** read-only service used by Tools, MCP, **and** optional interfaces without requiring GRAPH_UI.
