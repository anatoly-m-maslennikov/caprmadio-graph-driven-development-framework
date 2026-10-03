---
artifact_subtype: implementation_decision
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-042--verbose-semantic-identities
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
      - CAPRMEDIO-GOV-REQU-427--expandable-scope-path-identities
---

# Implementation Decision — Use route-derived identity kinds

Every governed atomic artifact declares one registered `artifact_type` and at
most one direct `artifact_subtype`. The registered pair derives its semantic
route without a second parent-Type hierarchy.

Artifact IDs and filenames use the registered visible identity kind:

| Artifact type | Identity kind |
|---|---|
| `requirement` | `REQUIREMENT` |
| `constraint` | `CONSTRAINT` |
| `contract` | `CONTRACT` |
| `implementation_decision` | `IMPL` |
| `test_plan` | `TEST-CASE` |
| `evaluation_plan` | `EVALUATION-CASE` |

Other registered types use their own unambiguous configured kind. Optional
subtype-bearing names use the subtype kind only when project settings enable
that naming policy. An identity vocabulary change is one complete governed
migration; superseded aliases are not accepted after cutover.

## Primary claim

Artifact identity kinds follow the registered direct artifact type or enabled
direct subtype, not a separate Decision, Question, Problem, or QA parent
hierarchy.

## Rationale

Direct identity kinds remain understandable in file lists and resolve the same
one-to-one semantic route used by validation, without maintaining a parallel
classification system.
