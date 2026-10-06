---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "GOVERNS"
    - "Subject"
    - "Entity"
version: 13
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
atom_id: "CA-R-1203"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Split at Multiple Governed Subject Boundaries

an Atom **must** be split **if** its Claim governs **`>1`** canonical Entities through GOVERNS Subject Relations.
