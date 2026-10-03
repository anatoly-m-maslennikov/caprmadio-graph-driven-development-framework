---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-22 21:44:14
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-041--three-level-priority-vocabulary
  check_of:
    - CAPRMEDIO-GOV-REQU-299--effective-priority-conflict-selection
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Effective-priority selection

## Claim checked

Conflict selection derives the governed effective priorities and never chooses
through a tie, incomparable scope, uncertainty, or ineligible external
obligation.

## Applicable conditions

1. Accept stored priority only on Concern Atoms and reject it on Epic, Task, Action Policy, and every other Content role Atom.
2. Accept only stored `high`, `medium`, or `low`.
3. Reject stored `highest`, `critical`, and `deferred`.
4. Apply the strict-ancestor and earlier-layer increments independently and
   together, capped at virtual `highest`.
5. Confirm `ask_always` always asks.
6. Confirm `auto_by_effective_priority` selects exactly one unique eligible
   winner and asks on ties, incomparable scopes, uncertainty, or multiple
   winners.
7. Confirm unsatisfiable external obligations stop rather than auto-resolve.

## Acceptance criteria

Every comparison produces the governed effective priorities and never guesses
through a non-unique or ineligible result.

## Failure disposition

Stop automatic selection, ask the operator, and record a Concern for any
incorrect priority or unauthorized winner.
