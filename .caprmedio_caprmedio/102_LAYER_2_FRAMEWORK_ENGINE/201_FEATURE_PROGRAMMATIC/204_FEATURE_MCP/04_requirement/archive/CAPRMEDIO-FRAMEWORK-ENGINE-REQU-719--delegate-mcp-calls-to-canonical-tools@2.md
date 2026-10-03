---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Delegate MCP calls to canonical Tools

Every MCP invocation must delegate to the selected canonical Tool executable and must not reimplement Tool decisions, project meaning, target resolution, validation, mutation, or recovery behavior inside the MCP carrier. Every Tool must remain independently executable without MCP, and introducing MCP must not create a Tool dependency on MCP or another APPS unit.
