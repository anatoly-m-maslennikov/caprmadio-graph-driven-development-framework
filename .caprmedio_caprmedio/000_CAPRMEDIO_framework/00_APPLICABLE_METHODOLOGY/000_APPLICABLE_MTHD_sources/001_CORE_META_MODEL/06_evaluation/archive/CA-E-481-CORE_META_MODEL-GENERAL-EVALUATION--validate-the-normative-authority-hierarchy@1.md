---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Project/normative authority graph"
  depends_on:
    - "Project"
    - "Relation"
    - "Normative Authority Relation Pair"
version: 1
updated_at: "2026-09-17 03:53:30 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for":["CA-R-833","CA-R-808","CA-R-879"]}
---
# Validate the normative-authority hierarchy

the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.

- the evaluated input is the active normative-authority subgraph selected under its registered direct Relation types. unresolved selection **or** typing **must not** be reported as a conforming hierarchy.
- retain the distinction between declared direct authority edges **and** inverse-derived views under CA-R-808 **and** CA-R-879. an inverse view **must not** become another independently declared edge **in** the cycle check.

this representation-independent criterion does **not** select a graph-construction implementation **or** a concrete test specimen.
