---
atom_id: CA-D-302
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Atom/Scope/Filename Token"
  depends_on:
    - "Scope Unit/Name"
    - "Project Configuration"
version: 9
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Scope Unit References as Filename Tokens

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.
