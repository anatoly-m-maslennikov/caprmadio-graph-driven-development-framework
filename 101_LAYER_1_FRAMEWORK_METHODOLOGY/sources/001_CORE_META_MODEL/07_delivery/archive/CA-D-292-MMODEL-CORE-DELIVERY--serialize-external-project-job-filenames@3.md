---
atom_id: CA-D-292
cce_version: cce_1
cce_form: grammar
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Requirement Type: Job/Filename"
  depends_on:
    continuant:
      - Operator
      - Project/Scope Unit
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Serialize External Project Job Filenames

**every** external Project Job filename **must** match `<OPERATOR_NAMES>-DEFINES_JOB_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.
