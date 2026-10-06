---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 06:00:00
relations:
  child_of:
    - CA-R-875-REQUIREMENT-BSEED_SEMANTICS--keep-ordered-dependencies-sparse-and-forward
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register the forward dependency relation kind

GOVERNANCE registers `depends_on` with this complete metadata:

| Field | Value |
|---|---|
| Relation family | `dependency` |
| Ordering domain | `dependency_order` |
| Inverse-derived name | `required_by` |
| Declared target position | previous or otherwise earlier provider |
| Inverse target position | later dependent |
| Source class | Scope Unit or Artifact |
| Target class | Scope Unit or Artifact |
| Source lifecycle | active |
| Target lifecycle | active |
| Declaration owner | source relational Atom |
| Cardinality | one or more |
| Authority effect | none |
| Transitive | false |
| Authority modes | strict and casual |
| Status | active |
| Exclusive meaning | The later source depends on the earlier target. |

For ordered peer Scope Units, every `depends_on` target must have a lower Local Order than the source Scope Unit. `required_by` is derived and must not be stored.
