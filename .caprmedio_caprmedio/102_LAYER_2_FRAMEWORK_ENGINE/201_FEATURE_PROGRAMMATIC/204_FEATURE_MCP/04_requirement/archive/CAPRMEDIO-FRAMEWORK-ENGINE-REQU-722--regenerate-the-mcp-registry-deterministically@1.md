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
# Regenerate the MCP registry deterministically

MCP registry generation must resolve and seal its complete Tool source frontier before publication, use stable ordering, and produce the same semantic registry from the same Tool contracts and project state. Repeated generation over an unchanged frontier must be idempotent, and volatile execution metadata must not change MCP capability identity or schema.
