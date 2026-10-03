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
# Require complete Tool invocation contracts

Every active Tool exposed through MCP must provide one complete machine-invocation contract containing its stable Tool identity, model-readable description, capability kind, accepted-input schema, structured result envelope, diagnostic and failure contract, and canonical executable binding. Missing, conflicting, or ambiguous contract fields make that Tool invalid for MCP projection.
