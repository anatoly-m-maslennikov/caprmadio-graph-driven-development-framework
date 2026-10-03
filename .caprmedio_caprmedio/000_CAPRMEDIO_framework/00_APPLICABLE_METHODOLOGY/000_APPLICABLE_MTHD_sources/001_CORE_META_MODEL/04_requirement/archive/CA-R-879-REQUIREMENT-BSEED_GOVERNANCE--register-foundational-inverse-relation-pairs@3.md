---
subject_scopes:
  - relation-model
version: 3
updated_at: 2026-08-22 01:37:40
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register foundational inverse relation pairs

GOVERNANCE registers these foundational declared and inverse-derived relation pairs:

| Ordering domain | Declared relation | Declared target position | Inverse-derived relation | Inverse target position |
|---|---|---|---|---|
| normative authority | `child_of` | upstream | `parent_of` | downstream |
| dependency | `depends_on` | upstream | `required_by` | downstream |
| realization | `implementation_of` | upstream | `implemented_by` | downstream |
| temporal succession | `replaced_by` | downstream | `replacement_of` | upstream |

Only the declared relation is authoritative. Replacement declarations occur in the authoritative Journal and archive history rather than active current-state Atom relations.
