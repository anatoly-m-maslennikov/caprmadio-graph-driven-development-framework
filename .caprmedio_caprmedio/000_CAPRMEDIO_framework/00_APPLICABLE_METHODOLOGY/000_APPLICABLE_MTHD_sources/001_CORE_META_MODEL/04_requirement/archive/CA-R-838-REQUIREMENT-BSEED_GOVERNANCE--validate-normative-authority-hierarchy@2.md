---
atom_id: CA-R-838
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-22 01:56:15
relations:
  child_of:
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
---
# Validate the normative-authority hierarchy

GOVERNANCE validators must construct the active normative-authority subgraph from registered authority-bearing direct relations and reject it when any authority edge lacks registered typing or the directed subgraph contains a cycle.
