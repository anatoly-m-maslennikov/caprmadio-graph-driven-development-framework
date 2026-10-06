---
atom_id: CA-E-383
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Subject Expression Evaluation
  depends_on:
    continuant:
      - General Term
      - Governed Term
      - Subject Expression
version: 5
updated_at: "2026-09-10 05:28:44 +0400"
relations:
  evaluation_for:
    - CA-R-1194
    - CA-R-1204
    - CA-R-1245
    - CA-R-1322
    - CA-R-1323
    - CA-R-1324
    - CA-R-1325
    - CA-R-1297
---
# Reject Invalid Subject Expressions

the Evaluation **must** reject a Subject Expression **if** `/` does **not** encode one valid bearer edge, `:` does **not** assign one allowed value, a Dependent Entity occurrence lacks one immediate bearer, a reusable Term is rejected **only** for changing ordinal position, a Governed Term begins with a lowercase letter, a General Term begins with a capital letter, a Term name **contains** `/` **or** `:`, a complete composite Subject Expression is classified as one Term, **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.
