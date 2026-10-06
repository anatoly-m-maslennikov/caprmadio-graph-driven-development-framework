---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Entity"
version: 14
updated_at: "2026-10-02 21:30:43 +0400"
relations: {}
atom_id: "CA-R-1202"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once.md
  source_atom_id: CA-R-1202
  source_atom_revision: 14
  source_sha256: a92e1fc6be791e4fa7f5400efde58cd2d07e5b5e5d6f20a65125acb2ddb9de07
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Resolve Every Direct Subject Target Once

## Scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Entity. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.

## Details
