---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 14
updated_at: "2026-10-02 21:30:43 +0400"
relations: {}
atom_id: "CA-R-1204"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification.md
  source_atom_id: CA-R-1204
  source_atom_revision: 14
  source_sha256: f57d56dab2cff12ea38a94900a1f146e40ead39f0af9e26e3130e9867f290dda
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use Subject Path Slash Only for Bearer Qualification

## Scope

a Subject Path.

## Claim

**in** a Subject Path, `/` **must** express **only** **`=1`** IS_BORNE_BY edge from the following Dependent Entity occurrence **to** the immediately preceding qualified Entity occurrence.

## Details
