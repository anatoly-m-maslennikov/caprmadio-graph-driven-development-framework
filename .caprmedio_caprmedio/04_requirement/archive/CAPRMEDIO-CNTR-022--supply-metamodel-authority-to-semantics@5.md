---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 5
updated_at: 2026-08-22 01:51:09
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relational_endpoints:
  controller:
    scope_unit: ../SEMANTICS
    content_role: requirement
  followers:
    - scope_unit: ../METAMODEL
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
relations:
  child_of:
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  authority_input:
    - ../METAMODEL
  depends_on:
    - ../METAMODEL
---
# Supply METAMODEL authority to SEMANTICS

SEMANTICS consumes the complete applicable upstream authority set from METAMODEL through the `authority_input` Contract.
