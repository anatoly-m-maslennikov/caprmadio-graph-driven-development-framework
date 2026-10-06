---
subjects:
  governs:
    continuant:
      - relation-model
    occurrent:
      - evaluation
  depends_on:
    occurrent:
      - runtime
cce_version: cce_1
cce_form: permission
version: 4
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Allow pre-runtime pass only with complete relation coverage

An Evaluation MAY return `pass` before runtime from a Realization Graph only when the Realization Graph declares complete coverage of every relation mechanism required by the Evaluation.
