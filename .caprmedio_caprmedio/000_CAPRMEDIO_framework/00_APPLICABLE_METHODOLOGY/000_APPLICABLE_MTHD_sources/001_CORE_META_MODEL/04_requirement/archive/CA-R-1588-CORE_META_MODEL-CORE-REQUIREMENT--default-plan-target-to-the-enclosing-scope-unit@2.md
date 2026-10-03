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
version: 2
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1574", "CA-D-476"]}
---
# Default Plan target to the enclosing Scope Unit

a Plan Atom with a containing Scope Unit **and** **without** an explicit Claim Target Scope Unit **must** use its nearest containing Scope Unit as that target, independently of its decomposition **or** Label; a Hub does **not** become the default Claim target.
