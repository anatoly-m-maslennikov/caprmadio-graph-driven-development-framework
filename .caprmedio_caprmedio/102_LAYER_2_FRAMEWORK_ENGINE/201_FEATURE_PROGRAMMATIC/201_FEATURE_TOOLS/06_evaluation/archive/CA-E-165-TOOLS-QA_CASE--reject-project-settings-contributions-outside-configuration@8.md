---
subjects:
  governs:
    continuant:
      - project-settings
    occurrent:
      - evaluation
version: 8
updated_at: 2026-09-01 23:40:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1070
---
# Reject Project Settings contributions outside Configuration

## Test case

**Fixture:** Add a `project_settings` map to any active Atom other than the
governed Project Configuration Atom.

**Expected result:** Generation fails before either output changes and reports
that current operator-selected settings have a second owner. The sole admitted
contribution map remains `project_scope_unit_graph`.
