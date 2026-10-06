---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-22 01:51:09
relations:
  child_of:
    - CA-R-876-REQUIREMENT-BSEED_SEMANTICS--separate-control-dependency-and-result-flow
---
# Register field-feedback relation kind

GOVERNANCE registers `field_feedback` with this complete metadata:

| Field | Value |
|---|---|
| Relation family | `operational_feedback` |
| Ordering domain | `operational_feedback` |
| Inverse-derived name | `feedback_routed_to` |
| Declared target position | upstream |
| Inverse target position | downstream |
| Source class | relational Atom |
| Target class | FIELD Scope Unit or FIELD-owned Artifact |
| Source lifecycle | active |
| Target lifecycle | active |
| Declaration owner | source relational Atom |
| Cardinality | one or more |
| Authority effect | none |
| Transitive | false |
| Authority modes | strict and casual |
| Status | active |
| Exclusive meaning | The source routes observed FIELD meaning to its `relational_endpoints.controller.scope_unit`. |

The relation does not by itself establish a Requirement, improvement decision, or acceptance result.
