---
subjects:
  governs: "Atom/Claim/Canonical Signature/Projection"
  depends_on:
    - "Atom/Claim/Canonical Signature"
    - "Carrier"
    - "Atom/Identity"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Atom/Carrier"
    - "CCE"
version: 12
updated_at: "2026-10-05 00:25:37 +0400"
relations:
  child_of:
    - CA-D-266
atom_id: "CA-D-346"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Deliver CCE Canonical Signatures as External Report Projections

## Scope
Canonical Signature Projections for selected source frontiers **and** their external reports.

## Claim

**every** Canonical Signature Projection **must** be delivered as **`=1`** non-authoritative report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom Identity **and** Revision, **every** source expression occurrence, **every** Canonical Signature, **and** **every** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, **or** establish Claim equivalence.

## Details
