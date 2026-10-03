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
# Fail closed on invalid Tool projections

MCP must publish a current registry only when every active Tool selected for exposure has a valid, uniquely projectable invocation contract. Any missing contract, name collision, invalid schema, unresolved binding, or ambiguous Tool identity must fail registry publication atomically with explicit diagnostics; MCP must not silently skip the Tool, publish a partial registry, or present a previous registry as current.
