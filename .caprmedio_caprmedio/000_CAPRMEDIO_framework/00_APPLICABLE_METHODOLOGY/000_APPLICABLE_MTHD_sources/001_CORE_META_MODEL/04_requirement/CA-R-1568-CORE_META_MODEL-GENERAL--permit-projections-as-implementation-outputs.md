---
subjects:
  governs: "Projection"
  depends_on:
    - "Implementation"
    - "Spec Content Roles"
    - "Artifact"
    - "Atom"
    - "Projection/Authority"
version: 5
updated_at: "2026-10-03 00:22:56 +0400"
relations: {"relates_to": ["CA-R-1548", "CA-R-1571", "CA-R-1703"]}
atom_id: "CA-R-1568"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Permit Projections as Implementation outputs

## Scope

Projections delivered as Implementation outputs.

## Claim

a Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth.

- its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.
- its Standard output classification does **not** change the Content Roles, Local Tiers, identities, **or** authority of source Atoms represented inside it.

## Details
