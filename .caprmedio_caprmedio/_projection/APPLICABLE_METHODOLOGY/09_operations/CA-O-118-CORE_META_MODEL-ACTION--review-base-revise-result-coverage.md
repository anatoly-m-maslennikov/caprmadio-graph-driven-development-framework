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
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/RMED_ATOM_REVIEW/CA-O-118-CORE_META_MODEL-ACTION--review-base-revise-result-coverage.md
  source_atom_id: CA-O-118
  source_atom_revision: 1
  source_sha256: 13101b6fa0d46755f25dcbf2c81cb31e8f945be1a0a932dabd36c0b77274ad26
  original_relations_sha256: 0e0a2445b2c035e0671f11f830da82891997aa34348962a7fd52c6d1de7ad708
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
