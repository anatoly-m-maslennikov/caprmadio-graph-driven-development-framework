---
atom_id: CA-O-118
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 15:15:46 +0000"
subjects:
  governs: "RMED Atom Review Workflow/coverage/Action: 118"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
relations:
  relates_to: [CA-O-104]
---
# Summary

Review Base Revise result coverage

## Operation

the Coverage Gate **must** compare saved main-Step results with their explicit expected work **and** return covered **only** at coverage **`=100`** percent.

## Details

- gather: compare the carried ordered selection **and** rule bindings with the frozen request; missing, duplicate, extra **or** unexplained work blocks coverage. an explicit empty selection has no omitted work.
- check: account for **all** selected Atoms **and** **all** **`=6`** required checks with evidence **and** concluded passed **or** failed results. blocked, pending **or** unknown results are missing coverage.
- fix: account for **all** selected Atoms **and** **all** initial findings with applied corrections **or** reasoned rejections. retain initial check evidence; blocked **or** unaccounted findings are missing coverage.
- report expected, covered, missing, coverage percent **and** evidence references. percentages do **not** round incomplete work to **`=100`**.
- incomplete **or** unknown coverage returns ask_operator with an explicit question; preserve completed effects **and** await an Operator decision.
- this Programmatic Action checks accounting, **not** whether an Atom **or** a repair is semantically correct.
