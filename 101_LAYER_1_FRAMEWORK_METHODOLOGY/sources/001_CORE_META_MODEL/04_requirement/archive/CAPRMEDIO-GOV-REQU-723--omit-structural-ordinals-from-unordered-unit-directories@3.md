---
subject_scopes:
  - carrier-placement
version: 3
updated_at: 2026-08-22 02:24:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-META-REQU-713--define-unordered-unit-structural-kind
    - CAPRMEDIO-META-REQU-720--identify-unordered-units-without-local-order
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Omit Structural ordinals from unordered unit directories

A directory that carries an `unordered_unit` must not encode a `local_order`. It may use a registered numeric carrier prefix, provided that prefix is not interpreted as a Structural ordinal or `local_order`.
