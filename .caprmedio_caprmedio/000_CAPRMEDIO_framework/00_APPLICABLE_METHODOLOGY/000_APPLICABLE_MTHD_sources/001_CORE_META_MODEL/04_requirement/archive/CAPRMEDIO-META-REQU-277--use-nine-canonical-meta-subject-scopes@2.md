---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-17 16:39:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-266--use-one-canonical-subject-scope-per-meta-atom
  child_of:
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
---
# Use nine canonical META Subject scopes

Every active META Atom selects its `subject_scopes` from this closed, ordered
vocabulary:

1. `principles` — framework identity and universal constitutional principles;
2. `semantics` — canonical terms, Content-role meanings, semantic distinctions, and role boundaries;
3. `artifact-model` — artifact forms, Types, properties, claims, and relations;
4. `scope-topology` — structural scopes, levels, labels, Profiles, inheritance, handoffs, and recursive applicability;
5. `authority` — normative ownership, admission, precedence, and amendment;
6. `evaluation` — falsifiability, evidence, verification, uncertainty, and the boundary between authority and observed fact;
7. `lifecycle-traceability` — revisions, dependencies, lineage, replacement, archive, currentness, provenance, Git history, and Journals;
8. `development-flow` — Exploration, candidate promotion, backlog, version, release, and reconciliation; and
9. `framework-boundary` — governed storage, runtime isolation, repository work areas, and bounded self-hosting.

`scope_path` continues to identify structural ownership and Applicability.
`subject_scopes` are layer-local discovery and review classifications and do
not change authority, inheritance, relations, or effective structural scope.

Missing, empty, unknown, duplicate, irrelevant, or fallback Subject scopes fail
META admission and Projection generation. Requirement, Method, Evaluation, and
Delivery Atoms select exactly one value; other Content roles may select one or
more. Extending this vocabulary requires the normal MECE and parsimony gates.
