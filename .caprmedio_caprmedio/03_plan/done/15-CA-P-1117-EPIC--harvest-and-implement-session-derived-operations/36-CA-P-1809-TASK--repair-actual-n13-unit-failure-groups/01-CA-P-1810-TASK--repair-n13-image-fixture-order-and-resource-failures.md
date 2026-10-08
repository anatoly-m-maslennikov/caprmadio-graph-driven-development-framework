---
atom_id: CA-P-1810
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 23:10:43 +0000"
subjects:
  governs: "Repair N13 image fixture order and resource failures"
  depends_on: [Implementation, Evaluation, Source Carrier, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1809]
  relates_to: [CA-C-514]
---
# Summary

Repair N13 image fixture order and resource failures

## Objective

repair the confirmed cause of the twenty-two image-fixture failures in the sealed Unit context without weakening image or retention predicates.

## Details

test_release_image.py and its necessary isolated fixture helper; reproduce the actual later-case failure, retain precise reason diagnostics, and verify a bounded order-equivalent regression.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Acceptance evidence

independent review accepts the test-only idempotent cleanup of the current nested fixture and detailed suite-failure diagnostics. the retained N13 image and read-only archived N13 workspace completed the bounded ordered ten-case chain with 10 tests, zero failures and zero errors, including the first historically failing image case. immediate-prefix failure did not reproduce, so the exact causal contribution of the cleanup repair to N13's full-module failure remains unproven; the fresh full Release gate decides integration.

this is bounded fixture acceptance only; actual complete Release acceptance remains with CA-P-1809 and CA-P-1117.

## Reopened resource boundary

N15's complete child report still contains 21 image-fixture failures and one error before image assertions. the nested fixture Suite reports recording_uncertain/OSError. retained reference snapshots approached the one-GiB module-local temporary mount; the direct errno was not captured, so capacity is a supported hypothesis, not proven causality. the previous cleanup correction remains accepted, but this resource remainder is unfinished. review the bounded D579 two-GiB source revision, apply exact executor/test parity without changing other limits, and retain focused acceptance plus a fresh complete Unit result. no N15 passing receipt or exit code is inferred.
