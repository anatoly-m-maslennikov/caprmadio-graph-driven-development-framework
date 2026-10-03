---
subject_scopes:
  - artifact-operations
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Transition an artifact lifecycle

The framework must provide one deterministic Tool that applies one registered artifact lifecycle transition, lazily creates its permitted destination directory, moves the carrier, updates required metadata and references, and fails closed on an undefined or ambiguous state model.
