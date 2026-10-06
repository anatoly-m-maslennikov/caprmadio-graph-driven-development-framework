---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    - "Tool"
    - "Extension"
    - "Framework Instance Settings"
    - "Default Settings"
version: 10
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-359
  relates_to:
    - CA-M-279
    - CA-D-408
atom_id: "CA-D-361"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-361-CORE_META_MODEL--serialize-framework-settings-content-in-toml.md
  source_atom_id: CA-D-361
  source_atom_revision: 10
  source_sha256: 08f48988f709e47417ae7d3c01c33c4bd9cfc64066e7d6996133a465afc51d68
  original_relations_sha256: c721615c7983c0a76470a5c52c89f21a22517496a3a90da9fb26001e4e66f71f
---
# Summary

Serialize Framework Settings Content in TOML

## Scope

the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details
