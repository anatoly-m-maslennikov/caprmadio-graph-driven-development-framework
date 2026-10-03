---
subject_scopes:
  - scope-topology
tier: core
version: 1
updated_at: 2026-08-22 00:53:40
relations:
  child_of:
    - CAPRMEDIO-META-REQU-712--define-ordered-unit-structural-kind
    - CAPRMEDIO-META-REQU-718--separate-structural-ownership-from-cross-unit-flow
---
# Keep ordered dependencies sparse and forward

An explicit dependency among peer ordered Scope Units may flow only from an earlier unit to a later unit. It may skip intermediate positions, and the relative order of two units does not imply that a dependency exists between them.

For ordered peers `u` and `v`:

`dependency_flow(u, v) implies local_order(u) < local_order(v)`

`local_order(u) < local_order(v) does not imply dependency_flow(u, v)`
