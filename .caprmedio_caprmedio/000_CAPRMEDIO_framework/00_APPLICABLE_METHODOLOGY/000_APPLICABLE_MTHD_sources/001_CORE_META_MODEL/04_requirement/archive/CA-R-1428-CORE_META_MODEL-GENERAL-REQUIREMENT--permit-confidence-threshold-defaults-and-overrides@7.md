---
subjects:
  governs: "Confidence Threshold/source"
  depends_on:
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Hub Atom"
    - "Property"
    - "Framework Instance Settings"
version: 7
updated_at: "2026-09-22 14:41:44 +0000"
relations:
  child_of:
    - "CA-R-1427"
---
# Permit confidence-threshold defaults and overrides

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Hub chain follows `IS_DECOMPOSITION_OF`, **not** Label spelling.
