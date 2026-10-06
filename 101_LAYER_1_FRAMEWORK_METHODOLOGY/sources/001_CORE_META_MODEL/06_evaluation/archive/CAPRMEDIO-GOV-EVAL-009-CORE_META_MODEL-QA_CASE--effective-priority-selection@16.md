---
subjects:
  governs: "evaluation"
version: 16
updated_at: "2026-09-22 14:41:44 +0000"
relations:
  evaluation_for:
    - "CA-D-386"
    - "CAPRMEDIO-GOV-REQU-299"
---
# Effective-priority selection

## Claim checked

conflict selection follows the admissible Operator-selected priority model **without** an implicit ancestry bonus **and** never chooses through a tie, incomparable scope, uncertainty, **or** ineligible external obligation.

## Applicable conditions

1. accept stored priority **only** on Concern Atoms **and** reject it on **every** non-Concern Content Role Atom.
2. accept **only** stored `high`, `medium`, **or** `low`.
3. reject stored `highest`, `critical`, **and** `deferred`.
4. compare Concern Atoms with equal stored Priority under a selected model that gives them equal comparison results. change **only** their Scope Unit ancestry; confirm that no implicit increment, virtual `highest`, **or** ancestry-based winner appears.
5. confirm that comparison follows the selected model, its effective parameters, **and** its active criteria; an unresolved model **or** unjustified selection asks the Operator.
6. confirm `ask_always` always asks.
7. confirm `auto_by_effective_priority` selects **`=1`** unique eligible winner **and** asks on ties, incomparable scopes, uncertainty, **or** multiple winners.
8. confirm unsatisfiable external obligations stop rather than auto-resolve.

## Acceptance criteria

**every** comparison conforms **to** the selected priority model **without** an implicit ancestry bonus **and** never guesses through a non-unique **or** ineligible result. authority-tier precedence remains separate **and** unchanged.

## Failure disposition

stop automatic selection, ask the Operator, **and** record a Concern for **any** incorrect priority **or** unauthorized winner.
