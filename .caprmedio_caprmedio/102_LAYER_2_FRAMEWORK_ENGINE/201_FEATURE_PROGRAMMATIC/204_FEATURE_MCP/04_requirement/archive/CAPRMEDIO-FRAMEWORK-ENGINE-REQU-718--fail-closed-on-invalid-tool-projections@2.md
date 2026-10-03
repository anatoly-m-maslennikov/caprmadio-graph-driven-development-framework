---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Fail closed on invalid Tool projections

MCP must publish a current registry only when every active Tool selected for exposure has a valid, uniquely projectable invocation contract. Any missing contract, name collision, invalid schema, unresolved binding, or ambiguous Tool identity must fail registry publication atomically with explicit diagnostics; MCP must not silently skip the Tool, publish a partial registry, or present a previous registry as current.
