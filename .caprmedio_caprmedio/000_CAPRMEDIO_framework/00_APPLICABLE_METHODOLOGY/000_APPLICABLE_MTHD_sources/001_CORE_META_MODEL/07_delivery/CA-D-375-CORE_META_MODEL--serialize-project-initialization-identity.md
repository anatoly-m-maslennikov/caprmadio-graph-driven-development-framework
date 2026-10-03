---
subjects:
  governs: "Project Settings/Project identity/Carrier"
  depends_on:
    - "Project Settings"
    - "Project"
    - "Project Name"
    - "Operator"
    - "Atom"
    - "Implementation"
version: 9
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-375"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact lowercase value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details
