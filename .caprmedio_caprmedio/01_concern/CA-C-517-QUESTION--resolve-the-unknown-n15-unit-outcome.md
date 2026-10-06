---
atom_id: CA-C-517
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 23:10:43 +0000"
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

the Operator explicitly approved: "Yes—record unknown and continue". authorize a narrowly admitted operation that records N15 as interrupted/unknown, preserves all existing evidence, refuses competing terminal receipts and repeats, and performs no Unit replay, promotion or retirement. this capability requires source-first RMED and independent acceptance before execution. no terminal fact has yet been created. keep this Question active until its authorized disposition is implemented and recorded; independent source/test repairs continue.
