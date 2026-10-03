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
---
# Bound and control MCP requests

MCP must validate every admitted protocol message before dispatch, apply declared time and resource bounds, support cancellation without corrupting Tool or project state, and expose progress for admitted long-running operations. Invalid, expired, cancelled, or resource-exhausted requests must terminate with explicit structured outcomes and must not leave an ungoverned background operation.
