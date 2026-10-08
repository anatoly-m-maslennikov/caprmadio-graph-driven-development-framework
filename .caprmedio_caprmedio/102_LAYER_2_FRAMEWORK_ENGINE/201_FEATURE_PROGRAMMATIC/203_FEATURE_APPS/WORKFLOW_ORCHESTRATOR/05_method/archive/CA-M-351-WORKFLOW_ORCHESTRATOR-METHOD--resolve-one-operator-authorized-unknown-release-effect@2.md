---
atom_id: CA-M-351
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 03:38:00 +0400"
subjects:
  governs: "Operator-authorized unknown Release effect resolution"
  depends_on: [Release Version, Workflow Run, Step Run, Action Run, Operator, Permission, Journal, Source, Queue, DBOS]
relations:
  method_for: [CA-R-1895]
  relates_to: [CA-M-340, CA-O-164, CA-C-517]
---
# Summary

resolve one Operator-authorized unknown Release effect

## Scope

the one-shot resolution variant of the existing explicit Release recovery endpoint for the exact N15 in-progress closed Unit gate.

## Claim

resolve an unknown Release effect by validating the frozen occurrence and C517-bound Operator decision, then recording one truthful canonical `interrupted` result whose resolution kind is `unknown_effect`, without dispatching, replaying or recovering a pending event.

## Details

1. accept only a request whose exact keys are `operation`, `run_id`, `request_identity`, `authorization_ref`, `authorization_sha256` and `expected_checkpoint_sha256`; require `operation: resolve_release_unknown_effect`, reject every extra/missing key, and preserve ordinary `recover_selected_release` as its existing three-key shape.
2. reopen the exact frozen request, binding, checkpoint and canonical Journal. Derive and verify the snapshot and Workflow/Step/Action pins from CA-R-1895's single registered N15 occurrence and the frozen checkpoint; do not admit duplicate caller assertions. Revalidate source, permission and resolver authority by selecting exactly `[CA-R-1895, CA-M-351, CA-E-594, CA-D-589]` in that order from CA-D-572's JSON `## Unknown-effect resolver authority` block; each pin has exactly `atom_id`, `version`, `source_path`, `digest`. Prove completed indices 0--3 and prove the sole index-4 context remains the stated in-progress occurrence.
3. refuse before any write if a pending original event, typed Unit result, canonical terminal receipt, prior resolution, changed checkpoint, changed binding or competing decision exists.
4. under the existing canonical per-Run/Journal lock, append exactly the existing `interrupted` Action, Step and Workflow facts for the existing occurrence. Their resolution kind/reason says the Unit terminal outcome is unknown; none supplies a pass/fail or fabricates an original Unit receipt.
5. persist one authoritative companion resolution record with literal `schema: release_unknown_effect_resolution_v1`, literal `resolution_kind: unknown_effect`, and exact keys `schema`, `resolution_kind`, `run_id`, `workflow_run_id`, `step_run_id`, `action_run_id`, `old_checkpoint_sha256`, `authorization_ref`, `authorization_sha256`, `approved_authority_pins`, `event_refs` and `unknown_reason`. `approved_authority_pins` has exactly four ordered D572-shape pins `[CA-R-1895, CA-M-351, CA-E-594, CA-D-589]`; `event_refs` has exactly three ordered canonical refs `[Action, Step, Workflow]`. It binds the original checkpoint and approved authority pins, not a caller-provided Unit result. Persist the matching terminal checkpoint as stopped at phase 4 with no in-progress effect and preserve all predecessor facts byte-for-byte.
6. return only one of these closed response variants: `resolved` or `already_resolved`, each with exactly `operation`, `run_id`, `disposition`, `resolution_ref`, `event_refs` and `unknown_reason`; or `blocked`, with exactly `operation`, `run_id`, `disposition` and `blocked_reason`. A repeated identical request returns the original resolution reference and event refs only.
7. do not call Docker, the Unit runner, a generic selected dispatcher, a DBOS replay, promotion, retirement or any later Release phase. Pending append/crash recovery remains limited to original sealed event bytes and must not require old-checkpoint modification to manufacture proof. Do not use raw SQLite history mutation; DBOS is used only through its legitimate API for transport/observation.
