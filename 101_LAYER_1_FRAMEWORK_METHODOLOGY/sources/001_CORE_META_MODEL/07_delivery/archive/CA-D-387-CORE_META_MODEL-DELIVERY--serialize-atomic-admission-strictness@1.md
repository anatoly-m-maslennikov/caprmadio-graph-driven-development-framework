---
atom_id: CA-D-387
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    continuant:
      - "Framework Instance Settings"
version: 1
updated_at: "2026-09-10 20:54:17 +0400"
relations: {}
---
# Serialize Atomic Admission Strictness

the Framework Instance Settings TOML Carrier **must** encode atomic admission strictness as `creation_strictness` **in** `[artifacts]`, using the allowed values **and** default governed by CAPRMEDIO-GOV-REQU-302.
