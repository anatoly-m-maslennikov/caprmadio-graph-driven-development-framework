---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim/Target Scope Unit"
    - "Scope Unit"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Label"
version: 3
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1574", "CA-D-482"]}
---
# Summary

Default Plan target to the enclosing Scope Unit

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.
