---
subject_scopes:
  - session-engine
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-19 16:45:00
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-507--automatically-initialize-the-session-engine
    - CAPRMEDIO-GOV-REQU-371--define-the-bounded-session-state-envelope
---
# Initialize the CAPRMEDIO session

At session start and after context compaction:

1. Discover the owning project and current scope.
2. Load routing invariants, project settings, and compact session state.
3. Validate the canonical routing tree.
4. Resolve applicable active authority on demand.
5. Enter Exploration Mode unless the operator has supplied an executable instruction.
