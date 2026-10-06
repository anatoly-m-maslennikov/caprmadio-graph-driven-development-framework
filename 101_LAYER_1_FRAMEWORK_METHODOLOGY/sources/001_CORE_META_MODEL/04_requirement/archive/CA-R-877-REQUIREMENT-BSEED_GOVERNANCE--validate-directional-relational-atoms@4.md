---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 06:00:00
relations:
  child_of:
    - CA-R-904
    - CA-R-905
    - CA-R-907
    - CA-R-908
    - CA-R-909
    - CA-R-910
    - CA-R-911
    - CA-R-912
---
# Validate Relational Atoms

GOVERNANCE validators must derive every Atom's Current Scope from its carrier and its Claim Scope from the Type-governed filename target or the Current-scope omission. An Atom with different Current Scope and Claim Scope must have Content role Requirement and Type `define_scope_for` or `demand_for`.

Type `define_scope_for` requires the Claim Scope to be a direct child of the Current Scope. Type `demand_for` prohibits an ancestor or non-direct descendant Claim Scope. A Relational Atom must not declare semantic shape, endpoint, controller, follower, or target Content-role metadata.
