---
atom_id: CA-E-402
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim Value Set Validation
  depends_on:
    continuant:
      - Atom/Claim
      - Claim Value Set
      - Property
      - Subject Expression
      - IS_ALLOWED_VALUE_OF
version: 1
updated_at: 2026-09-01 22:26:54 +0400
relations:
  evaluation_for:
    - CA-R-1359
    - CA-M-237
---
# Reject Invalid Claim Value Sets

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
