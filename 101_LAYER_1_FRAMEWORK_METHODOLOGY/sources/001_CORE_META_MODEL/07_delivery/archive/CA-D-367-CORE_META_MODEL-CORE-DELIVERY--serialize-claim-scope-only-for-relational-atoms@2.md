---
atom_id: CA-D-367
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Claim/Scope/Carrier
  depends_on:
    continuant:
      - Current-scope Atom
      - Relational Atom
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Serialize Claim Scope Only for Relational Atoms

a Markdown Atom Carrier **must** omit an explicit Claim Scope **if** its Atom is Current-scope **and** **must** serialize **`=1`** Claim Scope **if** its Atom is Relational.
