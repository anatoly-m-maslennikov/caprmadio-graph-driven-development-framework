---
atom_id: CA-D-367
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Claim/Structural Entity/Carrier
  depends_on:
    continuant:
      - Current-scope Atom
      - Relational Atom
version: 4
updated_at: "2026-09-12 03:06:55 +0400"
relations: {}
---
# Serialize Claim Structural Entity Only for Relational Atoms

a Markdown Atom Carrier **must** omit an explicit Claim Structural Entity **if** its Atom is Current-scope **and** **must** serialize **`=1`** Claim Structural Entity **if** its Atom is Relational.
