---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Atom/Claim"
    - "Atom/Local Tier"
    - "Methodology Source"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
version: 16
updated_at: "2026-10-03 02:57:13 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-033-REQUIREMENT--preserve-ancestor-core-authority-across-structural-levels
atom_id: "CA-R-1748"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Bound descendant specialization to its structural scope

## Scope

Applicable inherited authority in descendant Scope Units and specializations within their permitted boundaries.

## Claim

applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.

- the specialization **must not** change the parent meaning outside its declared descendant scope.
- ancestor Core authority remains protected under CAPRMEDIO-REQU-033-REQUIREMENT--preserve-ancestor-core-authority-across-structural-levels; a child declaration **or** an override label does **not** grant permission **to** weaken it.
- Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** Local Tier under CA-R-1375-CORE_META_MODEL-CORE--restrict-methodology-source-expansion-to-core-permission. changing the descendant's local rank **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary.

## Details
