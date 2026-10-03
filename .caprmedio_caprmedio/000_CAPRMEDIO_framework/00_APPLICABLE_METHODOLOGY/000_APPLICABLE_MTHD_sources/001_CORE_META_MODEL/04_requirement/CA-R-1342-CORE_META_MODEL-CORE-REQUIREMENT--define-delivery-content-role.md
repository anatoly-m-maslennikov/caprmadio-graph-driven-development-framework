---
subjects:
  governs: "Atom/Content Role: Delivery"
  depends_on:
    - "Atom/Content Role"
    - "Atom/Claim"
    - "Carrier"
    - "Entity"
    - "Entity/Carrier"
version: 11
updated_at: "2026-09-28 22:47:05 +0000"
relations: {}
atom_id: "CA-R-1342"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Delivery Content Role

## Scope

the Delivery Content Role.

## Claim

Delivery **means** the Content Role of an Atom Claim that defines the Carrier model **or** constrains how an Entity is carried.

## Details

the Carrier model includes:

- Carrier definitions **and** classification.
- the Entity/Carrier binding **and** its identity-preservation constraints.
- Carrier format, storage, representation, **and** placement.
- constraints on Carrier changes.

a Carrier definition **or** classification is a Delivery contribution even **when** it does **not** prescribe a concrete format **or** location.
