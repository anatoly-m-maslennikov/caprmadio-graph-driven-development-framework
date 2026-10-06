---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-19 01:11:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706--make-structural-ownership-immediate-recursive-and-typed
---
# Require one immediate owner for each non-root structural unit

Every active non-root Structural unit must declare exactly one immediate owner through one `structural_parent` relation.
