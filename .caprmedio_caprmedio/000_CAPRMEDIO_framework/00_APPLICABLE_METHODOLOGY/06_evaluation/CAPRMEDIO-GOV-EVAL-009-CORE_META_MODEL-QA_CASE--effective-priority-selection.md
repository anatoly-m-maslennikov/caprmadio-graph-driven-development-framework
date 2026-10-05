---
subjects:
  governs: "evaluation"
version: 19
updated_at: "2026-10-01 21:46:54 +0400"
relations:
  evaluation_for:
    - "CA-D-386"
    - "CA-R-1629"
atom_id: "CAPRMEDIO-GOV-EVAL-009"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-009-CORE_META_MODEL-QA_CASE--effective-priority-selection.md
  source_atom_id: CAPRMEDIO-GOV-EVAL-009
  source_atom_revision: 19
  source_sha256: debf8c3f03344fc462b228052941f60107f165c5d571dfebde4724368c947ada
  original_relations_sha256: cfa35829dc6d9343744fff2321fb2cf02a4f2f8894266ef3fcdb6f460637746e
---
# Summary

Effective-priority selection

## Scope

the following effective-priority selection conditions:

1. accept stored priority **only** on Concern Atoms **and** reject it on **every** non-Concern Content Role Atom.
2. accept **only** stored `high`, `medium`, **or** `low`.
3. reject stored `highest`, `critical`, **and** `deferred`.
4. compare Concern Atoms with equal stored Priority under a selected model that gives them equal comparison results. change **only** their Scope Unit ancestry; confirm that no implicit increment, virtual `highest`, **or** ancestry-based winner appears.
5. confirm that comparison follows the selected model, its effective parameters, **and** its active criteria; an unresolved model **or** unjustified selection asks the Operator.
6. confirm `ask_always` always asks.
7. confirm `auto_by_effective_priority` selects **`=1`** unique eligible winner **and** asks on ties, incomparable scopes, uncertainty, **or** multiple winners.
8. confirm unsatisfiable external obligations stop rather than auto-resolve.

## Claim

conflict selection follows the admissible Operator-selected priority model **without** an implicit ancestry bonus **and** never chooses through a tie, incomparable scope, uncertainty, **or** ineligible external obligation.

## Details

### Acceptance criteria

**every** comparison conforms **to** the selected priority model **without** an implicit ancestry bonus **and** never guesses through a non-unique **or** ineligible result. authority-tier precedence remains separate **and** unchanged.

### Failure disposition

stop automatic selection, ask the Operator, **and** record a Concern for **any** incorrect priority **or** unauthorized winner.
