---
atom_id: CA-R-1893
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 10:47:48 +0000"
subjects:
  governs: "MCP/Release binding state reconciliation"
  depends_on: [MCP, Manifest, Git, Operator, Journal, Carrier, Source Carrier]
relations:
  relates_to: [CA-R-1882, CA-C-497, CA-P-1780]
---
# Summary

Observe the exact Git-backed Release binding state

## Scope

explicit current-state reconciliation for the canonical selected-workflow binding when its existing Journal history differs from its exact committed bytes.

## Claim

MCP **must** provide a separately authorized, plan-first observation of the exact Git-backed current Release binding state that advances its observed carrier history without rewriting the Manifest or historical events.

## Details

- this operation is not initial publication, admission refresh, Release execution or replay of a historical write. its trusted grant cannot substitute for their grants.
- require a regular canonical sixteen-route binding admitted by the narrow refresh-base validator, exact equality of physical bytes to the current Git HEAD blob, valid existing target-specific Journal history, and no pending publication intent.
- seal the current raw digest, exact Git commit/blob, latest event identity/revision/digest and current source frontier. changed inputs, dirty/unproven bytes or conflicting history are refused.
- append one current-time recovered state at the prior carrier-history revision **+1**. its exact nested evidence witnesses the predecessor; it does not claim that earlier changes were authored, replayed or recorded at their historical times.
- planning has no effect. execute holds the existing carrier lock through fresh checks and observation append. an uncertain append retains the exact sealed event for recording-only recovery.
- an exact retry returns or finalizes the same observation once. after accepted reconciliation, ordinary guarded refresh uses its unchanged admission checks and links its actual change to the observed state. installed N remains unchanged.
