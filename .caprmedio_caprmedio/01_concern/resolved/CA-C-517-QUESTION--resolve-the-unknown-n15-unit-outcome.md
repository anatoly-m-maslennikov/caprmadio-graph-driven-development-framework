---
atom_id: CA-C-517
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 00:30:45 +0000"
subjects:
  governs: "Unknown N15 Unit outcome"
  depends_on: [Operator, Workflow Run, Action Run, Evaluation, Journal, Docker Image, Implementation]
relations:
  concern_about: [CA-P-1117, CA-P-1713, CA-P-1716]
---
# Summary

Resolve the unknown N15 Unit outcome

## Concern

how should the exact N15 Unit Action Run be closed when its host disappears before recording a terminal receipt, without replaying its effect or inferring an exit result from its child report?

## Evidences

- Run: `release-epic-resume-20261006-N15`; snapshot: `3bfdd04e1b9901c97a6af49c59e01731c456ea5313816db657457e94bd35a9f7`.
- the checkpoint retains `in_progress` for Step 5 / Action CA-O-168, with phases 1–4 completed and no pending Journal recording. DBOS still reports PENDING.
- the former host worker was absent at the last permitted process observation. its readiness files are stale; the later managed profile denies process inspection.
- the exact Unit container is now absent. its mounted `coverage.xml` contains 2,011 child test cases: 1,986 successes, 24 failures, one error and no skipped cases. no terminal Unit receipt or independently captured exit code exists.
- retained diagnostic bytes, original paths and hashes are in `.caprmedio_tmp/epic-resume-release/N15/observed-unit-evidence/`. the report is child-test evidence, not a passing Release gate.
- existing Release recovery rejects unresolved in-progress effects. recording recovery requires an already saved pending event, which is absent here.

## Blast radius

only the exact N15 unresolved Action/Step/Workflow and their truthful terminal disposition. installed N, historical Events, other containers and all Release gates remain unchanged.

## Operator decision

the Operator explicitly approved: "Yes—record unknown and continue". the reviewed source-admitted recovery recorded Action, Step and Workflow interruption facts through MCP, with unknown Unit outcome and no replay, promotion or retirement. the scheduler is CANCELLED. the original checkpoint SHA remains unchanged; the separate stopped companion preserves predecessor results. an identical repeat returned already_resolved with the same three Event references.

## Resolution

- resolution carrier: `.caprmedio_install/workflow_orchestrator/runs/release-epic-resume-20261006-N15/release_unknown_effect_resolution.json`.
- Journal: `run-support-2026-10-07-part-1.ndjson`, lines 1–3.
- Event references: `event-36c4cff6-9480-47d7-81a3-33c0f7f1198d`, `event-8cdfbda7-44ab-4f31-a943-cefffd79aff3`, `event-4865a151-f54d-44db-9bba-c5b6a0a7250e`.
- N15 is interrupted/unknown, not a passing Release. a fresh successor remains subject to every mandatory gate.
