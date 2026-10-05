---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Relation Kind"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 10
updated_at: "2026-10-02 21:45:33 +0400"
relations: {}
atom_id: "CA-R-1276"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1276-CORE_META_MODEL-CORE-REQUIREMENT--type-every-direct-subject-reference.md
  source_atom_id: CA-R-1276
  source_atom_revision: 10
  source_sha256: bb383767920b4fd62eb66793d75a639181944250bcf4f3426bb25b49548e93df
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Type Every Direct Subject Reference

## Scope

direct references in an Atom's Subjects Property.

## Claim

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.

## Details
