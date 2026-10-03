---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 13
updated_at: 2026-09-23 04:20:00 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define the APPS Scope Unit topology

`APPS` **must** own the following immediate `unordered_unit` Scope Units: `GRAPH_SERVER`, `GRAPH_UI`, `WORKFLOW_ORCHESTRATOR`, **and** `AGENT_HOST_PLUGINS`.

- `GRAPH_SERVER` owns the headless source indexer, rebuildable graph read model, **and** read-only query service derived from governed Atoms **and** Journals.
- `GRAPH_UI` owns the optional human interface over `GRAPH_SERVER` **and** **must not** be required for headless Tool or MCP operation.
- `WORKFLOW_ORCHESTRATOR` owns Workflow Run coordination, interactive Step suspension, continuation, **and** recovery.
- `AGENT_HOST_PLUGINS` owns host-specific integration packages.

None of these applications, their databases, interfaces, or Projections becomes project authority.
