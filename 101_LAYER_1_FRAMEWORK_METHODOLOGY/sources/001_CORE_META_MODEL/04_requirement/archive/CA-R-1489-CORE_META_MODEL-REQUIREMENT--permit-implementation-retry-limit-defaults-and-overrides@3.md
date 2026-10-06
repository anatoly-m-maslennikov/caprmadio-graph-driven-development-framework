---
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-R-1488
subjects:
  governs: "Implementation Retry Limit/source"
  depends_on:
    - "Implementation Retry Limit"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Framework Instance Settings"
    - "Property"
cce_version: cce_1
cce_form: obligation
---
# Permit implementation retry-limit defaults and overrides

an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.

- a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
- an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
- a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.
