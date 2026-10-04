---
subjects:
  governs: "Owned Atoms"
  depends_on:
    - "Atom"
    - "Scope Unit"
    - "Atom Collection"
version: 8
updated_at: "2026-10-02 23:17:53 +0400"
relations: {}
atom_id: "CA-R-1447"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1447-CORE_META_MODEL-GENERAL--define-owned-atoms.md
---
# Summary

Define Owned Atoms

## Scope

the ownership of Atoms by Scope Units.

## Claim

Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.

## Details
