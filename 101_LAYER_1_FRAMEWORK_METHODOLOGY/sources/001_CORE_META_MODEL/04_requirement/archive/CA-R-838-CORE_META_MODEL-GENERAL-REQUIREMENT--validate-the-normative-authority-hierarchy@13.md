---
atom_id: CA-R-838
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
cce_version: cce_1
cce_form: obligation
version: 13
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-R-833
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate the normative-authority hierarchy

validators **must** construct the active normative-authority subgraph from registered authority-bearing direct relations **and** **must** reject the subgraph **when** **any** authority edge lacks registered typing **or** the directed subgraph **contains** a cycle.
