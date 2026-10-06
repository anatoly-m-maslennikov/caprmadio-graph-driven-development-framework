---
atom_id: CA-R-838
subjects:
  declared:
    continuant:
      - relation-model
  prerequisite:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 7
updated_at: 2026-08-29 01:16:37 +0400
relations:
  child_of:
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
---
# Validate the normative-authority hierarchy

GOVERNANCE validators **must** construct the active normative-authority subgraph from registered authority-bearing direct relations **and** **must** reject the subgraph **when** **any** authority edge lacks registered typing **or** the directed subgraph **contains** a cycle.
