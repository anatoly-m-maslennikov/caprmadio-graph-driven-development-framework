---
atom_id: CA-R-1363
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Atom/Current Scope/Governed Subject Set
  depends_on:
    continuant:
      - Subject
      - Subject Path
      - "Claim-Subject Relation/Kind: GOVERNS"
      - Claim-Subject Relation/Temporal Form
version: 1
updated_at: 2026-09-02 00:35:23 +0400
relations:
  child_of:
    - CA-R-920
    - CA-R-1195
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
---
# Define Governed Subject Set

a Governed Subject Set **means** the unordered set of **all** Subject references **in** an Atom's GOVERNS Claim-Subject Relations with **`>=1`** **and** **`<=2`** members, **`<=1`** member for **every** Temporal Form, canonical identity by Temporal Form **and** canonical Subject Path, **and** no authority **in** authored order.
