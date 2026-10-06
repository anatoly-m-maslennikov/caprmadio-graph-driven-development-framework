---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Subject"
    - "Atom/Subjects"
    - "Entity"
    - "Atom/Claim"
version: 13
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
atom_id: "CA-R-1280"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Reference Every Prerequisite Subject through DEPENDS_ON

**every** canonical Entity required by an Atom's Claim **without** governing that target **must** be referenced directly through DEPENDS_ON **in** the Atom's Subjects Property.
