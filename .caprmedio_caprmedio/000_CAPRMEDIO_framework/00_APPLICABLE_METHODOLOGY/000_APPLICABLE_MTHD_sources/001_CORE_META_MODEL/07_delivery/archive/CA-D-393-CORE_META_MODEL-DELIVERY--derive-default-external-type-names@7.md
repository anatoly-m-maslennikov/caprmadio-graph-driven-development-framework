---
subjects:
  governs: "Type"
  depends_on:
    - "Atom/Content Role"
    - "Carrier"
version: 7
updated_at: "2026-09-10 20:55:13 +0400"
relations:
  child_of:
    - "CAPRMEDIO-META-REQU-100"
    - "CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type"
    - "CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role"
atom_id: "CA-D-393"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
global_tier: 11
---
# Derive default external Type names

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
