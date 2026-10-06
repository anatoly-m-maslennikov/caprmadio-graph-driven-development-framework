---
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface
---
# Register Refactoring Plan as a Method subtype

GOV registers `refactoring_plan` as a direct subtype of the internal Method
Atom Type.

A Refactoring Plan selects one bounded, independently replaceable strategy for
changing an existing realization while preserving its declared behavior and
other applicable obligations. It identifies the target, preservation boundary,
intended structural transformation, applicable constraints, evaluation needed,
and stop conditions. Independently replaceable transformations require sibling
Refactoring Plan Atoms rather than one compound plan.

A behavior or outcome change is governed by a separate Requirement Atom. A
Refactoring Plan may implement that Requirement, but it must not hide the
behavior change inside a refactoring claim.

## Rationale

Refactoring needs an accepted Method before implementation begins, while the
single-claim boundary prevents a broad plan from becoming an overlapping
container for unrelated transformations or hidden behavior changes.
