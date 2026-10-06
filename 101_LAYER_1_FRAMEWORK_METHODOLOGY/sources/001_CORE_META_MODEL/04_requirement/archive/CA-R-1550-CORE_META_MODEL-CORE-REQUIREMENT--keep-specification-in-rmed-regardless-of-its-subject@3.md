---
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Atom/Claim"
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Atom/Content Role: Implementation"
    - "Atom/Subjects"
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"relates_to": ["CA-R-1531", "CA-R-1548", "CA-R-1549", "CA-R-1343"]}
atom_id: "CA-R-1550"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep specification in RMED regardless of its Subject

a specification Claim about Change **or** Implementation content **must** remain **in** Spec Content Roles according **to** its own contribution rather than inherit the Content Role of the content it specifies.
