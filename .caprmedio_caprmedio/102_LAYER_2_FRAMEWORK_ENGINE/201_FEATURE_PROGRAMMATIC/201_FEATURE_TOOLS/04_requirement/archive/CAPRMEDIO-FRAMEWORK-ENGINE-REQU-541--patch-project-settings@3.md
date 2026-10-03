---
subject_scopes:
  - project-settings
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Patch project settings

The framework must provide one deterministic Tool that applies a schema-validated key-level patch to project settings, preserves unrelated values, emits the exact effective diff, and rejects direct edits to values declared as generated.
