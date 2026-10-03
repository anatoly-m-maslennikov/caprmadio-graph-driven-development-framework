---
subject_scopes:
  - framework-engine-mcp
version: 2
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Enforce least authority and secret boundaries

MCP must grant each projected capability no more authority than its source Tool requires and must preserve all Tool authorization and permission checks. Credentials must remain bound to their admitted transport and resource, and secrets must not appear in Tool discovery, model-readable results, diagnostics, logs, progress messages, or generated registries.
