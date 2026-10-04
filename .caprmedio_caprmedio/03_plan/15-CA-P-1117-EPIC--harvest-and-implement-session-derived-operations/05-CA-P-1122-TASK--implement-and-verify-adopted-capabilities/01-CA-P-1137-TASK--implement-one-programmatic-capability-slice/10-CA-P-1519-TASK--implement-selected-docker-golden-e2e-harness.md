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
updated_at: "2026-10-04 23:56:32 +0400"
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

## Implementation result (partial; not Done)

Added the owned `test_selected_workflows_docker_e2e.py` harness and its
`selected_workflows_docker_fixture.py` disposable corpus helper. The helper
requires the exact current W01--W13 manifest, copies every pinned definition
and selected source registry into one fresh mock-only Project per case, captures
admitted authority snapshots, and supplies a sealed fixture request. It also
copies the existing CA-O-104 readiness binding only because the current Docker
worker refuses readiness without it; that does not turn Base Revise into
selected-route evidence.

The harness has explicit checks for all thirteen read-only previews across MCP
client reconnects, W01 durable enqueue/reconnected-terminal-status/effect/Journal proof, W13 stale-source
rejection without an effect, exact W01--W13/J01--J08 corpus labels, and a
fresh-image compose assertion that `/project/102_FRAMEWORK_ENGINE` is not a
mount. It deliberately fails rather than skips when `CAPRMEDIO_DOCKER_E2E=1`
and the manifest, route registration, shared Run integration, or effect/Journal
proof is absent.

Verification performed:

```text
PYTHONDONTWRITEBYTECODE=1 python -m py_compile \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/selected_workflows_docker_fixture.py \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py
git diff --check -- <the two owned test files>
```

Both passed. An initial exact opt-in Docker baseline reached the disposable mock
runtime, then failed before selected dispatch because the current worker
readiness fingerprint required CA-O-104 and the initial corpus had not copied
that non-selected readiness input. The corpus now copies that one pinned input
and tears down partially started runtimes. That initial failure is retained as
failure evidence, not a selected-route pass.

After that correction, the source-pinned corpus test passed for all thirteen
route labels and all eight Journal labels, and the Compose boundary test passed:
`worker` and `mcp` mount `/project` and read-only `/project/.git`, but no host
`/project/102_FRAMEWORK_ENGINE` implementation mount. Those are harness/config
checks only; neither is Docker functional route evidence. The managed macOS
test environment can deny deletion of freshly bind-mounted fixture paths, so
`CAPRMEDIO_KEEP_DOCKER_FIXTURES=1` retains a uniquely named failed-fixture path
for bounded diagnostics rather than converting fixture-cleanup failure into a
route result.

Remaining before this Plan can be Done: root-owned fresh-image/no-host-code
compose update; current MCP registration and selected queue integration;
concrete route adapters and source-valid W01--W13 parameters/effects; and
functional Docker proof for all happy/no-op/cancel/partial/currentness and
J01--J08 Journal-retry/standalone/nested-lineage cases. No real authority,
native Run, credential, or paid Agent was used.

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.
