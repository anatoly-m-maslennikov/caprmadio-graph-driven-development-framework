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
# Bind MCP operation to the current project frontier

Every MCP service instance and invocation must bind to exactly one resolved CAPRMEDIO project root, selected installed Tool release, current project-graph frontier, and generated MCP registry revision. Discovery and results must expose sufficient source and revision provenance to diagnose currentness; cross-project path escape, unresolved project identity, and invocation through a stale registry must fail explicitly.
