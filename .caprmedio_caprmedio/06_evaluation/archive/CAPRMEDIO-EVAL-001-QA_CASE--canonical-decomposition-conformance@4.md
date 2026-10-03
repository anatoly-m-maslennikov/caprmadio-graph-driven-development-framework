---
atom_id: CAPRMEDIO-EVAL-001
subject_scopes:
  - authority
version: 4
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-M-001
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
  child_of:
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
---
# Canonical decomposition conformance

## Claim checked

Every canonical decomposition satisfies REQU-002 and REQU-642.

## Check

For each declared axis, enumerate the bounded universe and classify every admissible member. Report any missing universe or axis declaration, unclassified member, multiple same-axis assignments, or forced near match without changing the governed decomposition.

## Acceptance

Pass only when no conformance issue is found.

## Failure

Record each issue as a Concern against the narrowest owning scope.
