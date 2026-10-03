---
subjects:
  governs: "CAPRMEDIO/Project Root/Carrier"
  depends_on:
    - "Directory Carrier"
    - "Delivery"
version: 9
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
atom_id: "CA-D-327"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Use the Project Root Only for Delivery Carriers

the CAPRMEDIO Project root **must** carry **only** Delivery Directory Carriers produced for Project Scope Units whose authority Carriers live under `.caprmedio_caprmedio/` **or** another registered Project-owned Carrier root.
