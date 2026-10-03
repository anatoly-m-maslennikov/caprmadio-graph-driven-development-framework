---
artifact_subtype: qa_case
subject_scopes:
  - project-settings
version: 5
updated_at: 2026-08-23 11:39:04
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
contribution maps remain `project_scope_unit_graph` and `project_graph_state`.
