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
