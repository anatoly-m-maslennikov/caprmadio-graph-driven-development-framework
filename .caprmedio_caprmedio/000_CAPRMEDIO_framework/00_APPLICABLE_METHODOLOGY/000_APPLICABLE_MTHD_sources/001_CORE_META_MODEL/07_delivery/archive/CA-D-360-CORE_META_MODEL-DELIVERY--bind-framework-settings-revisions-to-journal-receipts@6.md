---
atom_id: CA-D-360
cce_version: cce_1
cce_form: traceability
subjects:
  governs: "Framework Instance Settings/Revision Binding"
  depends_on:
    - "Artifact/Revision"
    - "Work Journal/Record"
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-D-359
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind Framework Settings Revisions to Journal Receipts

the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind to its authoritative TOML Carrier through the canonical completed governed-change Work Journal receipt; absence, ambiguity, **or** mismatch **must** leave its currentness unknown.
