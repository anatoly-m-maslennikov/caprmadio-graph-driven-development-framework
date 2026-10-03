---
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 5
updated_at: 2026-08-23 16:24:28 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Provide one project-local provider-neutral MCP service

One project-local provider-neutral MCP service must expose the complete generated Tool surface; CAPRMEDIO must not require one MCP server per Tool. Every exposed capability must remain usable headlessly without `GRAPH_APP`, user-interface resources, or an agent-host plugin. Agent-host plugins may package or connect to MCP but must not become the owner of provider-neutral MCP or Tool behavior.
