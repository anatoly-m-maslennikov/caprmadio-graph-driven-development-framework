---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Subject Expression"
    - "Entity"
    - "Relation"
    - "Subject"
    - "Term"
version: 13
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
atom_id: "CA-R-1194"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Subject Path

a Subject Path **means** a full canonical Subject Expression used by a Subject Relation **to** identify **`=1`** Entity through its named Term components **and** registered qualifications. qualification retains its registered endpoint constraints; the path identifies the target **without** creating another target identity **or** becoming the Subject Relation itself.
