---
atom_id: "CA-D-506"
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
    - "Entity"
    - "Carrier"
    - "Property"
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-506-CORE_META_MODEL-CORE--give-every-non-ephemeral-entity-a-carrier.md
  source_atom_id: CA-D-506
  source_atom_revision: 1
  source_sha256: 8f1102676b3b04ec408c17a6a6995858030bd9b0df609cf9feb9f96fb829fae9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Give every non-ephemeral Entity a Carrier

## Scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
