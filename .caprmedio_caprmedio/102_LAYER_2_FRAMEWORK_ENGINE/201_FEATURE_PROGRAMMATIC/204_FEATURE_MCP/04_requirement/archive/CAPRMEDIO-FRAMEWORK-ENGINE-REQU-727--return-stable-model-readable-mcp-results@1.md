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
    - CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-002--supply-mcp-tool-interface-to-skills
---
# Return stable model-readable MCP results

MCP must map Tool results, diagnostics, empty results, partial results, and failures into stable model-readable protocol responses while preserving their governed meaning and provenance. Responses must remain usable without a user interface, distinguish protocol failure from Tool failure, and must not expose internal implementation details as part of the public MCP contract.
