---
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 4
updated_at: 2026-08-23 16:24:28 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Negotiate supported MCP protocol capabilities

MCP must declare its supported Model Context Protocol revision and capabilities and negotiate them during initialization. Unsupported revisions, incompatible required capabilities, and invalid lifecycle transitions must fail with explicit machine-readable diagnostics rather than silently changing behavior or accepting an undefined compatibility mode.
