---
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 5
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Negotiate supported MCP protocol capabilities

MCP must declare its supported Model Context Protocol revision and capabilities and negotiate them during initialization. Unsupported revisions, incompatible required capabilities, and invalid lifecycle transitions must fail with explicit machine-readable diagnostics rather than silently changing behavior or accepting an undefined compatibility mode.
