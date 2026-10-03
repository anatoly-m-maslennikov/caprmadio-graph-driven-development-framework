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
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1372-CORE_META_MODEL-CORE-REQUIREMENT--derive-journal-revision-updated-at.md
---
# Derive Journal Revision updated at

every Journal/Revision **must** have **`=1`** derived `updated_at` from its latest accepted Journal entry.
