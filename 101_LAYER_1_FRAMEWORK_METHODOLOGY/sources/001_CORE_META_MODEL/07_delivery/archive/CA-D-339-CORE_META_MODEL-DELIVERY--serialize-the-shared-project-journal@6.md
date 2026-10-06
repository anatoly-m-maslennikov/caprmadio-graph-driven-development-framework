---
atom_id: CA-D-339
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Journal/Carrier
  depends_on:
    continuant:
      - Journal
      - Project
      - Work Journal
version: 6
updated_at: "2026-09-10 22:35:50 +0400"
relations:
  relates_to:
    - CA-D-308
    - CAPRMEDIO-META-REQU-158
---
# Serialize the shared Project Journal

the shared Project Work Journal **must** serialize its ordered Records as append-only NDJSON File Carrier segments **in** its registered Project-wide Journal directory. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, **or** workflows.
