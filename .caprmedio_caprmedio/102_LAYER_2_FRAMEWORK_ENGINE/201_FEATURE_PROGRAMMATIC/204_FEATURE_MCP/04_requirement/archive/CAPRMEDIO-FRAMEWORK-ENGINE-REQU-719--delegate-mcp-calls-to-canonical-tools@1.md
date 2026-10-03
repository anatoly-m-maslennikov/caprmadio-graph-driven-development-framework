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
# Delegate MCP calls to canonical Tools

Every MCP invocation must delegate to the selected canonical Tool executable and must not reimplement Tool decisions, project meaning, target resolution, validation, mutation, or recovery behavior inside the MCP carrier. Every Tool must remain independently executable without MCP, and introducing MCP must not create a Tool dependency on MCP or another APPS unit.
