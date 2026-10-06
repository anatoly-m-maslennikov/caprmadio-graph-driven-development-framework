---
version: 14
updated_at: "2026-09-14 23:34:13 +0000"
relations:
  child_of:
    - CA-M-001
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Scope Unit"
    - "Atom"
    - "Owned Atoms"
    - "Targeting Atoms"

atom_id: "CAPRMEDIO-REQU-032"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Let Parents Own Immediate Child Goals

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
