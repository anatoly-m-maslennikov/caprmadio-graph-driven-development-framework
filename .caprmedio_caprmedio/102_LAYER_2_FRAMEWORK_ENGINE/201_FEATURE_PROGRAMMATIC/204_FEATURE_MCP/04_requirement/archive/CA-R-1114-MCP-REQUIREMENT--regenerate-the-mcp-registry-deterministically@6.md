---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Regenerate the MCP registry deterministically

MCP registry generation must resolve and seal its complete Tool source frontier before publication, use stable ordering, and produce the same semantic registry from the same Tool contracts and project state. Repeated generation over an unchanged frontier must be idempotent, and volatile execution metadata must not change MCP capability identity or schema.
