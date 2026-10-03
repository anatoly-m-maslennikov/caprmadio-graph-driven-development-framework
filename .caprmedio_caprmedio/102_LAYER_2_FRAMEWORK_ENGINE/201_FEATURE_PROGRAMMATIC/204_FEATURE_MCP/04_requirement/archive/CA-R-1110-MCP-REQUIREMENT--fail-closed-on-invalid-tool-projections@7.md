---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 7
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Fail closed on invalid Tool projections

MCP must publish a current registry only when every active Tool selected for exposure has a valid, uniquely projectable invocation contract. Any missing contract, name collision, invalid schema, unresolved binding, or ambiguous Tool identity must fail registry publication atomically with explicit diagnostics; MCP must not silently skip the Tool, publish a partial registry, or present a previous registry as current.
