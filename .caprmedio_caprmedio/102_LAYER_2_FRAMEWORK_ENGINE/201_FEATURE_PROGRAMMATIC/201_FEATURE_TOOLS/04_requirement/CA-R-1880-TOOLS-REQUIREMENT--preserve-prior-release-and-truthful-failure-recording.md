---
atom_id: CA-R-1880
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Failure and recovery"
  depends_on: [Tool, Workflow Run, Action Run, Journal, Artifact, Image]
relations:
  relates_to: [CA-R-1878, CA-R-1879]
---
# Summary

Preserve the prior release and truthful failure recording

## Scope

Release failure, recording uncertainty, rollback, and delayed old-image retirement.

## Claim

On a failed, blocked, or uncertain release effect or recording, Release Version **must** preserve the prior selected N and actual effect evidence, report the shared Run/Action result truthfully, and never replay an uncertain effect; it may retire an exact old image only after successful N+1 verification and proof that no container or required rollback reference retains it.

## Details

Rollback restores only the retained prior selection and affected derived carriers. A request, dry run, candidate manifest, or queued Run is not success, and no failure path authorizes source mutation or broad image pruning.
