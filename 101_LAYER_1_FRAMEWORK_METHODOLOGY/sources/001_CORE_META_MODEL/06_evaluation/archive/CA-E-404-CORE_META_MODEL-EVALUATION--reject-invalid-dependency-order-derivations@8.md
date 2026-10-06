---
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
version: 8
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"evaluation_for": ["CA-R-1026", "CA-R-915", "CA-D-268", "CA-M-239", "CA-R-1580"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Dependency-Order Derivations

the Evaluation **must** reject one derived non-Plan Artifact dependency order **if** a relation endpoint is **not** an admitted non-Plan Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.


Plan blocking **must** be checked separately under CA-E-504; a Plan `BLOCKS` fact **must not** fail merely because it is absent from `relations.depends_on`.
