---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Confidence Threshold/source"
  depends_on:
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Hub Atom"
    - "Property"
    - "Framework Instance Settings"
version: 6
updated_at: "2026-09-22 14:41:44 +0000"
relations:
  child_of:
    - "CA-R-1427"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Permit confidence-threshold defaults and overrides

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Hub chain follows `IS_DECOMPOSITION_OF`, **not** Label spelling.
