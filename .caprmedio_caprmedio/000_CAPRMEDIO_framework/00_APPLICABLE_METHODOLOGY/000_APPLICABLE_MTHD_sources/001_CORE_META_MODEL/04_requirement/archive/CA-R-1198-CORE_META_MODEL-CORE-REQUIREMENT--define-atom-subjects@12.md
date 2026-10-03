---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Atom"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Property"
    - "Entity"
version: 12
updated_at: "2026-09-17 17:09:59 +0000"
relations: {}
atom_id: "CA-R-1198"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Atom Subjects

the Atom Subjects Property **means** the Atom Property that records its direct Subject Relations: GOVERNS **and** DEPENDS_ON links from that Atom **to** canonical targets. it preserves the target identities **without** storing copies of the targets **or** introducing a separately identified Subject object **or** a nested Entity **or** Reference Property for **every** link.
