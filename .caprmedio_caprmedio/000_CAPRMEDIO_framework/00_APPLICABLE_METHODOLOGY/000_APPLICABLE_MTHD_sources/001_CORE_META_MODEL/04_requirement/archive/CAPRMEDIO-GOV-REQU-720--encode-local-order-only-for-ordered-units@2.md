---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-20 03:09:39
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-712--define-ordered-unit-structural-kind
    - CAPRMEDIO-META-REQU-715--define-local-order
---
# Encode local order only for ordered units

Only an `ordered_unit` may encode `local_order`, and that value must be unique within its ordered peer partition at one Structural level.
