---
atom_id: CA-D-292
cce_version: cce_1
cce_form: grammar
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal/Filename"
  depends_on:
    - "Operator"
    - "Project/Scope Unit"
version: 10
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize External Project Goal Filenames

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.
