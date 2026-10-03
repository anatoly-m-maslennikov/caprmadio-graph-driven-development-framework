---
atom_id: CAPRMEDIO-FRAMEWORK-ENGINE-REQU-519
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
---
# Persist bounded session-engine state

The framework must persist the minimum project-local session state required to resume routing after context compaction under `.caprmedio_runtime`.
