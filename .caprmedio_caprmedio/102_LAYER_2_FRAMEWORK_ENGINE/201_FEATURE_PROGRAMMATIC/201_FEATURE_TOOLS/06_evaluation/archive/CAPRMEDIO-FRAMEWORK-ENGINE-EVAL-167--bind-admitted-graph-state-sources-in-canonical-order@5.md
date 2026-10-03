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
# Bind admitted Scope Unit Graph sources in canonical order

## Test case

**Fixture:** Provide multiple admissible active `project_scope_unit_graph` or
`project_graph_state` contributions, then discover the carriers in different
filesystem orders.

**Expected result:** Every run emits the same Project Scope Unit Graph and
Sources Projection bindings in canonical source-identity order, with no
contribution treated as a project-selected setting.
