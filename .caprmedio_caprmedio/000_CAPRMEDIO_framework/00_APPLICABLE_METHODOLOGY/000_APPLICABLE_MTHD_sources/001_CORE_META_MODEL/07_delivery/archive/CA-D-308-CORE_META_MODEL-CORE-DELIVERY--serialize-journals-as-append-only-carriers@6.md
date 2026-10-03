---
atom_id: CA-D-308
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Journal/Carrier"
  depends_on:
    - "Journal/Record"
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Journals as Append-Only Carriers

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
