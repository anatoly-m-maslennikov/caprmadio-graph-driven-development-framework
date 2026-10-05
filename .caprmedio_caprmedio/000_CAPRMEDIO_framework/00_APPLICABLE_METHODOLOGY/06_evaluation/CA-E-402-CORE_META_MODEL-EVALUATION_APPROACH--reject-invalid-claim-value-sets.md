---
subjects:
  governs: "Claim Value Set Validation"
  depends_on:
    - "Atom/Claim"
    - "Claim Value Set"
    - "Property"
    - "Subject Expression"
    - "IS_ALLOWED_VALUE_OF"
version: 10
updated_at: "2026-10-02 20:03:51 +0400"
relations:
  evaluation_for:
    - CA-R-1359
    - CA-M-237
atom_id: "CA-E-402"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-402-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-claim-value-sets.md
  source_atom_id: CA-E-402
  source_atom_revision: 10
  source_sha256: cffc334a0cfc39cca910ac8893452709ad85be1d34cb4b4bda8d038b7180858b
  original_relations_sha256: 2c0932358549235fdbd296113de13ad2b49d058b029ebdab8919171cb68323a5
---
# Summary

Reject Invalid Claim Value Sets

## Scope

Claim Value Sets.

## Claim

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.

## Details
