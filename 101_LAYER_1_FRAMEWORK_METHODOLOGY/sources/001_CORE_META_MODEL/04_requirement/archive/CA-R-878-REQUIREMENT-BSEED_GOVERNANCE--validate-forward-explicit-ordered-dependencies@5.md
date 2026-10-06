---
subject_scopes:
  - relation-model
version: 5
updated_at: 2026-08-22 06:00:00
relations:
  child_of:
    - CA-R-914
    - CA-R-915
    - CA-R-916
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Validate forward explicit ordered dependencies

GOVERNANCE validators must evaluate only declared `depends_on` edges between peer ordered Scope Units. They must reject an edge unless it flows from a lower Local Order to a higher Local Order, permit the flow to skip positions, and never synthesize a dependency from order alone. For a Demand For Atom between those peers, the Claim Scope must have a lower Local Order than the Current Scope.
