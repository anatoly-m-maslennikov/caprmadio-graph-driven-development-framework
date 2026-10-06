---
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
version: 7
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Validate Generated-Only Provenance Boundary

Generated-Only Provenance Validation **must not** pass **if** a generated-only Git Commit contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input.
