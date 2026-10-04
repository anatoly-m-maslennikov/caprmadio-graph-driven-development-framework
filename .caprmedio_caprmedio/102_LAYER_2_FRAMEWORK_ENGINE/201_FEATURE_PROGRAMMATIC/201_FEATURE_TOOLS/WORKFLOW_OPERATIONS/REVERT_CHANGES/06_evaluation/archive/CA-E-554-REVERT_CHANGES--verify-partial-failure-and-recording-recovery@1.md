---
atom_id: CA-E-554
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 23:00:41 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES"
  depends_on: [Tool, Workflow, Action, Operator, Artifact, Journal, Workflow Run, Step Run]
relations:
  evaluation_for: [CA-R-1834]
---
# Summary

Verify reversal partial failure and recording recovery

## Scope

Functional mocked Project/MCP cases for effect uncertainty, partial effects, Journal failure, and safe recovery of REVERT_CHANGES.

## Claim

Every realization **must** retain exact effect uncertainty and recording state; only confirmed zero-effect, zero-uncertainty execution failure may be `failed`.

## Details

Inject an execution failure before the first effect with confirmed zero applied and zero uncertain completion: expect `failed`, exact failure evidence, and no inverse/replay. Inject a timeout at the first effect with zero confirmed applied but unknown completion: expect `partial_failure`, an `uncertain` effect, and an explicit remaining boundary. Inject failure after one confirmed effect: expect `partial_failure`, completed/failed/unattempted effects, preserved history/reference evidence, and no automatic compensation.

Inject Journal failure before start: expect `recording_blocked` and no mutation. Inject recording failure after an actual effect: expect `recording_blocked`, known effect account and pending-recording evidence, never `reverted` or journaled/complete. Retry only recording with the same event identity and payload: expect one reconciled shared receipt and no second effect invocation. Retry with conflicting payload: reject without overwriting history or replaying effects. A recovery after target/hash/permission change must block remaining work until a new admitted manifest binds it.

Acceptance verifies MCP output, mutation trace, effect invocation count, preserved provenance, and shared Run/Journal receipt behavior. The shared J01–J08 schema is exercised by reference, not duplicated here. This is an executable-test specification, not runtime evidence.

### Sources

- CA-R-1834; CA-O-130 v1; CA-O-131 v2; CA-O-132 v1; CA-P-1463 v1; CA-P-1451 J01–J08.
