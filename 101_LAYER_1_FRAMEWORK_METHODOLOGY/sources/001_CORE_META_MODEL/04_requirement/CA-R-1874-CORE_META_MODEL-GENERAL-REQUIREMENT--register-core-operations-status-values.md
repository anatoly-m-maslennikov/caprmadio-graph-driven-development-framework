---
atom_id: CA-R-1874
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Atom/Content Role: Operations/Status"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Operations/Type"
    - "Artifact/Revision/Status"
    - "Extension"
    - "Project Configuration"
version: 1
updated_at: 2026-10-05 05:34:06 +0400
relations: {relates_to: [CA-R-1530, CA-R-1565, CA-R-1306, CA-R-1308, CA-R-1312, CA-R-1313]}
---
# Summary

Register Core Operations Status Values

## Scope

the default Status value domain of Operations Atoms with Type Workflow, Step, Action, or Actor.

## Claim

the Core allowed values of Operations Status **must** be exactly (Draft, Active, Archived); that one Content Role Status model applies to Operations Atoms with Type Workflow, Step, Action, or Actor unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.

## Details

this Status is the Artifact Revision Property of the Operations Atom itself. it does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state.
