---
atom_id: CA-R-838
subjects:
  - relation-model
  - atom-boundary
version: 3
updated_at: 2026-08-23 01:44:00
relations:
  child_of:
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
---
# Validate the normative-authority hierarchy

GOVERNANCE validators must construct the active normative-authority subgraph from registered authority-bearing direct relations and reject it when any authority edge lacks registered typing or the directed subgraph contains a cycle.
