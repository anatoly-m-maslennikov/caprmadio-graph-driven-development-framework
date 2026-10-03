---
subject_scopes:
  - framework-engine-mcp
version: 1
updated_at: 2026-08-22 02:06:02
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-713--define-mcp-unit
    - CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-001--supply-active-tools-to-mcp
---
# Discover active Tool units

MCP must discover the complete current set of immediate Tool units owned by `TOOLS` from the current project graph and their corresponding Tool folders. Every registered immediate Tool unit is eligible for MCP exposure unless current project authority or Configuration explicitly disables it; nested implementation helpers and folders that are not Tool units must not become MCP tools.
