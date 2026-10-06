---
subjects:
  governs: "Artifact/Type"
  depends_on:
    - "Artifact"
    - "Type"
    - "NARROWER_THAN"
version: 19
updated_at: "2026-09-11 05:27:15 +0400"
relations: {}
atom_id: "CAPRMEDIO-META-REQU-741"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Prohibit Artifact Type admission through NARROWER_THAN

an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
