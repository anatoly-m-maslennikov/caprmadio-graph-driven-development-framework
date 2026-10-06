---
subjects:
  governs: "Extension Installation"
  depends_on:
    - "Extension"
    - "Project Configuration"
version: 11
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
atom_id: "CA-R-1206"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Separate Extension Installation from Activation

installing an Extension **must** make its immutable authority available **to** Project Configuration **without** making the Extension authority applicable **to** the current Project.
