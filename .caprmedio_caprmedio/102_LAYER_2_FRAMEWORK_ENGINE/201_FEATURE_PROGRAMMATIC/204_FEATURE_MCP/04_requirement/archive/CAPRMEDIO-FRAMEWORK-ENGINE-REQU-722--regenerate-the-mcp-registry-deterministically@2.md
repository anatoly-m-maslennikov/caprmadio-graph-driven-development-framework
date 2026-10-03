---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Regenerate the MCP registry deterministically

MCP registry generation must resolve and seal its complete Tool source frontier before publication, use stable ordering, and produce the same semantic registry from the same Tool contracts and project state. Repeated generation over an unchanged frontier must be idempotent, and volatile execution metadata must not change MCP capability identity or schema.
