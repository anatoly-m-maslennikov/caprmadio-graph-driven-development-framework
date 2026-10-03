---
subject_scopes:
  - authority
version: 7
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-M-001
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
  child_of:
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
---
# Canonical decomposition conformance

## Claim checked

**every** canonical decomposition satisfies REQU-002 **and** REQU-642.

## Check

For each declared axis, enumerate the bounded universe **and** classify **every** admissible member. Report **any** missing universe **or** axis declaration, unclassified member, multiple same-axis assignments, **or** forced near match **without** changing the governed decomposition.

## Acceptance

pass **only** **when** no conformance issue is found.

## Failure

Record each issue as a Concern against the narrowest owning scope.
