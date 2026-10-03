---
atom_id: CA-R-838
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 12
updated_at: "2026-09-14 23:34:13 +0000"
relations:
  child_of:
    - CA-R-833
---
# Validate the normative-authority hierarchy

validators **must** construct the active normative-authority subgraph from registered authority-bearing direct relations **and** **must** reject the subgraph **when** **any** authority edge lacks registered typing **or** the directed subgraph **contains** a cycle.
