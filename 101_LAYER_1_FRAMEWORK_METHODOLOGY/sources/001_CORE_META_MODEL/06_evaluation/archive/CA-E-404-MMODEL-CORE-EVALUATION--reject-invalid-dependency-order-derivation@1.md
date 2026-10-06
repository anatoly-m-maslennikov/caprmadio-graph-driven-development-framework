---
atom_id: CA-E-404
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Dependency Order Derivation Evaluation
  depends_on:
    continuant:
      - DEPENDS_ON
      - DERIVED_FROM
      - Atom/Direct Relation Serialization
      - Dependency Order Derivation
version: 1
updated_at: 2026-09-01 23:18:00 +0400
relations:
  evaluation_for:
    - CA-R-915
    - CA-D-268
    - CA-D-272
    - CA-M-239
---
# Reject Invalid Dependency-Order Derivations

the Evaluation **must** reject one derived dependency order **if** one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.
