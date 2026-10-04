---
subjects:
  governs: "Configuration Selection and Precedence"
  depends_on:
    - "Framework Instance Settings"
    - "Extension"
    - "Tool"
version: 21
updated_at: "2026-10-03 02:39:08 +0400"
relations: {}
atom_id: "CA-R-1724"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1724-CORE_META_MODEL-CORE--define-configuration-selection-and-precedence.md
---
# Summary

Define Configuration selection and precedence

## Scope

Framework Instance Settings Artifact selection of available Tools **and** Extensions.

## Claim

the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.

## Details
