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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1568-CORE_META_MODEL-GENERAL--permit-projections-as-implementation-outputs.md
  source_atom_id: CA-R-1568
  source_atom_revision: 6
  source_sha256: 91c4576fa27eb3fbec01af55767468bff2de5e91f7f006a9c4cff067ed6fc699
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
