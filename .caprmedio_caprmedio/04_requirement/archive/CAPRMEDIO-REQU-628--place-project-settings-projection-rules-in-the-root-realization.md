---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-18 03:25:18
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
---
# Place Project Settings Projection rules in the root REALIZATION

The CAPRMEDIO framework repository must own `caprmedio_project_settings_projection_rules.toml` in its root REALIZATION and expose that same carrier through a relative symlink under `.caprmedio/000_caprmedio_framework`.
