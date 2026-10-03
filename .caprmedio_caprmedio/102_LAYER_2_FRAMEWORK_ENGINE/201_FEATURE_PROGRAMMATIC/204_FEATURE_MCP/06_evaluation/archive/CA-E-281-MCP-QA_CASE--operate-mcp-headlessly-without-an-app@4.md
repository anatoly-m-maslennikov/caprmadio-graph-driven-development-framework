---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 4
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-175
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Operate MCP headlessly without an App

## Claim checked

The project-local provider-neutral MCP service exposes an eligible Tool without App or plugin presentation.

## Test case

Start the MCP service without `GRAPH_APP` or an agent-host plugin and invoke one eligible Tool.

## Acceptance criteria

The Tool remains discoverable and callable through the one project-local service.

## Failure disposition

Reject an MCP deployment that depends on an App or transfers provider-neutral ownership to a plugin.
