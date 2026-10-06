---
subjects:
  governs: "Dependency Order Derivation"
  depends_on:
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Artifact/Revision"
    - "Artifact"
    - "Atom/Content Role: Plan/Type: Plan"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-120
atom_id: "CA-M-239"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-239-CORE_META_MODEL--derive-dependency-order-from-explicit-edges.md
  source_atom_id: CA-M-239
  source_atom_revision: 11
  source_sha256: 287f47cd2fcf0ed1b4090a376b3924a6aa3e45838d837fbcea306b8e46a81ad6
  original_relations_sha256: 6caffda397ba31ac9d7c64190643f433aa17c7879565aa7ba74ffaca9b33bc94
---
# Summary

Derive Dependency Order from Explicit Edges

## Scope

non-Plan Artifact dependency order derivation from explicit edges.

## Claim

**to** derive one non-Plan Artifact dependency order, the resolver **must**:

1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
2. derive its `required_by` inverse view **without** authoring inverse edges;
3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
4. reject a cycle.

the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.

## Details

Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
