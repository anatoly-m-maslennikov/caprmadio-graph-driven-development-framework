---
subjects:
  governs: "Navigational Order Number"
  depends_on:
    - "Carrier"
    - "Scope Unit"
    - "Project Structure"
version: 5
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
atom_id: "CA-D-380"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Navigational Order Numbers

**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.
