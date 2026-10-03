---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 7
updated_at: 2026-08-22 02:37:15
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relational_endpoints:
  controller:
    scope_unit: ./OPERATOR_DOCUMENTATION
    content_role: requirement
  followers:
    - scope_unit: ../METAMODEL
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ../SEMANTICS
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ../GOVERNANCE
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: .
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ./FRAMEWORK_METHODOLOGY
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ./FRAMEWORK_ENGINE
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
relations:
  child_of:
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  authority_input:
    - ../METAMODEL
    - ../SEMANTICS
    - ../GOVERNANCE
    - .
    - ./FRAMEWORK_METHODOLOGY
    - ./FRAMEWORK_ENGINE
  depends_on:
    - ./FRAMEWORK_ENGINE
---
# Supply cumulative authority to OPERATOR_DOCUMENTATION

OPERATOR_DOCUMENTATION consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, GOVERNANCE, CAPRMEDIO, FRAMEWORK_METHODOLOGY, and FRAMEWORK_ENGINE through the `authority_input` Contract.
