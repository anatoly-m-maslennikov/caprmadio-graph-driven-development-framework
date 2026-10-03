---
atom_id: CA-R-1279
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "GOVERNS"
  depends_on:
    - "Definition Atom"
    - "Subject"
    - "Term"
    - "Subject Path"
version: 7
updated_at: "2026-09-13 02:05:21 +0400"
relations: {}
---
# Govern Every Defined Term

**every** Definition Atom **must** reference the Subject it defines through its **`=1`** direct GOVERNS target, with the defined Term as the terminal name **in** that target's Subject Path.
