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
version: 2
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CAPRMEDIO-GOV-REQU-302
---
# Serialize Atomic Admission Strictness

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CAPRMEDIO-GOV-REQU-302.
