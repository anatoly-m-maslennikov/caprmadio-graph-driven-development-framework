---
subjects:
  governs: "Projection"
  depends_on:
    - "Implementation"
    - "Spec Content Roles"
    - "Artifact"
    - "Atom"
    - "Projection/Authority"
version: 6
updated_at: "2026-10-04 22:07:54 +0000"
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

non-authoritative view Projections delivered as Implementation outputs.

## Claim

a view Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth for the facts it represents.

- its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.
- its Standard output classification does **not** change the Content Roles, Local Tiers, identities, **or** authority of source Atoms represented inside it.

## Details

This permission concerns delivered views, not a permanent loss of actual-state authority for native Implementation. RMED → using O → I derives a realization of intent; that native I can then be source truth for what actually exists. I → using O → a dependency graph or another view produces a non-authoritative Projection.
