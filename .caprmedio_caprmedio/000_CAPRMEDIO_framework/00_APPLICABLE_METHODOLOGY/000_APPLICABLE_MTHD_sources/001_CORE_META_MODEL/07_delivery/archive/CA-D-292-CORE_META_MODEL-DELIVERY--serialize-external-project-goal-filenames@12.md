---
cce_version: cce_1
cce_form: grammar
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal/Filename"
  depends_on:
    - "Operator"
    - "Project/Scope Unit"
    - "Project"
    - "Project Name"
version: 12
updated_at: "2026-09-17 14:12:04 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize External Project Goal Filenames

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.

the `<PROJECT_SCOPE>` component **must** be the exact registered Project Name.
