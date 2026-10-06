---
atom_id: CA-D-308
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Journal/Carrier
  depends_on:
    continuant:
      - Journal/Record
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Serialize Journals as Append-Only Carriers

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
