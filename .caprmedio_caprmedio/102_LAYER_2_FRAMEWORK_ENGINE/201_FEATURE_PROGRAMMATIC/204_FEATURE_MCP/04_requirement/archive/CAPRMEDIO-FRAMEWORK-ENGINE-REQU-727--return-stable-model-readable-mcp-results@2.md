---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Return stable model-readable MCP results

MCP must map Tool results, diagnostics, empty results, partial results, and failures into stable model-readable protocol responses while preserving their governed meaning and provenance. Responses must remain usable without a user interface, distinguish protocol failure from Tool failure, and must not expose internal implementation details as part of the public MCP contract.
