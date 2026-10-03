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
# Require complete Tool invocation contracts

Every active Tool exposed through MCP must provide one complete machine-invocation contract containing its stable Tool identity, model-readable description, capability kind, accepted-input schema, structured result envelope, diagnostic and failure contract, and canonical executable binding. Missing, conflicting, or ambiguous contract fields make that Tool invalid for MCP projection.
