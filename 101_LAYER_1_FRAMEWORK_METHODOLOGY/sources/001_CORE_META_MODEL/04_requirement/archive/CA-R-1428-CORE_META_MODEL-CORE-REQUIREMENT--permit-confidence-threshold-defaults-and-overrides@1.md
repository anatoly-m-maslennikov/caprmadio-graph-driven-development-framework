---
atom_id: CA-R-1428
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Confidence Threshold/source"
  depends_on:
    continuant:
      - "Confidence Threshold"
      - "Operator"
      - "Atom/Content Role: Plan/Type: Task"
      - "Epic"
      - "Property"
      - "Framework Instance Settings"
version: 1
updated_at: "2026-09-09 02:24:28 +0400"
relations:
  child_of:
    - "CA-R-1427"
---
# Permit confidence-threshold defaults and overrides

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Task Property, an explicit enclosing Epic Property, **or** a Framework Instance Settings default.
