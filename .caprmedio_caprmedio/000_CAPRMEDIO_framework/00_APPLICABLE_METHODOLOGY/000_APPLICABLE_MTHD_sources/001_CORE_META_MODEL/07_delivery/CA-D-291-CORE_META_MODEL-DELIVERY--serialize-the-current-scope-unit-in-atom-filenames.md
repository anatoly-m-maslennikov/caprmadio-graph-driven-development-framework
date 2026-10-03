---
subjects:
  governs: "Atom/Carrier/Current Scope Unit/Filename Token"
  depends_on:
    - "Atom/Scope"
    - "Scope Unit"
version: 15
updated_at: "2026-10-01 21:24:59 +0400"
relations: {}
atom_id: "CA-D-291"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
