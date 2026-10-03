---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 10
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-358
atom_id: "CA-D-359"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Scope

the Framework Instance Settings Artifact for a Project named `<project_name>`.

## Claim

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
