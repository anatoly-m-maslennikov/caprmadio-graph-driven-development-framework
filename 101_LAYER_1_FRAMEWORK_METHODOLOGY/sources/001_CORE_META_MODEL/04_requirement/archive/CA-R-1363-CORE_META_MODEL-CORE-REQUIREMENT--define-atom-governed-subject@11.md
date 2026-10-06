---
subjects:
  governs: "Atom/Governed Subject"
  depends_on:
    - "Atom/Subjects"
    - "GOVERNS"
    - "Subject"
    - "Relation Kind"
    - "Entity"
    - "Atom/Claim"
version: 11
updated_at: "2026-09-22 20:07:50 +0000"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
atom_id: "CA-R-1363"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Atom Governed Subject

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Entity governed by the Atom's Claim; the Relation **and** its target are distinct.
