---
atom_id: CA-R-1828
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Result Carriers"
  depends_on: ["Atom", "Artifact/Carrier", "Journal/Record", "Authorization"]
version: 2
updated_at: "2026-10-04 23:01:23 +0400"
relations:
  relates_to: [CA-R-1825, CA-R-1826, CA-R-1827, CA-R-866, CA-R-868, CA-R-1041]
---
# Summary

Return lifecycle dispatch result and carriers

## Scope

The request/result and carrier handoff at the lifecycle dispatcher boundary.

## Claim

The dispatcher **must** return its typed lifecycle payload inside CA-D-527's one shared outer result. The payload contains request identity; the complete target or predecessor Carrier set and, for Replace, every accepted successor Carrier set; sealed expected and observed Carrier Version/digest metadata; selected operation; model/currentness resolution; authorization disposition; exact native result; diagnostics; changed/unchanged/unknown effects; and history/lineage references. A successful Replace names its predecessor and every successor Carrier. A Change Status names the prior and admitted resulting status; an Archive also names every newly broken Relation and active referrer with its separate repair handoff. A preview names no observed mutation.

The shared outer result owns disposition, actual Run IDs and definition bindings when started, canonical Event IDs/receipts or the recording blocker, and retry disposition. A lifecycle result with incomplete persistence, verification, or recording marks the affected carrier/effect `unknown` or `unverified`, retains recoverable evidence, and uses CA-D-527's `recording_pending` rather than claiming recovery or success without observed restoration. An unstarted preview, decline, or block carries no invented Run/Event identity.

## Details

The shared Run receipt consumes this payload. This carrier contract creates no second Journal, Event schema, receipt, recording state, or retry mechanism.
