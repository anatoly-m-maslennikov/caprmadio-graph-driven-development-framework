---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 20
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - "CA-M-002"
atom_id: "CA-R-1051"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Separate active authority from preserved history

the active RMED authority graph represents **only** current governed state. historical states **and** transitions are excluded from that graph **and** preserved through canonical lifecycle placement **and** append-only Journals; generated Projections **may** render history **without** making it active RMED authority.
