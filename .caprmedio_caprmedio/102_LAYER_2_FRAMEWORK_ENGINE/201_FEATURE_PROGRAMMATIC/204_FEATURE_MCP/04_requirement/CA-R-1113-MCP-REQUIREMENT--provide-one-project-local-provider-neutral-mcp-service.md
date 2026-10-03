---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 10
updated_at: 2026-09-23 04:25:00 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Provide one project-local provider-neutral MCP service

One project-local provider-neutral MCP service **must** expose the complete active callable surface for Tools, Prompts, **and** Workflows; CAPRMEDIO **must not** require one MCP server per capability. Programmatic calls return their results. Prompt calls return the selected prompt plus its invocation envelope for the main session. Workflow calls start **or** resume the applicable Workflow Run and return the next programmatic result, interactive Step invocation, Operator request, completion, **or** failure state. Every exposed capability **must** remain usable headlessly without `GRAPH_UI` **or** an agent-host plugin. Agent-host plugins **may** package **or** connect **to** MCP but **must not** become the owner of provider-neutral MCP, Tool, Prompt, **or** Workflow behavior.
