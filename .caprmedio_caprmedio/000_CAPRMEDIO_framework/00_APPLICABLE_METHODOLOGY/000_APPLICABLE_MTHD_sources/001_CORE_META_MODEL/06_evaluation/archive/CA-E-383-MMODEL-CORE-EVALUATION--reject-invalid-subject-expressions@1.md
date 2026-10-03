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
      - Subject Expression
version: 1
updated_at: 2026-08-28 22:12:45 +0400
relations: {}
---
# Reject Invalid Subject Expressions

the Evaluation **must** reject a Subject Expression **if** `/` does not encode one valid bearer edge, `:` does not assign one allowed value, a Dependent Entity occurrence lacks one immediate bearer, a reusable Term is rejected only for changing ordinal position, a Governed Term segment begins with a lowercase letter, an Entity name contains `/`, or a registered CCE Operator is redefined as a Governed Term or Scope Unit Name.
