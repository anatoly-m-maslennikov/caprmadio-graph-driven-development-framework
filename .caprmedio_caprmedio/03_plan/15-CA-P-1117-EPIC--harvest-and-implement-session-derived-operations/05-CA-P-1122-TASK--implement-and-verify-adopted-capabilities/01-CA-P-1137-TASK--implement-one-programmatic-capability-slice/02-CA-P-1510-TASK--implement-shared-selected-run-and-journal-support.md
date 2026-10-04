---
atom_id: CA-P-1510
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Selected Workflow implementation delivery"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 23:57:02 +0400"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement shared selected run and journal support

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1493/P1502 accepted shared R1821–1824,E541–544,D527–529 current Versions; J01–J08, current work_journal API and its compatibility tests.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py; work_journal.py; dedicated tests/test_selected_run_support.py and schema-v5 Journal tests. No domain route policy or another Workflow executor.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Test-first golden mock execution then implement D527 exact preview/execute request/result sealing/currentness and explicit exact approval; distinct WF/Step/Action Run provenance; immutable schema5 Journal backward-compatible v4; original-context/globalID append recovery and one receipt without effect replay. Expose one small non-executable shared runtime tracker/service and publish its Python API immediately for parallel consumers. Results cannot be complete without actual required durable receipts. Add safe context/author/date rollover/conflicting-id tests.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests -p 'test_selected_run_support.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Implementation result

Implemented the non-executable shared `RunTracker` service in
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py` and
the compatible schema-v5 extension in `work_journal.py`.

- `RunTracker.run_selected_operation(request)` seals the preview contract,
  rejects unknown or shadow manifest fields and request-ID byte changes, checks
  injected selected-route currentness, and requires exact preview-bound current
  authorization for `execute`.
- Its injected executor receives a lazy `RunExecutionSession`, whose
  `start_run`/`finish_run`/`note_effects`/`recover` methods record only actual
  invocations. A durable accepted-dispatch carrier rejects an exact execute
  replay after restart; recovery can append only its preserved pending event.
  A requested Workflow ID is preserved as its actual outer Run ID; uninvoked
  branches receive no Run or Event. An executor exception records only started
  work as `interrupted_pending`, rather than claiming completion.
- Schema-v5 `workflow_execution` records distinct Run/definition/Initiative
  provenance and truthful admitted outcomes. The Journal now seals append
  context, finds Event IDs globally across partitions and receipts, retains
  pending immutable bytes/context, and retries only that original append.

Changed files:

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_selected_run_support.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_work_journal_schema_v5.py`

Test-first baseline: the required selected-run discovery command initially
failed with `ModuleNotFoundError: workflow_run_support`, before the service was
created. Final development-worker proof used the mounted `/project` code:

```text
docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests -p 'test_selected_run_support.py' -v
# 7 tests: OK
docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests -p 'test_work_journal_schema_v5.py' -v
# 1 test: OK
```

The selected-run tests prove read-only preview, exact execute admission,
outer-Workflow identity preservation, skipped-branch non-materialization,
executor-exception interruption, stale/currentness refusal, manifest shadow
rejection, durable schema-v5 receipts, post-fsync receipt reconciliation,
date/timezone rollover context reuse, and global collision refusal without
effect replay. They additionally cover no-op, confirmed-zero-effect failure,
cancellation, partial effects, an exception after observed effects, and a
restart replay that remains blocked before and after one identical recovery.

Not yet covered here: integration of a configured `RunTracker` instance into
the selected queue, MCP, and reversal adapters; all thirteen real route
executors; and fresh immutable-image proof. Those are separate packets and are
not claimed by this result.
