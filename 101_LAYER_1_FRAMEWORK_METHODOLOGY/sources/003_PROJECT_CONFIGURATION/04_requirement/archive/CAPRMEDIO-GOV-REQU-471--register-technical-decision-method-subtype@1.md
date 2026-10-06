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
---
# Register Technical Decision as a Method subtype

GOV registers `technical_decision` as a direct subtype of the internal Method
Atom Type.

A Technical Decision selects one bounded technical approach, structure,
algorithm, dependency, protocol, or realization rule from viable alternatives.
It explains the selected approach and applicable tradeoffs without redefining
the required outcome, recording the realized change, or claiming evaluation or
operational results.

The selected technical approach to a refactoring remains a Technical Decision. Its bounded action sequence uses the `refactoring_plan` subtype of Plan. A decision that exists between explicit endpoints uses the relational `integration_decision` Type.

## Rationale

The subtype gives implementation choices a precise home while keeping outcome Requirements, relational Integration Decisions, Refactoring Plans, and concrete Implementations independently replaceable.
