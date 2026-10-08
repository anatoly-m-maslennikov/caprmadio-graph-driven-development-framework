---
atom_id: CA-P-1719
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-05 16:43:32 +0000"
subjects:
  governs: "Release publication Journal handoff"
  depends_on: [Implementation, Operator, Journal, Manifest, Evaluation]
relations:
  is_decomposition_of: [CA-P-1715]
  blocks: [CA-P-1624]
---
# Summary

Record and recover sealed Release publication

## Objective

Deliver the MCP-owned canonical Journal handoff that survives an interrupted manifest publication without replaying an ambiguous write.

## Details

1. implement `release_manifest_lifecycle.py` against current CA-M-339@2, CA-E-582@2 and CA-D-576@2 and the shared private context contract. Use existing Work Journal primitives, not Workflow Run support or another ledger.
2. observe and record the prior carrier only when necessary; seal the exact successor event and preserve its pending evidence before replacement.
3. finalize only after exact target-byte and loader verification. Recover the same sealed event after recording failure; changed or uncertain target bytes do not authorize another replacement.
4. test the real generic Journal shape, prior-state linkage, append failure, interrupted publication and exact no-replay recovery in retained fixtures. Coordinate only the declared internal API with the publisher owner.

The bounded next implementation/review leaf is estimated at <=15 minutes. Decompose before exceeding that bound. Independent API authoring may proceed in parallel; dependent tests and acceptance wait for the current helper implementations. Root owns integration, accepted authority and Git.

## Definition of Done

Focused actual-Journal fixture tests and independent bounded review prove the declared sealing, prior linkage and byte-verified no-replay handoff. No canonical Project publication or actual Release Run is inferred.

## Pre-execution review

Root accepts this bounded decomposition of the parent's existing source requirements. It adds no selected Workflow or execution permission, preserves the required full behavior, and does not execute the Operator-deferred final all-Workflow audit.

## Result

The one MCP-owned lifecycle adapter uses the existing Work Journal pending/event mechanisms. It reuses sealed intents idempotently, records prior provenance truthfully, classifies changed target bytes as ambiguous, and recovers exact pending events without replacement replay. It now owns the actual carrier-lock scope rather than accepting a caller lock boolean. Fresh lifecycle fixtures passed 11/11; the independent cold-restart and final lock-gap reviews accepted the bounded implementation. Canonical Project publication is still the parent Task's separate gate.
