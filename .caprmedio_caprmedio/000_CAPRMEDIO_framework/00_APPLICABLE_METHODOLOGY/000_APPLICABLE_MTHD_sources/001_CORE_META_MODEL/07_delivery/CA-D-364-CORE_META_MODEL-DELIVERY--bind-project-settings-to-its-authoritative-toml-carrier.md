---
subjects:
  governs: "Project Settings/Authoritative Carrier"
  depends_on:
    - "Project Settings/Authoritative Carrier/Filename"
version: 9
updated_at: "2026-10-01 21:24:59 +0400"
relations:
  child_of:
    - CA-D-363
atom_id: "CA-D-364"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/caprmedio_<project_name>_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
