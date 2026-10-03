---
atom_id: CA-R-1372
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Journal/Revision
  depends_on:
    continuant:
      - Journal
version: 3
updated_at: "2026-09-10 06:59:09 +0400"
relations: {}
---
# Derive Journal Revision updated at

every Journal/Revision **must** have **`=1`** derived `updated_at` from its latest accepted Journal entry.
