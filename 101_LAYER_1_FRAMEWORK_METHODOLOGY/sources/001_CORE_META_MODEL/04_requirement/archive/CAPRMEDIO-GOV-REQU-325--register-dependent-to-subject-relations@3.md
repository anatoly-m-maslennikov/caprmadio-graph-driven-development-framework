---
subjects:
  - relation-model
  - atom-boundary
version: 3
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-480--register-rationale-for-relation
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-119--create-rationale-after-its-subject
    - CAPRMEDIO-META-REQU-120--keep-analysis-optional-before-specification
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register dependent-to-subject relations

GOVERNANCE registers the following directed relations. The artifact on the left stores the relation to its pre-existing subject on the right:

| Relation | Owning artifact | Allowed target |
| --- | --- | --- |
| `derived_from` | internal Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, or Rationale Atom | source Analysis Atom |
| `rationale_for` | Rationale Analysis Atom | Requirement, Method, Evaluation, or Delivery Atom |
| `method_for` | Method Atom | Requirement Atom |
| `evaluation_for` | Evaluation Atom | Requirement or Method Atom |
| `delivery_for` | Delivery Atom | Requirement or Method Atom |
| `implementation_of` | governed Implementation carrier | specification Atom |
| `evidence_for` | Evidence carrier | Evaluation or Implementation carrier |
| `concern_about` | Concern Atom | Observation or another directly affected artifact |

Each relation is persisted only by its owning artifact. Inverse navigation is derived and must not be stored as a backlink. An artifact may store both `derived_from` and another registered relation when they express different direct facts, such as a Rationale derived from an Analysis Report and explaining a Requirement.

The registered relations do not imply transitive links. Additional relation meanings require separate GOVERNANCE authority rather than reuse of the nearest-sounding relation.
