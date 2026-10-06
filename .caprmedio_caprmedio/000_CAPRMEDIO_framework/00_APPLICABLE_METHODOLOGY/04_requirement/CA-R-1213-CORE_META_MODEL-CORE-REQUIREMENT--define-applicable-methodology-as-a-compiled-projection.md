---
subjects:
  governs: "Applicable Methodology"
  depends_on:
    - "Methodology Source"
    - "Atom/Revision"
    - "Projection"
    - "Projection/Type: Reconciled Projection"
    - "Scope Unit"
    - "Atom/Claim"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Carrier"
    - "Atom/Content Role: Delivery"
version: 17
updated_at: "2026-10-02 21:35:09 +0400"
relations: {}
atom_id: "CA-R-1213"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1213-CORE_META_MODEL-CORE-REQUIREMENT--define-applicable-methodology-as-a-compiled-projection.md
  source_atom_id: CA-R-1213
  source_atom_revision: 17
  source_sha256: 6962d60e15445e82bf78866bec337e389b5e1b1cad5a9d830dcf3feb6ec7c7c2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Applicable Methodology as a Compiled Projection

## Scope

Compilation of Applicable Methodology from selected Methodology Source Scope Units.

## Claim

the Applicable Methodology **must** be a non-authoritative Reconciled Projection compiled by direct, content-preserving derivation from current active Atom Revisions **in** selected Methodology Source Scope Units, preserving the selected source Atoms **and** their final selected Revisions unchanged. Applicable Methodology is **not** a Scope Unit **and** **must not** be the Claim Target Scope Unit of a Goal Atom.

direct **and** content-preserving describe this derivation, **not** a Carrier persistence strategy; its Reconciled Projection classification does **not** select such a strategy. trace metadata **may** be added **to** projected Carriers **only** as governed by applicable Delivery authority, **without** changing the source Atom Revision **or** its Claim authority.

## Details
