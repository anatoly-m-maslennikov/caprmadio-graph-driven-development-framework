---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Require complete Tool invocation contracts

Every active Tool exposed through MCP must provide one complete machine-invocation contract containing its stable Tool identity, model-readable description, capability kind, accepted-input schema, structured result envelope, diagnostic and failure contract, and canonical executable binding. Missing, conflicting, or ambiguous contract fields make that Tool invalid for MCP projection.
