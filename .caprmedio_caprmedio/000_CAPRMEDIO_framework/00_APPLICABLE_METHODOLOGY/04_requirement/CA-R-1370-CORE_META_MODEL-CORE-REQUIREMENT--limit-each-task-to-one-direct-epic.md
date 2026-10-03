---
atom_id: CA-R-1370
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Epic Membership"
  depends_on:
    continuant:
      - "Atom Collection/Type: Epic/Direct Membership"
version: 3
updated_at: 2026-09-06 01:45:12 +0400
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-140
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1370-CORE_META_MODEL-CORE-REQUIREMENT--limit-each-task-to-one-direct-epic.md
---
# Limit Each Task to One Direct Epic

**every** Atom with Content Role Plan **and** Type Task **must** be a direct member of **`<=1`** Epic.
