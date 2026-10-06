---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Claim/Target Scope Unit/Carrier"
  depends_on:
    - "Atom/Claim/Target Scope Unit"
    - "Current-scope Atom"
    - "Relational Atom"
    - "Atom/Carrier"
version: 1
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923"]}
---
# Serialize Claim Target Scope Unit only for Relational Atoms

a Markdown Atom Carrier **must** omit an explicit Claim Target Scope Unit **if** its Atom is Current-scope **and** **must** serialize **`=1`** Claim Target Scope Unit **if** its Atom is Relational.
