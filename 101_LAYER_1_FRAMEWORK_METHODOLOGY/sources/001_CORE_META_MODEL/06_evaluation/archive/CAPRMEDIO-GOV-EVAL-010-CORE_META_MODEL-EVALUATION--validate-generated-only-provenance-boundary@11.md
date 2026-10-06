---
atom_id: CAPRMEDIO-GOV-EVAL-010
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Generated-Only Provenance Validation"
  depends_on:
    - "Journal/Record"
    - "Implementation Relation"
    - "Projection"
version: 11
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  evaluation_for:
    - CA-M-135
    - CAPRMEDIO-META-REQU-657
---
# Validate Generated-Only Provenance Boundary

generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
