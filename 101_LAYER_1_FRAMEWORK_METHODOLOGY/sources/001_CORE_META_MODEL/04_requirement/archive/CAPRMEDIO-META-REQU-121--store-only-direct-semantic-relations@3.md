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
---
# Store only direct semantic relations

An Atom declares a relation only when that relation expresses an immediate semantic dependency, explanation, realization, evaluation, evidence, resolution, control, or other registered meaning between the two endpoints. Here `immediate` distinguishes an authored edge from transitive reachability; it is independent of the declared versus inverse-derived direction of a relation pair.

CAPRMEDIO derives transitive lineage and reachability from chains of direct relations instead of copying every ancestor relation into every descendant.

Declared relations represent immediate semantic edges; transitive lineage is derived.
