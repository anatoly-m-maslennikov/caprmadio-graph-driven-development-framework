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
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-387-CORE_META_MODEL-CORE-EVALUATION--reject-invalid-type-assignments.md
---
# Reject Invalid Type Assignments

the Evaluation **must** reject a Type assignment **if** one Entity occurrence has **`>1`** direct Type values, the selected value is not allowed by its most-specific applicable qualified Type Subject, **or** qualified Type Subjects create **`>1`** Type Property slots for the occurrence.
