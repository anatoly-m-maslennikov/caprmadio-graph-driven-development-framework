---
atom_id: CA-P-1519
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
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

implement selected docker golden e2e harness

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1492 Done exact tmp/selected_workflows/docker_acceptance.md portfolio W01–W13/J01–J08; current selected RMED/source manifest and route implementations; existing test_docker_e2e.py/runtime.py packaging.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py and selected fixture corpus/harness helpers only. Docker packaging adjustments only if exactly needed for13route dependencies and coordinated with root. No domain/shared/MCP/backend file edits.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Build complete disposable golden mock corpus first and parameterized real Docker/MCP harness for all13 capabilities plus failures/noops/cancel/partial/currentness/immutable Journal retry and standalone/nested lineage. Tests must check actual expected authority/Projection/files/one canonical Event/receipts not acknowledgment. Fresh image/no host implementation mounts; mock Agent actual implementation exercise and client disconnect/reconnect persistence, real queue handles. Record unimplemented failures honestly until integration. Do not operate real Project authority or reuse native Runs; no cost/credential use by inference. Functional image proof after matching mock tests pass, not build-only.

Test-first exact command in the usable Python/Docker environment:

`CAPRMEDIO_DOCKER_E2E=1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p 'test_selected_workflows_docker_e2e.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.
