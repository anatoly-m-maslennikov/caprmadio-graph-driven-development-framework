---
subjects:
  governs: "Atom/Governed Subject"
  depends_on:
    - "Atom/Subjects"
    - "GOVERNS"
    - "Subject"
    - "Relation Kind"
    - "Entity"
    - "Atom/Claim"
version: 12
updated_at: "2026-10-02 22:23:29 +0400"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
atom_id: "CA-R-1363"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1363-CORE_META_MODEL-CORE--define-atom-governed-subject.md
  source_atom_id: CA-R-1363
  source_atom_revision: 12
  source_sha256: f897ce81ed4e0d630006ed7f0f382a082204b82bde93664e394d7e31abbf0b12
  original_relations_sha256: cf083fc6909c16047a4a2a96c9a50e03f91fdb6be24a2277a01fa5beff61e7ca
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Entity governed by the Atom's Claim; the Relation **and** its target are distinct.

## Details
