---
subjects:
  governs: "Structural Entity/Authoritative Carrier"
  depends_on:
    - "Structural Entity"
    - "Directory Carrier"
    - "Scope Unit"
    - "Project Structure"
version: 3
updated_at: "2026-09-20 23:55:10 +0000"
relations: {"relates_to": ["CA-D-259", "CA-D-312", "CA-R-1484"]}
atom_id: "CA-D-465"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Carry Each Materialized Structural Entity with a Directory Carrier

**every** materialized Structural Entity **must** be carried by **`>=1`** Directory Carrier; a Scope Unit established by Project Structure **may** remain unmaterialized under CA-R-1484 without losing its declaration **or** identity.
