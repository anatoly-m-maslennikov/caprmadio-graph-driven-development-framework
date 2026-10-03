---
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 5
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Discover active Tool units

MCP must discover the complete current set of immediate Tool units owned by `TOOLS` from the current project graph and their corresponding Tool folders. Every registered immediate Tool unit is eligible for MCP exposure unless current project authority or Configuration explicitly disables it; nested implementation helpers and folders that are not Tool units must not become MCP tools.
