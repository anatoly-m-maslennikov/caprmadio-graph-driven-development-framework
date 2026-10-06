---
atom_id: CA-E-592
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 10:47:48 +0000"
subjects:
  governs: "MCP/Release binding state reconciliation assurance"
  depends_on: [MCP, Manifest, Git, Operator, Journal, Carrier, Source Carrier]
relations:
  evaluation_for: [CA-R-1893, CA-M-349, CA-D-587]
---
# Summary

Verify honest Release binding state reconciliation

## Scope

fixture proof of exact, honest observation and recovery before guarded Release binding refresh.

## Claim

all observer realizations **must** prove one authorized, Git-backed current-state observation with unchanged Manifest and historical event bytes, exact predecessor evidence, and recording-only idempotent recovery.

## Details

- prove read-only planning creates no event, pending carrier or Manifest write.
- seed an initial publication, commit a genuine later binding revision, then observe it at the next carrier-history revision. validate the new-time recovered-state schema and exact nested predecessor witness; retain all previous event bytes and physical Manifest bytes.
- refuse non-HEAD/dirty bytes, symlink carriers, malformed/conflicting history, wrong or advanced predecessor, pending publication, changed Git/blob/source/input and forged or cross-operation grants before a new append.
- inject changes after authorization and after lock acquisition; prove the original sealed facts are not silently rebound.
- inject append or receipt failure. retain exact pending observation, finalize its original event once on retry, and refuse changed evidence. returning a recorded event must not append another line or create a new timestamp.
- prove a later ordinary admission refresh links its completed change to this recovered state and still enforces its normal source checks.
- no test may claim a historical write was replayed, a Manifest was changed by observation, an image was built or a Release completed. live publication remains a separate recorded execution.
