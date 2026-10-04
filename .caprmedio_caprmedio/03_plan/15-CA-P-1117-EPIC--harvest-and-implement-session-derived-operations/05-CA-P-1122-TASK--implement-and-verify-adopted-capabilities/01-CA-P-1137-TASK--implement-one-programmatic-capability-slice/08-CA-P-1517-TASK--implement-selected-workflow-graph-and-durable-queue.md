---
atom_id: CA-P-1517
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
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

implement selected workflow graph and durable queue

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1499/D521v3 accepted; R1522/R1523/R1524 and existing DBOS/Agent/Docker adapters; shared D527/528/529 and thirteen-route immutable source-bound graph manifest from MCP lane.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

Existing APPS/WORKFLOW_ORCHESTRATOR/contracts.py, backend.py, orchestrator.py and new selected_execution.py + focused tests/test_selected_execution.py. Preserve BaseRevise engine.py behavior and all existing native Runs; no MCP/shared library/domain module edits.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Test-first mock full graphs then tagged enqueue_selected independent DBOS dispatch/status with prequeue and actualdispatch source/preview/authorization revalidation. Interpret the reviewed derived graph manifest (entry/Step-to-Action/typed On Result conditions), not independent hardcoded Update-to-Replace policy. Invoke actual Step/Action handlers for all13 routes with distinct W/S/A Run identities/shared Journal; closed-frontier/current definition checks. Existing BaseRevise retained. Client disconnect/worker restart/uncertain intent never replay effect. Actual canceled/partial/pending and short/full report refs. Explicit worker start only; generic callbacks for programmatic/Agentic contexts. Publish integration API immediately.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p 'test_selected_execution.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Result

Implemented the tagged `enqueue_selected` carrier and DBOS workflow path in
`APPS/WORKFLOW_ORCHESTRATOR`, isolated from retained Base Revise enqueue state.
`selected_execution.py` freezes the canonical MCP manifest and all Workflow,
Step, Action, source, native Action-call, and requested-Run pins before queue
acknowledgement; rechecks them immediately before dispatch; and retains
request, intent, accepted result, and uncertainty carriers under the existing
selected Run directory. It accepts D547's physical `ordered_steps`,
`source_path`/`digest`, `entry_step`, and typed `on_result` shape (as well as
the small legacy unit fixture) and interprets only manifest-declared entry,
Step-to-Action bindings, and On Result transitions. It does not contain
route-specific successor policy.

The selected executor uses the P1510 shared lazy Run tracker. It starts and
finishes an actual Workflow Run, then only actually traversed Step/Action Runs;
the outer requested Workflow identity remains the DBOS `run_id`. An existing
intent with no accepted result returns `recording_pending` / `interrupted_pending`
without another handler call. Native factories are late-loaded and context
scoped: O067/O128 lifecycle, O015 structural O004/O012/O005/O013/O014,
O016 prompt Actions, O133/O136 graph Actions, and O011 compiler Actions. The
shared O004/O005 binding is selected by Workflow identity, never globally.
`make_revert_action_handler(service)` provides the CA-O-131 session bridge;
the injected Revert service retains its own governed observe/apply capabilities
and finishes the one existing lazy Action Run without a duplicate Journal event.
The built-in O131 entry is a safe pre-effect refusal until that explicit bridge
is registered. `register_implementation_agent(agent)` or the constructor's
`implementation_agent=` supplies the O016 prompt Action callback; no BaseRevise
Agent response is misrepresented as an implementation-prompt response.

Changed files:

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/contracts.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/backend.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/selected_execution.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_execution.py`

Verification in `caprmedio-ea535e2c0d4e-worker-1`:

- Initial golden baseline failed as expected: `ModuleNotFoundError: selected_execution`.
- `python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p 'test_selected_execution.py' -v` passed eleven tests: stale manifest rejection before dispatch, dispatch-time source recheck, graph-driven traversal with distinct actual identities, shared Journal evidence, retained uncertain intent with no replay, rejection of an undeclared result transition, all-thirteen physical D547 validation and prequeue freezes, all bound Action handler availability, physical D547 Update traversal, and the no-duplicate-run Revert session bridge.
- A no-write `compile()` check passed for `contracts.py`, `backend.py`, `orchestrator.py`, and `selected_execution.py`.
- The existing `test_orchestrator.py` run reported its first six tests passing through `test_codex_subprocess_adapter_with_mock_executable`, then exceeded the bounded worker observation window at `test_detached_idle_worker_survives_start_client_exit`; it is not claimed as a full pass.

### Remaining boundary

This Plan remains Active. The repaired physical MCP-owned manifest now passes
current definition/D547 validation and requested-Run prequeue validation for
all thirteen original routes; the source fixture also confirms a built-in,
context-scoped handler entry for every Action ID. Successful CA-O-131 execution
still requires a caller-owned constructed Revert service registered as
`register_action_handler("CA-O-131", make_revert_action_handler(service))`;
the default safely refuses before an effect. Successful O016 execution likewise
requires its compatible prompt Agent registration. O011 only follows exact
native state labels that satisfy a reviewed edge; unsupported correction and
decision paths remain `interrupted_pending` rather than inventing source edits,
approvals, or continuation. No selected Docker/MCP functional claim is made by
this development-worker proof.
