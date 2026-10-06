---
atom_id: CA-R-842
subject_scopes:
  - scope-topology
tier: core
version: 1
updated_at: 2026-08-21 01:38:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-712--define-ordered-unit-structural-kind
    - CAPRMEDIO-META-REQU-715--define-local-order
    - CAPRMEDIO-META-REQU-718--separate-structural-ownership-from-cross-unit-flow
---
# Define ordered upstream unit

An `ordered_unit` has as its `upstream_unit` the peer `ordered_unit` in the same ordered partition with the nearest lower `local_order`. The first unit in an ordered partition has no `upstream_unit`. This derived navigation does not establish Structural parentage or independently grant authority.
