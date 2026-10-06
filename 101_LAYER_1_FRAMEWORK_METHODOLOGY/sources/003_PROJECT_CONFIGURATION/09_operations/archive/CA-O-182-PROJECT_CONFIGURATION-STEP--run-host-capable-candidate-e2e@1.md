---
atom_id: CA-O-182
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run host-capable Candidate E2E"
  depends_on: [Workflow, Step, Action, Test, Docker Image, Journal]
version: 1
updated_at: 2026-10-06 00:00:00 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-181]
---
# Summary

Run host-capable Candidate E2E

## Step

This Step invokes CA-O-181 once after CA-O-177's immutable image canary, binding the exact candidate/package/image/N identity and explicit host-capable controller authorization.

## Details

Absent host capability is non-pass, not a fallback to the frozen Docker worker. Failed, partial, stale, unsafe or missing-recording results stop before Full Gate aggregation, promotion and retirement without replay.
