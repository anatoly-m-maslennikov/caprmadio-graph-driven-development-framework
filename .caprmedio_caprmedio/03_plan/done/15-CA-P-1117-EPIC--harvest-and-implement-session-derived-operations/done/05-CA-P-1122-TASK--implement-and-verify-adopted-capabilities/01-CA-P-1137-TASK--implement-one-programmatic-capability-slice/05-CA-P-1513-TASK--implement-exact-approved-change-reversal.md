---
atom_id: CA-P-1513
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Selected Workflow implementation delivery"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-04 19:12:21 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement exact approved change reversal

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1496/P1505 accepted R1833–34/E553–54/D536–37, O130/O131/O132 and shared D527/528.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/revert_changes.py and sibling tests/test_revert_changes.py, only exact native adapter integration if needed. No shared Journal or orchestrator changes.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Test-first real temporary effects then approved exact reversal manifest admission/currentness/order/history. Before-dispatch admit is no Run; actual O131 Action uses shared Run tracker. Stop safely on cancellation/failed/partial/uncertain effects with precise completed/unattempted evidence; no automatic inverse/replay. Same-event recording retry has no repeated effects. Export action-level callable for real one-Step Workflow and standalone invocation, canonical request/receipts.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/tests -p 'test_revert_changes.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Implementation result (2026-10-04)

Implemented the bounded native CA-O-131 adapter at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/revert_changes.py`.
Its public `RevertChangesService.handle` and standalone
`apply_approved_reversal` accept only strict `admit`, `execute`, and
`recover_recording` modes. Admission is mutation-free and seals a deterministic
manifest. Execution uses injected governed effect, currentness/revalidation, and
shared Run/Journal collaborators; it applies approved effects in order, retains
exact effect accounting, stops at failure/uncertainty/cancellation, and never
performs inverse, replay, reset, or history deletion. The same pending-recording
event is reconciled through the shared tracker without effect replay.

Initial red command: the prescribed Docker unittest command failed with
`ModuleNotFoundError: No module named 'revert_changes'` before the entrypoint
existed. Final command: `docker exec -i -w /project
caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s
102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/tests
-p 'test_revert_changes.py' -v` passed 8 tests, including a real temporary-file
two-effect reversal, no-op, stale reference, ordering, cancellation, timeout,
and recording-retry cases. `git diff --check` is clean for the owned package.

Continuation result: adapted the Action to P1510's lazy shared-session API via
`execute_with_session(manifest, session, requested_action_run_id)` and
`recover_recording_with_session(...)`. The Action starts/finishes only its
generated Action Run; the caller retains Workflow/Step lineage and graph
continuation. A real temporary Project test now proves shared preview, admitted
execute, canonical schema-v5 Journal events, transient terminal append failure,
and canonical pending-event-only recovery with no effect replay (10 tests
passing). Direct selected-queue/MCP registration remains P1517/P1518-owned;
P1519 owns immutable-image/all-route proof and neither is claimed here.
