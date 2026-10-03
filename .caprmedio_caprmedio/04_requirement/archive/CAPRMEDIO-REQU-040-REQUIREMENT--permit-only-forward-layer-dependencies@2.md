---
atom_id: CAPRMEDIO-REQU-040
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-001-CORE-REQUIREMENT--keep-nesting-sibling-order-and-navigation-distinct
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
---
# Permit only forward Layer dependencies

Every dependency between Project Layers must point from the Project root or an earlier Layer to a later Layer in the cumulative order.
