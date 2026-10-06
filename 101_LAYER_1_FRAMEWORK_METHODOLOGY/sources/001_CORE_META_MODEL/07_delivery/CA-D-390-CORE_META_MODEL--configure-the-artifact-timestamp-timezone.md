---
subjects:
  governs: "Framework Instance Settings/Artifact Timestamp Timezone"
  depends_on:
    - "Framework Instance Settings"
    - "Artifact/Revision"
    - "Carrier"
version: 8
updated_at: "2026-10-02 19:36:21 +0400"
relations:
  child_of:
    - "CA-D-311"
    - "CA-R-1402"
atom_id: "CA-D-390"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Configure the Artifact timestamp timezone

## Scope

the Artifact timestamp timezone setting in Framework Instance Settings.

## Claim

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS`, **and** the setting supplies its timezone interpretation.

## Details
