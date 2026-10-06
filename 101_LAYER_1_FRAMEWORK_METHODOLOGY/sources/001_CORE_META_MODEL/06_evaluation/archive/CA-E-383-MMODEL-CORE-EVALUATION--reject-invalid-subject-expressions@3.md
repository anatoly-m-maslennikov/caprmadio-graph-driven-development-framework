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
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Reject Invalid Subject Expressions

the Evaluation **must** reject a Subject Expression **if** `/` does **not** encode one valid bearer edge, `:` does **not** assign one allowed value, a Dependent Entity occurrence lacks one immediate bearer, a reusable Term is rejected **only** for changing ordinal position, a Governed Term begins with a lowercase letter, a General Term begins with a capital letter, a Term name **contains** `/` **or** `:`, a complete composite Subject Expression is classified as one Term, **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.
