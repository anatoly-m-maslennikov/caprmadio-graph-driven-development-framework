---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 6
updated_at: 2026-08-22 02:37:15
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relational_endpoints:
  controller:
    scope_unit: ./FRAMEWORK_ENGINE
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
relations:
  child_of:
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  authority_input:
    - ../METAMODEL
    - ../SEMANTICS
    - ../GOVERNANCE
    - .
    - ./FRAMEWORK_METHODOLOGY
  depends_on:
    - ./FRAMEWORK_METHODOLOGY
---
# Supply cumulative authority to FRAMEWORK_ENGINE

FRAMEWORK_ENGINE consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, GOVERNANCE, CAPRMEDIO, and FRAMEWORK_METHODOLOGY through the `authority_input` Contract.
