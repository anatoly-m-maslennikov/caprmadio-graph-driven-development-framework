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
    - "Atom/Claim"
version: 8
updated_at: "2026-09-14 04:00:22 +0400"
relations: {}
---
# Govern Every Defined Term

**every** Definition Atom **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by its Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim establishes that Term's meaning; the other Term components **in** the path are references **to** their own definitions, **not** additional definitions supplied by this Atom.
