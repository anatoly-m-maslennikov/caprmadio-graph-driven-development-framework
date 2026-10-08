---
atom_id: CA-C-510
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 18:24:00 +0000"
subjects:
  governs: "Repair N12 selected Run fixtures"
  depends_on: [Implementation, Evaluation, Source Carrier, Journal]
relations:
  concern_about: [CA-P-1805, CA-P-1801]
---
# Summary

Repair N12 selected Run fixtures

## Concern

four selected execution and MCP test cases fail in the sealed Unit context.

## Evidences

the retained actual N12 JUnit report contains 4 failing cases in this lane. N12's later source-currentness refusal does not invalidate those frozen test observations or establish their cause.

## Blast radius

the declared Unit modules and their shared source-complete fixture or implementation. no actual E2E, image or release acceptance is inferred from mock results.

## Decision

repair confirmed selected-run/MCP fixture or code mismatches while preserving existing authority, source freshness and recording contracts.

## Result

the selected-execution suite passes 20 tests and the isolated MCP suite passes 4 tests. the fixtures copy exact bound sources into disposable Projects, allow bounded gateway cold start and correctly stop before a next Step while terminal recording is pending. independent review accepts the changes; actual all-route release proof remains separate. retain the frozen N12 report and historical Events.
