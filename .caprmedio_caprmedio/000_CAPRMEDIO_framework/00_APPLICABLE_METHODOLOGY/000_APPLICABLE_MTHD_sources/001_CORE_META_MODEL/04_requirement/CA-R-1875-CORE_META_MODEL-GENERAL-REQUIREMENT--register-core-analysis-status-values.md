---
atom_id: CA-R-1875
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Atom/Content Role: Analysis/Status"
  depends_on:
    - "Atom/Content Role: Analysis"
    - "Atom/Content Role: Analysis/Type"
    - "Artifact/Revision/Status"
    - "Extension"
    - "Project Configuration"
version: 1
updated_at: 2026-10-05 05:37:29 +0400
relations: {relates_to: [CA-R-1232, CA-R-1337, CA-R-1664, CA-R-1727, CA-R-1306, CA-R-1308, CA-R-1312, CA-R-1313]}
---
# Summary

Register Core Analysis Status Values

## Scope

the default Status value domain of Analysis Atoms with Type Analysis Report or Rationale.

## Claim

the Core allowed values of Analysis Status **must** be exactly (Draft, Done, Archived); that one Content Role Status model applies to Analysis Atoms with Type Analysis Report or Rationale unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.

## Details

this Status is the Artifact Revision Property of the Analysis Atom itself. it does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727 continues to govern when an admitted Analysis is Draft or Done and the meaning of its archival.
