---
atom_id: CA-P-1701
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Compose frozen Release Action phases"
  depends_on: [Tool, Action, Step, Workflow, Manifest, Journal, Evaluation]
version: 1
updated_at: "2026-10-05 07:12:01 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Compose frozen Release Action phases

## Objective

Within <=15 minutes, compose the accepted Release helpers behind the frozen selected Step/Action boundary.

## Details

After P1700/P1693, own only new RELEASE_VERSION/release_actions.py and tests/test_release_actions.py. Use the exact O164@2 ten Step/Action/phase pairs, strict D560 inputs and accepted helpers; phase comes only from private selected context, never client parameters. Validate the exact root, frozen parameters and Run/Step/Action identity. Keep typed retained phase results tied to the same candidate/Run, observe each actual helper result, stop on partial/failed/stale/unrecorded outcomes, and never fabricate Journal receipts. Preparation is effect-free; compile only the accepted child; staging never selects runtime; promotion uses full suite/image evidence. P1697 is safely pending when approved retention proof is unknown.

Use the existing shared execution Session for Run recording in the later provider integration; this private adapter must not create a second Journal writer. Durable recording-recovery/provider registration is separate required work; an interrupted/unknown private phase must not be implicitly replayed. Golden-first actual disposable pre-image helper effects and explicit mock image callbacks must distinguish mock proof from real Docker/image proof. Unknown phases, mismatched bindings, stale inputs and skipped prerequisites refuse with truthful effects. Preserve all other files and C447/C449 boundaries. If complete composition cannot fit the bound, save exact implemented phase frontier and a bounded required remainder.

## Definition of Done

Save exact API/hashes and focused completed phase/refusal tests, with unfinished provider/recording/image coverage explicit.
