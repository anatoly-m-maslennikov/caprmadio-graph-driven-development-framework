---
subjects:
  governs: "Projection/Type: Terms Graph"
  depends_on:
    - "Governed Term"
    - "Term"
    - "Definition Atom"
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Relation"
    - "Relation Kind"
    - "Projection"
version: 7
updated_at: "2026-10-02 23:17:53 +0400"
relations:
  child_of:
    - CA-R-1335
    - CA-R-1319
    - CA-R-1437
atom_id: "CA-R-1454"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1454-CORE_META_MODEL-GENERAL--derive-governed-terms-views-from-selected-authority.md
  source_atom_id: CA-R-1454
  source_atom_revision: 7
  source_sha256: bab78ca52edb070123af5d40dd61fe4f44cf70941253aeb6aaf9deab0a5283f5
  original_relations_sha256: e1b78d5732a22f1a249523c8a80f9e751fb887dee7a89eaec9dd1b3fc06664b1
---
# Summary

Derive governed Terms views from selected authority

## Scope

governed-only Terms Graph views for a requested source selection.

## Claim

for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319-CORE_META_MODEL-CORE--define-governed-term **and** CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms from Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Kind is admitted for the Terms Graph; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph **and** the source Relation authority under CA-R-1437-CORE_META_MODEL-CORE--keep-one-source-for-each-relation-fact **without** introducing another graph kind **or** independent vocabulary authority.

the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** its Relation Kind authority; a governed-only filter alone does **not** admit another Type.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL-GENERAL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their admitted endpoint classes, graph-qualified Relation authority, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.

## Details
