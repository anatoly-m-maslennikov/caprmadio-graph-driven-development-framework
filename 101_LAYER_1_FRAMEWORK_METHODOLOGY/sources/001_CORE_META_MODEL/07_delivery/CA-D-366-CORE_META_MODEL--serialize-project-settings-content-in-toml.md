---
subjects:
  governs: "Project Settings/Authoritative Carrier/Content"
  depends_on:
    - "Project"
    - "Atom/Identifier/Project Prefix"
    - "Framework Instance Settings"
    - "Projection"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-364
atom_id: "CA-D-366"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Project Settings Content in TOML

## Scope

the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode Operator-editable Project initialization inputs through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Framework Instance choices **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details
