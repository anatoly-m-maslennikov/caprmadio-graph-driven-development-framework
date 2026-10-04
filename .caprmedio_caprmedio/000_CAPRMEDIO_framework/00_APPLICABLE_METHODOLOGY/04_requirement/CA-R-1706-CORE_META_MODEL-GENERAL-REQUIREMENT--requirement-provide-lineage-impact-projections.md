---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 19
updated_at: "2026-10-03 02:24:19 +0400"
relations:
  child_of:
    - "CA-R-1697"
    - "CA-R-1708"
atom_id: "CA-R-1706"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1706-CORE_META_MODEL-GENERAL-REQUIREMENT--requirement-provide-lineage-impact-projections.md
---
# Summary

Requirement — Provide lineage-impact Projections

## Scope

lineage-impact Projections for changed, replaced, or archived Atom revisions.

## Claim

CAPRMEDIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, **or** archived. the Projection derives the reachable descendant set **without** modifying **or** retargeting **any** persisted relation.

for **every** affected descendant, the Projection identifies the exact earlier revision **in** its lineage, the upstream event that triggered review, **and** the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, **or** confirmed compatible **without** change. unresolved descendants remain visible **until** disposition is recorded through governed history.

the Projection **may** group **and** prioritize work, but it **must not** change an Atom, break a historical link, **or** establish compatibility merely by listing it.

## Primary claim

a changed, replaced, **or** archived ancestor produces a derived review surface for **every** affected descendant while historical lineage remains intact.

## Details
