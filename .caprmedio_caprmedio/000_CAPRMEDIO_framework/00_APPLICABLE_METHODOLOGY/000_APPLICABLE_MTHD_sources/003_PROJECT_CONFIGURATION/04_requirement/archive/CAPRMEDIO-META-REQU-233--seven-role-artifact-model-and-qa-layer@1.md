---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-223--streamlined-content-role-cycle
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-201--canonical-layer-definitions
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-232--total-one-to-one-route-catalog
---

# Requirement — Use seven content roles and a downstream QA layer

CAPRMEDIO classifies artifact meaning through seven Content roles:

1. Problem;
2. Analysis;
3. Definition;
4. Method;
5. Evaluation;
6. Implementation; and
7. Observation.

Governance locus remains an independent axis with exactly three values:
`internal`, `external`, and `relation`. Revision mode remains an independent
axis with exactly three values: `atomic`, `append_only`, and `maintained`.
`scope_path` remains structural and is not a semantic axis.

The canonical role-and-locus naming model is:

| Content role | Internal | External | Relation |
|---|---|---|---|
| Problem | Problem | External Problem | Conflict |
| Analysis | Analysis Report | External Analysis Report | Conflict Analysis |
| Definition | Requirement | Constraint | Contract |
| Method | Technical Decision | Implementation Methodology | Integration Decision |
| Evaluation | QA Case | Evaluation Standard | Review Protocol |
| Implementation | Git Commit | External Git Commit | Pull Request |
| Observation | Evidence Record | External Evidence Record | Verification Record |

Every concrete artifact classification resolves through its full
Revision-mode, Content-role, and Governance-locus route. Authority,
provenance, priority, lifecycle, and `scope_path` remain separate metadata.

The ordered framework layers become:

```text
META → GOV → TOOL → SKILL → IMPL → QA → OPS
```

QA owns Test and Eval definitions, maintained QA planning surfaces, executable
checks, evaluation prompts and rubrics, result reconciliation, QA evidence,
and verification. QA derives checks from authoritative Definitions and
observes Implementations; it does not establish product behavior. A failed or
inconclusive check produces new feedback for a later cycle rather than a
backward QA-to-IMPL authority edge.

## Rationale

Separating Evaluation from Method prevents Technical Decisions and QA
definitions from sharing one semantic route. A downstream QA layer also keeps
post-implementation evaluation distinct from implementation construction while
preserving forward-only layer authority.
