---
atom_id: CA-D-292
cce_version: cce_1
cce_form: grammar
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Goal/Filename"
  depends_on:
    continuant:
      - Operator
      - Project/Scope Unit
version: 5
updated_at: 2026-09-02 03:30:00 +0400
relations: {}
---
# Serialize External Project Goal Filenames

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.
