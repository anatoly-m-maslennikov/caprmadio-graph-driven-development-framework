---
atom_id: CA-R-1279
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Subject/Relation Kind: GOVERNS"
  depends_on:
    continuant:
      - "Definition Atom"
      - "Entity"
      - "Term"
      - "Subject"
      - "Subject Path"
version: 6
updated_at: "2026-09-09 02:44:46 +0400"
relations: {}
---
# Govern Every Defined Term

**every** Definition Atom **must** reference the Entity it defines through its **`=1`** GOVERNS Subject, with the defined Term as the terminal name **in** that reference's Subject Path.
