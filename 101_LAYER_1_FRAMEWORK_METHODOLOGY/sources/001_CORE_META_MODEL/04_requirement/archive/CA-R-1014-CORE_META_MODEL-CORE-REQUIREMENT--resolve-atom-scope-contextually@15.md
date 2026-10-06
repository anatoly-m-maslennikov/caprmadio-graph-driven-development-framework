---
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Scope Unit/Scope"
    - "Operator"
    - "Atom/Governed Subject"
    - "Atom/Claim"
version: 15
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-1596
---
# Resolve Atom Scope Contextually

an Atom Scope **must** include its current Scope Unit Scope **or** named Operator fallback, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
