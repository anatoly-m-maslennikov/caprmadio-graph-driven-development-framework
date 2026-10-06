---
subjects:
  governs: "IS_BORNE_BY"
  depends_on:
    - "Primary Entity"
    - "Subject"
version: 10
updated_at: "2026-10-02 22:23:29 +0400"
relations: {}
atom_id: "CA-R-1351"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1351-CORE_META_MODEL-CORE--give-primary-entity-occurrences-no-bearer.md
  source_atom_id: CA-R-1351
  source_atom_revision: 10
  source_sha256: 00232e87adea2761623c07f3fbcb5b6ad455eca840b7793920a99c2c1072fbd2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Give Primary Entity Occurrences No Bearer

## Scope

Primary Entity occurrences referenced by a Subject.

## Claim

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.

## Details
