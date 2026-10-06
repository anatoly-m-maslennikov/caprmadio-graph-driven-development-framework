---
atom_id: CA-P-1773
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 04:12:31 +0000"
subjects:
  governs: "Release Harness source-pin refresh"
  depends_on: [Delivery, Evaluation, Implementation, Manifest]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1757, CA-P-1717, CA-P-1721]
---
# Summary

Refresh the admitted HTTP Harness source pin

## Objective

Bind the new accepted HTTP case in the existing mandatory Docker Harness without weakening its exact source admission.

## Details

Root owns CA-D-572 private Harness metadata and the matching release_source_admission.py trust anchor. Only the existing test_docker_e2e.py byte pin and timestamp change; D572's Claim, closed schema, twelve occurrences, source frontier and Version 10 remain unchanged. This is carrier/source-pin recoding, not a new Workflow definition. Independent read-only review verifies that exact delta before a fresh release dispatch. Estimated slice <=15 minutes.

## Definition of Done

The private pins reopen successfully, the unchanged sixteen-route manifest remains valid, focused admission tests pass and independent review accepts. No stale-pin guard is bypassed and no historical Run is rebound.

## Pre-execution review

Root selects this necessary mechanical pin refresh under the accepted E584/E585 HTTP proof, DRY and current source authority. Actual Docker verification remains P1757.
