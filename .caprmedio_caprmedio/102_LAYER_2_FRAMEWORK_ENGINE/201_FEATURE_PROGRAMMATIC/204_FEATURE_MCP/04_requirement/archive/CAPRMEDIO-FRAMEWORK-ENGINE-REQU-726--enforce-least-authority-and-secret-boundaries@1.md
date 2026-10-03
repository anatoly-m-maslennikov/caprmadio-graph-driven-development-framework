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
---
# Enforce least authority and secret boundaries

MCP must grant each projected capability no more authority than its source Tool requires and must preserve all Tool authorization and permission checks. Credentials must remain bound to their admitted transport and resource, and secrets must not appear in Tool discovery, model-readable results, diagnostics, logs, progress messages, or generated registries.
