---
atom_id: CA-D-360
cce_version: cce_1
cce_form: traceability
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Revision Binding
  depends_on:
    continuant:
      - Artifact/Revision
      - Work Journal/Record
version: 2
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-D-359
---
# Bind Framework Settings Revisions to Journal Receipts

the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind to its authoritative TOML Carrier through the canonical completed governed-commit Work Journal receipt; absence, ambiguity, **or** mismatch **must** leave its currentness unknown.
