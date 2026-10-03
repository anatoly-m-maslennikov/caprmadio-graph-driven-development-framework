---
subject_scopes:
  - relation-model
version: 5
updated_at: 2026-08-22 01:51:09
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
    - CAPRMEDIO-META-REQU-171--separate-structural-levels-from-scope-labels
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register authority input relation kind

GOVERNANCE registers `authority_input` with this complete metadata:

| Field | Value |
|---|---|
| Relation family | `authority_flow` |
| Ordering domain | `normative_authority` |
| Inverse-derived name | `authority_supplied_to` |
| Declared target position | upstream |
| Inverse target position | downstream |
| Source class | relational Atom |
| Target class | Scope Unit or Artifact |
| Source lifecycle | active |
| Target lifecycle | active |
| Declaration owner | source relational Atom |
| Cardinality | one or more |
| Authority effect | supplies applicable normative authority |
| Transitive | false |
| Authority modes | strict and casual |
| Status | active |
| Exclusive meaning | The target supplies authority required by the source's `relational_endpoints.controller.scope_unit`. |

The relation does not make supplied authority a Structural parent or transfer its semantic ownership.
