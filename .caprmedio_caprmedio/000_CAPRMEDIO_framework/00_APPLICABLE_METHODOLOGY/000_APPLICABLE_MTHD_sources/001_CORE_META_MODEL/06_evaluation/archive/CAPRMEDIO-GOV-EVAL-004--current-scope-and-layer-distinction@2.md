---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-18 02:17:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-022--feature-and-layer-distinction
  check_of:
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-089--current-layer-handoffs
    - CAPRMEDIO-REQU-040--permit-only-forward-layer-dependencies
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Current scope and layer distinction

## Claim checked

An operator can distinguish horizontal scope ownership, nested structural
scope, forward-only layer authority, and an invalid backward dependency.

## Applicable conditions

Representative structures include horizontal peer contracts, forward-only
ordered authority, nested Scope paths, and unavoidable backward dependencies.

## Acceptance criteria

At least 90% of classifications:

- classify horizontal ownership as peer scopes or features;
- classify ordered downstream authority as layers;
- preserve the current META → GOV → SPEC → REALIZATION → RELEASES → FIELD direction;
  and
- treat irreducible backward dependency as a reason to stop claiming a clean
  layer model.

## Failure disposition

Record a Concern for every repeated ambiguity and stop topology-readiness until
the governing distinction or its presentation is corrected.
