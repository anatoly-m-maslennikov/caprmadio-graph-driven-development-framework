---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 9
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-358
atom_id: "CA-D-359"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Bind Framework Settings to Its Authoritative TOML Carrier

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.
