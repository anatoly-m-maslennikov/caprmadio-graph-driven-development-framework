---
subjects:
  governs: "Applicable Methodology/Sources"
  depends_on:
    - "Methodology Source"
    - "Core Meta-Model"
    - "Project Configuration"
    - "Extension"
    - "Framework Instance Settings"
version: 15
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
atom_id: "CA-R-1228"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Include all applicable Methodology Sources

the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.
