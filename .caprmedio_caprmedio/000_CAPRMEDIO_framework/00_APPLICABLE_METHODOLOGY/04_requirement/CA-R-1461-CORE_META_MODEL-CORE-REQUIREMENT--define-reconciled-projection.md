---
subjects:
  governs: "Projection/Type: Reconciled Projection"
  depends_on:
    - "Projection"
    - "Type"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Carrier"
    - "Operator"
version: 5
updated_at: "2026-10-01 21:41:08 +0400"
relations: {}
atom_id: "CA-R-1461"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1461-CORE_META_MODEL-CORE-REQUIREMENT--define-reconciled-projection.md
---
# Summary

Define Reconciled Projection

## Scope

the Reconciled Projection Type value under Projection.

## Claim

Reconciled Projection **means** the Type value under Projection whose instances preserve selected source content, canonical identities, **and** exact final selected Revisions **without** synthesis **or** merge, **and** have no unresolved source conflict under the applicable declared checks.

## Details

source selection **and** conflict resolution remain governed by applicable source authority. **any** needed source correction **must** be separately authorized by the Operator **and** applied upstream **to** that authority, **not** by editing the projected content **or** treating projection production as authorization **to** change a source. a result **must not** be published as a Reconciled Projection **until** its final selected source Revisions have been re-evaluated **after** **any** such correction **and** no conflict remains unresolved under those checks. this classification does **not** grant the result independent source authority **or** determine its Carrier materialization strategy.
