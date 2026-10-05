---
subjects:
  governs: "Claim Value Set"
  depends_on:
    - "Atom/Claim"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 9
updated_at: "2026-10-02 22:23:29 +0400"
relations:
  child_of:
    - CA-R-1270
atom_id: "CA-R-1359"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1359-CORE_META_MODEL--define-claim-value-set.md
  source_atom_id: CA-R-1359
  source_atom_revision: 9
  source_sha256: 26bc473af5b1108bfa751991a56c236437fedc84a0a0cb7e588db0b4eadc0c7c
  original_relations_sha256: 996c38138f0d740a10abf989aca106cdb625bece78fb86564be33d4c8432969d
---
# Summary

Define Claim Value Set

## Scope

Claim Value Set expressions.

## Claim

a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.

## Details
