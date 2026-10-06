---
atom_id: CA-E-387
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Type Assignment Evaluation
  depends_on:
    continuant:
      - Entity
      - Subject Expression
      - Type
version: 1
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Reject Invalid Type Assignments

the Evaluation **must** reject a Type assignment **if** one Entity occurrence has **`>1`** direct Type values, the selected value is not allowed by its most-specific applicable qualified Type Subject, **or** qualified Type Subjects create **`>1`** Type Property slots for the occurrence.
