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
# Negotiate supported MCP protocol capabilities

MCP must declare its supported Model Context Protocol revision and capabilities and negotiate them during initialization. Unsupported revisions, incompatible required capabilities, and invalid lifecycle transitions must fail with explicit machine-readable diagnostics rather than silently changing behavior or accepting an undefined compatibility mode.
