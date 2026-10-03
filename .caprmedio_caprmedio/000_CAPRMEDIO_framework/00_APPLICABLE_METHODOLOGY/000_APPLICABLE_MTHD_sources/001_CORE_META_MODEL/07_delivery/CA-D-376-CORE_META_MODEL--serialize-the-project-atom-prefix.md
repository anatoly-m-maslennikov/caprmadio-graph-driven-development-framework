---
subjects:
  governs: "Project Settings/Atom Prefix/Carrier"
  depends_on:
    - "Project Settings"
    - "Atom"
    - "Operator"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-376"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the Project Atom prefix

## Scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details
