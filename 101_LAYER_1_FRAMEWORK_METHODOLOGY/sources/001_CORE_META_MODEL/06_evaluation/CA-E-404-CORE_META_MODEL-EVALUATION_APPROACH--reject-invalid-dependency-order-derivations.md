---
subjects:
  governs: "Dependency Order Derivation Evaluation"
  depends_on:
    - "Artifact"
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Dependency Order Derivation"
version: 12
updated_at: "2026-10-01 21:25:33 +0400"
relations: {"evaluation_for": ["CA-R-1026", "CA-R-915", "CA-D-268", "CA-M-239", "CA-R-1580"]}
atom_id: "CA-E-404"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
---
# Summary

Reject Invalid Dependency-Order Derivations

## Scope

derived non-Plan Artifact dependency orders.

## Claim

the Evaluation **must** reject one derived non-Plan Artifact dependency order **if** a relation endpoint is **not** an admitted non-Plan Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.

## Details

Plan blocking **must** be checked separately under CA-E-504-CORE_META_MODEL-QA_CASE--validate-plan-blocking-and-parallel-readiness; a Plan `BLOCKS` fact **must not** fail merely because it is absent from `relations.depends_on`.
