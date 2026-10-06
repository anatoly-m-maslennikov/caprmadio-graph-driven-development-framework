---
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
version: 17
updated_at: "2026-09-25 11:32:01 +0000"
relations: {}
atom_id: "CA-M-231"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
global_tier: 11
---
# Summary

Derive Navigation Projections from the CCE Claim

## Claim

an Atom's navigation values **must** be derived from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized first body block under CA-R-1465 **and** CA-M-111.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.

## Details
