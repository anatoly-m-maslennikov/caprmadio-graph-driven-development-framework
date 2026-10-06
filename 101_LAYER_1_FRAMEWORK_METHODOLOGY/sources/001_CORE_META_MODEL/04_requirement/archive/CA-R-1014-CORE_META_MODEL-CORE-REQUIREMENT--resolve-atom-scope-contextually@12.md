---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Scope Unit/Scope"
    - "Operator"
    - "Atom/Governed Subject"
    - "Atom/Claim/Scope"
version: 12
updated_at: "2026-09-13 02:05:21 +0400"
relations:
  child_of:
    - CA-R-919
---
# Resolve Atom Scope Contextually

an Atom Scope **must** include its current Scope Unit Scope **or** named Operator fallback, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
