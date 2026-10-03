---
subject_scopes:
  - project-settings
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 2
updated_at: 2026-08-18 22:44:59
relations:
  child_of:
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Patch project settings

The framework must provide one deterministic Tool that applies a schema-validated key-level patch to project settings, preserves unrelated values, emits the exact effective diff, and rejects direct edits to values declared as generated.
