---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-240--atomic-structural-and-subject-scopes
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
      - CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions
      - CAPRMEDIO-REQUIREMENT-117-admit-only-materially-distinct-framework-constructs
      - CAPRMEDIO-REQUIREMENT-120-preserve-bounded-meaning-across-structural-scales
---

# Requirement — Use one canonical Subject scope per META Atom

Every active META Atom declares exactly one singular `subject_scope` selected
from this closed, ordered vocabulary:

1. `principles` — framework identity and universal constitutional principles;
2. `artifact-model` — artifact forms, Content roles, Types, properties, claims,
   and relations;
3. `scope-topology` — structural scopes, layers, profiles, inheritance,
   handoffs, and recursive applicability;
4. `authority` — normative ownership, admission, precedence, and amendment;
5. `evaluation` — falsifiability, evidence, verification, uncertainty, and the
   boundary between authority and observed fact;
6. `lifecycle-traceability` — revisions, dependencies, lineage, replacement,
   archive, currentness, provenance, Git history, and Journals;
7. `development-flow` — Exploration, candidate promotion, backlog, version,
   release, and reconciliation; and
8. `framework-boundary` — governed storage, runtime isolation, repository work
   areas, and bounded self-hosting.

`scope_path` continues to identify structural ownership and applicability.
`subject_scope` is a layer-local discovery and review classification: it does
not change authority, inheritance, or the claim's effective structural scope.
An Atom is cataloged under one Subject scope only. Cross-cutting relevance is
expressed through typed relations rather than multiple Subject scopes.

An unknown, missing, or multiple Subject scope fails META admission and
Projection generation. CAPRMEDIO has no `other`, `misc`, or implicit fallback.
Extending the vocabulary requires the normal MECE and parsimony gates.

Replacing legacy plural `subject_scopes` with the semantically equivalent
singular value is lossless metadata recoding only when the Atom's claim,
`scope_path`, authority, applicability, relations, and lifecycle remain
unchanged.

## Primary claim

Every active META Atom has exactly one canonical `subject_scope` from the eight
value META vocabulary, independently of its structural `scope_path`.

## Rationale

One owning Subject scope gives deterministic discovery and a MECE catalog
without creating physical scope folders or duplicating cross-cutting Atoms.
