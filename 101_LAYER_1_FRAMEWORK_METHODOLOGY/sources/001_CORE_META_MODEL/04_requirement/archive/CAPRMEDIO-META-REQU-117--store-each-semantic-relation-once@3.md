---
subject_scopes:
  - artifact-model
version: 3
updated_at: 2026-08-22 00:53:40
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-118--let-the-dependent-atom-own-the-relation
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
    - CAPRMEDIO-META-REQU-643--assign-one-authoritative-owner-to-each-governed-claim
---
# Store each semantic relation once

CAPRMEDIO declares each semantic relation in exactly one Artifact carrier or authoritative Journal event. It must not store an inverse backlink, reciprocal copy, or second representation of the same relation.

Each declared relation kind has exactly one inverse-derived relation kind. Tools and Projections derive the inverse view from the one declaration whenever readers need to traverse the edge in the opposite direction.

Every semantic relation has one declared owner; its inverse view is derived and is never declared separately.
