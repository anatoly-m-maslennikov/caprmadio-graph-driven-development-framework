---
subjects:
  governs: "Optional Projection/Activation"
  depends_on:
    - "Framework Instance Settings"
    - "Projection"
version: 19
updated_at: "2026-09-10 07:34:05 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-305"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Configure Optional Projection Activation

the Framework Instance Settings Artifact **must** resolve **every** registered optional Projection as active **or** inactive, with inactive as the default **and** an unknown Type value under Projection rejected.
