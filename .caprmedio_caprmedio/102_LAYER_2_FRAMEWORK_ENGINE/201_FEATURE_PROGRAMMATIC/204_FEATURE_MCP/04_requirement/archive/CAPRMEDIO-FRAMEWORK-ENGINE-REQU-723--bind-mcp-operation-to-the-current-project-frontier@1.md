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
# Bind MCP operation to the current project frontier

Every MCP service instance and invocation must bind to exactly one resolved CAPRMEDIO project root, selected installed Tool release, current project-graph frontier, and generated MCP registry revision. Discovery and results must expose sufficient source and revision provenance to diagnose currentness; cross-project path escape, unresolved project identity, and invocation through a stale registry must fail explicitly.
