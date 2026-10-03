---
atom_id: CAPRMEDIO-CNTR-024
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 6
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relational_endpoints:
  controller:
    scope_unit: .
    content_role: requirement
  followers:
    - scope_unit: ../METAMODEL
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ../SEMANTICS
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
    - scope_unit: ../GOVERNANCE
      content_roles: [plan, requirement, method, evaluation, delivery, ops]
relations:
  child_of:
    - CA-R-881
  authority_input:
    - ../METAMODEL
    - ../SEMANTICS
    - ../GOVERNANCE
---
# Supply cumulative authority to CAPRMEDIO

CAPRMEDIO consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, and GOVERNANCE through the `authority_input` Contract.
