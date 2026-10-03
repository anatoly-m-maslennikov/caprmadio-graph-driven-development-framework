---
subject_scopes:
  - session-engine
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-283--initialize-the-session-engine-at-context-boundaries
    - CAPRMEDIO-SPEC-TOOLS-METH-053--isolate-runtime-state-under-caprmedio-runtime
---
# Govern session-engine rehydration

Session-engine rehydration must restore only routing invariants, current scope, applicable settings, compact session state, and references needed to load active authority on demand.
