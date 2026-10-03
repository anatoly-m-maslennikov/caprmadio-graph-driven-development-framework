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
version: 9
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Validate Generated-Only Provenance Boundary

Generated-Only Provenance Validation **must not** pass **if** a generated-only Git Commit contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input.
