---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 01:51:09
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
    - CAPRMEDIO-META-REQU-152--preserve-strict-semantic-distinctions
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register realization input relation kind

GOVERNANCE registers `realization_input` with this complete metadata:

| Field | Value |
|---|---|
| Relation family | `realization_flow` |
| Ordering domain | `realization` |
| Inverse-derived name | `realization_supplied_to` |
| Declared target position | upstream |
| Inverse target position | downstream |
| Source class | relational Atom |
| Target class | Scope Unit, Implementation Artifact, Delivery Artifact, or Ops Artifact |
| Source lifecycle | active |
| Target lifecycle | active |
| Declaration owner | source relational Atom |
| Cardinality | one or more |
| Authority effect | none |
| Transitive | false |
| Authority modes | strict and casual |
| Status | active |
| Exclusive meaning | The target supplies realized Artifacts or enacted outputs required by the source's `relational_endpoints.controller.scope_unit`. |
