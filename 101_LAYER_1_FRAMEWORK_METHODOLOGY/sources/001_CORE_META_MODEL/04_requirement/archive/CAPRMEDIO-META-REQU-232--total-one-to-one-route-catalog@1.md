---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-221--one-type-per-semantic-route
      - CAPRMEDIO-META-REQU-222--complete-semantic-route-coverage
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-223--streamlined-content-role-cycle
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
---

# Requirement — Keep the semantic route catalog total and one-to-one

Every possible combination of one Revision mode, one Content role, and one
Governance locus has exactly one canonical `artifact_type`.

No semantic route may be empty or occupied by multiple top-level types. Direct
subtypes may refine a canonical type but inherit its complete route and do not
create another top-level occupant.

## Primary claim

The semantic route catalog is total and one-to-one: each route has exactly one
canonical type.

## Rationale

The former occupancy and uniqueness atoms are inseparable halves of one
bijection requirement and therefore have one owner.
