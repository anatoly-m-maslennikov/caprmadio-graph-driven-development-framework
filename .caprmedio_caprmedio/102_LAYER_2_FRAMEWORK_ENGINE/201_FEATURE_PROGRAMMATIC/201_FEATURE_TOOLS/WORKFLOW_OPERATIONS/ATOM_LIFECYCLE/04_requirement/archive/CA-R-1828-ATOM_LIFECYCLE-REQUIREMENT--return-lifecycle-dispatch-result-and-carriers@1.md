---
atom_id: CA-R-1828
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Result Carriers"
  depends_on: ["Atom", "Artifact/Carrier", "Journal/Record", "Authorization"]
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  relates_to: [CA-R-1825, CA-R-1826, CA-R-1827, CA-R-866, CA-R-868, CA-R-1041]
---
# Summary

Return lifecycle dispatch result and carriers

## Scope

The request/result and carrier handoff at the lifecycle dispatcher boundary.

## Claim

The dispatcher **must** return a typed result containing request identity, target/predecessor identity where applicable, sealed expected and observed Carrier metadata, selected operation, model/currentness resolution, preview-or-mutation disposition, authorization disposition, exact native result, diagnostics, changed/unchanged/unknown effects, and history/lineage references. A successful Replace result names both predecessor and successor Carriers. A Change Status result names the prior and admitted resulting status. A preview names no observed mutation.

If carrier persistence, verification, or result recording is incomplete, the result marks the affected carrier/effect `unknown` or `unverified`, retains recoverable evidence, and never claims recovery or success without observed restoration.

## Details

The shared Run receipt consumes this result; this carrier contract does not duplicate its event schema.
