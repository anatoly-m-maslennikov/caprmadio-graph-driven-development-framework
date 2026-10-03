---
subject_scopes:
  - artifact-migration
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Apply an artifact migration

The framework must provide one deterministic Tool that applies one approved migration plan only when its recorded preconditions still match, commits all carrier and reference mutations as one rollbackable transaction, and appends the governed migration event through the Work Journal Tool.
