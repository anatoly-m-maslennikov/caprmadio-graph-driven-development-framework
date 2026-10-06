---
atom_id: CA-R-1428
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Confidence Threshold/source"
  depends_on:
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Task"
    - "Epic"
    - "Property"
    - "Framework Instance Settings"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-R-1427"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Permit confidence-threshold defaults and overrides

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Task Property, an explicit enclosing Epic Property, **or** a Framework Instance Settings default.
