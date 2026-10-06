---
subjects:
  governs: "Carrier/Representation"
  depends_on:
    - "Project"
    - "Scope Unit"
version: 7
updated_at: "2026-10-02 19:36:21 +0400"
relations: {}
atom_id: "CA-D-395"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
