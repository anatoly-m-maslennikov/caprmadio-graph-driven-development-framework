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
version: 1
updated_at: 2026-09-03 02:06:59 +0400
relations: {}
---
# Derive Journal Revision updated at

every Journal/Revision **must** have **`=1`** derived `updated_at` from its latest accepted Journal entry.
