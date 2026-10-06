---
subject_scopes:
  - relation-model
tier: core
version: 2
updated_at: 2026-08-22 01:56:15
relations:
  child_of:
    - CAPRMEDIO-REQU-045--separate-hierarchy-dimensions
    - CAPRMEDIO-META-REQU-718--separate-structural-ownership-from-cross-unit-flow
---
# Separate control, dependency, and result flow

Semantic-control direction, dependency direction, information or result-flow direction, and obligation-bearing direction are independent meanings. A directional relational Atom must declare semantic control through its registered endpoint descriptors and every graph edge through the corresponding registered relation kind. It must not infer one direction from another.
