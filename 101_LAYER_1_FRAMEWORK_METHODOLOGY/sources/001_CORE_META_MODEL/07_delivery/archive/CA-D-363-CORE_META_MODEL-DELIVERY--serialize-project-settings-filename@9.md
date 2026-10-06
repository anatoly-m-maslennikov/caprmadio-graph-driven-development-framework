---
subjects:
  governs: "Project Settings/Authoritative Carrier/Filename"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 9
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-362
atom_id: "CA-D-363"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Project Settings Filename

the authoritative Project Settings TOML File Carrier filename **must** match `caprmedio_<project_name>_settings.toml`, **where** `<project_name>` is the exact lowercase Project name.
