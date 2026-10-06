---
atom_id: CA-E-404
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Dependency Order Derivation Evaluation"
  depends_on:
    - "Artifact"
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Dependency Order Derivation"
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-1026
    - CA-R-915
    - CA-D-268
    - CA-D-272
    - CA-M-239
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Dependency-Order Derivations

the Evaluation **must** reject one derived Artifact dependency order **if** a relation endpoint is **not** an Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.
