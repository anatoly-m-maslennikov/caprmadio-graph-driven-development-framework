---
atom_id: "CA-D-507"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
global_tier: 9
status: "Active"
version: 1
updated_at: "2026-09-28 22:47:05 +0000"
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on:
    - "Entity/Identity"
    - "Carrier/Format"
    - "File Carrier/Extension"
relations: {}
---
# Summary

Separate Entity identity from Carrier format

## Scope

changes limited **to** Carrier Format **or** File Carrier Extension.

## Claim

a change **to** Carrier Format **or** File Carrier Extension alone **must not** establish **or** change Entity identity.

## Details
