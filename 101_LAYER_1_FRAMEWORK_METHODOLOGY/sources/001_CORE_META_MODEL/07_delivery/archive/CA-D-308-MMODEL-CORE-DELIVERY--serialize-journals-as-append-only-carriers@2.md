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
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Serialize Journals as Append-Only Carriers

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
