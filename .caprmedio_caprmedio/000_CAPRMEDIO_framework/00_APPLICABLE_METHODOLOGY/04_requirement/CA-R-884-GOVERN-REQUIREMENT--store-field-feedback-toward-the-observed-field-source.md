---
atom_id: CA-R-884
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Field Feedback Relation
  depends_on:
    continuant:
      - FIELD
version: 8
updated_at: 2026-09-04 23:11:19 +0400
relations:
  child_of:
    - CA-R-295
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CA-R-884-GOVERN-REQUIREMENT--store-field-feedback-toward-the-observed-field-source.md
---
# Store Field Feedback toward the Observed FIELD Source

**every** stored `field_feedback` relation **must** point from its owning Atom to the exact FIELD Scope Unit **or** FIELD-owned Atom that supplied the observation.
