---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    - "Tool"
    - "Extension"
    - "Framework Instance Settings"
    - "Default Settings"
version: 9
updated_at: "2026-09-15 00:13:02 +0000"
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
type: "Delivery"
---
# Serialize Framework Settings Content in TOML

the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.
