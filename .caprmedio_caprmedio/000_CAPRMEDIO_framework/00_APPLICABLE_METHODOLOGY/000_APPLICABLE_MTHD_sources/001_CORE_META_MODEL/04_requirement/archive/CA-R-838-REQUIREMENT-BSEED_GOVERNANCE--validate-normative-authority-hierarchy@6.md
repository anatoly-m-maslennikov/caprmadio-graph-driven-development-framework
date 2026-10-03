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
version: 6
updated_at: 2026-08-23 15:24:07
relations:
  child_of:
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
---
# Validate the normative-authority hierarchy

GOVERNANCE validators MUST construct the active normative-authority subgraph from registered authority-bearing direct relations and MUST reject the subgraph when any authority edge lacks registered typing or the directed subgraph contains a cycle.
