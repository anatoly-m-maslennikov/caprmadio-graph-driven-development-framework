---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: "2026-09-23 04:25:00 +0400"
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

the project-local provider-neutral MCP service exposes an eligible Tool **without** App **or** plugin presentation.

## Test case

Start the MCP service **without** `GRAPH_UI` **or** an agent-host plugin **and** invoke one eligible Tool, retrieve one ACTION_PROMPT invocation, **and** start one Workflow until its next interaction boundary.

## Acceptance criteria

the Tool remains discoverable **and** callable, the prompt returns its self-contained invocation envelope, **and** the Workflow returns its next resumable state through the one project-local service.

## Failure disposition

Reject an MCP deployment that depends on an App **or** transfers provider-neutral ownership **to** a plugin.
