---
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 2
updated_at: 2026-08-18 22:44:59
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-509--govern-session-engine-rehydration-behavior
---
# Persist bounded session-engine state

The framework must persist the minimum project-local session state required to resume routing after context compaction under `.caprmedio_runtime`.
