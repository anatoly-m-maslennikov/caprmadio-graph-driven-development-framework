---
subjects:
  governs: "Carrier/Storage Boundary"
  depends_on:
    - "Framework-Owned Carrier"
    - "Project-Owned Carrier"
    - "Runtime State Carrier"
version: 11
updated_at: "2026-10-02 19:18:22 +0400"
relations: {}
atom_id: "CA-D-341"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-341-CORE_META_MODEL-CORE--separate-persistent-authority-from-runtime-state.md
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Framework-Owned and Project-Owned Carriers.

## Claim

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.

## Details
