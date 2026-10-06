---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Claim/Structural Entity"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim/Structural Entity"
    - "Scope Unit"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Label"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1574", "CA-D-367"]}
---
# Default Plan target to the enclosing Scope Unit

a Plan Atom with a containing Scope Unit **and** **without** an explicit Claim Structural Entity **must** use its nearest containing Scope Unit as that target, independently of its decomposition **or** Label; a Hub does **not** become the default Claim target.
