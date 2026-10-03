---
atom_id: CA-D-302
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Atom/Scope/Filename Token
  depends_on:
    continuant:
      - Scope Unit/Name
      - Local Configuration
version: 4
updated_at: 2026-09-04 01:04:00 +0400
relations: {}
---
# Serialize Scope Unit References as Filename Tokens

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Local Configuration.
