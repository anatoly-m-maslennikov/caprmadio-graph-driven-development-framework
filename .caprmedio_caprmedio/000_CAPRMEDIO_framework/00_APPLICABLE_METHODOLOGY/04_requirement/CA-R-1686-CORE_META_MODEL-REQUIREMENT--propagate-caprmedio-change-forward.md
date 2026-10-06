---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 23
updated_at: "2026-10-03 02:10:09 +0400"
relations:
  child_of:
    - CA-M-001
atom_id: "CA-R-1686"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1686-CORE_META_MODEL-REQUIREMENT--propagate-caprmedio-change-forward.md
  source_atom_id: CA-R-1686
  source_atom_revision: 23
  source_sha256: 333189beef01b75b1019f45f8fe0512ae4cc9b356029634143e3997b69e08e68
  original_relations_sha256: 2f95e55e3d0a844c858c40eeab601ef29e88bfb9f5c8b9fd17a85ccd2af662a7
---
# Summary

Propagate CAPRMEDIO change forward

## Scope

an accepted upstream change in the ordered layer graph.

## Claim

the change propagates **only** forward through the ordered layer graph. it:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation **to** the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

## Details

refreshing a Projection alone does **not** complete propagation. downstream Method, Evaluation, Delivery, Implementation, **and** Operations remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
