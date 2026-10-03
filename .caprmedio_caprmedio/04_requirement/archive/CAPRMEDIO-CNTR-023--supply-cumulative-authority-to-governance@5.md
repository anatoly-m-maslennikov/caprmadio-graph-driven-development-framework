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
    scope_unit: ../GOVERNANCE
    content_role: requirement
  followers:
    - scope_unit: ../METAMODEL
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ../SEMANTICS
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
relations:
  child_of:
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  authority_input:
    - ../METAMODEL
    - ../SEMANTICS
  depends_on:
    - ../SEMANTICS
---
# Supply cumulative authority to GOVERNANCE

GOVERNANCE consumes the complete applicable upstream authority set from METAMODEL and SEMANTICS through the `authority_input` Contract.
