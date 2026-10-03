---
subject_scopes:
  - artifact-operations
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-23 15:59:05 +0400
---
# Transition an artifact lifecycle

The framework must provide one deterministic generic Artifact Tool that applies one registered artifact lifecycle transition, lazily creates its permitted destination directory, moves the carrier, updates required metadata and references, and fails closed on an undefined or ambiguous state model.

This Tool owns generic lifecycle-transition mechanics only. `ATOM_ARCHIVE`, `ATOM_PROMOTE`, `ATOM_UPGRADE`, and `CLOSE_ATOM` own their distinct CAPRMEDIO Markdown Atom transition meanings, validation, bulk rules where admitted, and MCP-gated effects; the generic Tool must not become a public alternative for those transitions.
