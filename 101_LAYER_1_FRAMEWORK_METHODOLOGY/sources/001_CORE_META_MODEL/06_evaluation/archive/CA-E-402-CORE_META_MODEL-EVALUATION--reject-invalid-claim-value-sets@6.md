---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Claim Value Set Validation"
  depends_on:
    - "Atom/Claim"
    - "Claim Value Set"
    - "Property"
    - "Subject Expression"
    - "IS_ALLOWED_VALUE_OF"
version: 6
updated_at: "2026-09-10 05:21:58 +0400"
relations:
  evaluation_for:
    - CA-R-1359
    - CA-M-237
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Claim Value Sets

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
