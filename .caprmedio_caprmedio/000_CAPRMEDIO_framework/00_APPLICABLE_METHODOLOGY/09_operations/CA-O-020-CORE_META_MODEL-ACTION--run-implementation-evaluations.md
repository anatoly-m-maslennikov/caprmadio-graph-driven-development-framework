---
atom_id: CA-O-020
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Evaluation"
  depends_on:
    - "Action"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Implementation"
    - "Artifact/Revision"
version: 5
updated_at: "2026-10-04 15:15:47 +0000"
relations:
  relates_to:
    - CA-O-018
    - CA-O-089
    - CA-O-090
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-020-CORE_META_MODEL-ACTION--run-implementation-evaluations.md
  source_atom_id: CA-O-020
  source_atom_revision: 5
  source_sha256: 13aea0488ac7b230becf1739bd7ad6f29e5f964f0db1e4e1b680aac3b5f59051
  original_relations_sha256: 2146528c15a6ec96b4d49adc2b754f10d06b1d499506b67dafcf2d217de4758d
---
# Summary

Run implementation Evaluations

## Operation

Implementation Evaluation **means** the Agentic Action that executes the selected applicable checks against the current candidate **and** returns their actual results.

- inputs: the selected Plan, current candidate, admitted checks **and** commands, complete test inputs, current R/E/D **and** Method bindings, execution phase, **and** retained issue **and** regression evidence.
- run available checks, including baseline tests, regression tests, **and** required end-to-end tests. preserve failed, blocked, unevaluated, **and** stale outcomes; never replace execution with preparation **or** a remembered result.
- bind output **and** failure evidence **to** the actual candidate, commands, inputs, test definitions, **and** governing baseline. distinguish the initial pre-implementation run from a repair verification run.
- return `passed` **only** for complete current coverage with no failed **or** blocked checks; return `failed` with the available failure evidence; return `blocked` for missing execution prerequisites **or** untrustworthy/incomplete execution evidence. do **not** classify a failure as a code defect merely from the nonzero exit code.

## Details
