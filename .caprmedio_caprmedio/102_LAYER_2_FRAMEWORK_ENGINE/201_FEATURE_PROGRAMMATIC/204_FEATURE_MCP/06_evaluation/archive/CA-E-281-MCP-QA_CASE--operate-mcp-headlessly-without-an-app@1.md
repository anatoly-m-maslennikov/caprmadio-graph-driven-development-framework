---
atom_id: CA-E-281
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-175
  derived_from:
    - CA-A-057
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
