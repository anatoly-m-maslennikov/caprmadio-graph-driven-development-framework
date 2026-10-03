---
subject_scopes:
  - scope-topology
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions
---
# Own immediate child scopes and Contracts

Every governed structural scope owns the definitions of its immediate child
scopes and the Contracts between those children. PROJECT therefore owns Layer
scopes and inter-Layer Contracts; each Layer owns its Feature scopes and
inter-Feature Contracts.

Each concrete child scope and sibling Contract is a Standard Requirement of
that owner. Deeper descendants remain owned recursively by their immediate
parent scope rather than being duplicated at an ancestor.
