---
atom_id: CAPRMEDIO-GOV-EVAL-010
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Generated-Only Provenance Validation
  depends_on:
    continuant:
      - Git Commit
      - Implementation Relation
      - Projection
version: 10
updated_at: "2026-09-10 05:28:44 +0400"
relations:
  evaluation_for:
    - CA-M-135
    - CAPRMEDIO-META-REQU-657
---
# Validate Generated-Only Provenance Boundary

Generated-Only Provenance Validation **must not** pass **if** a generated-only Git Commit contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input.
