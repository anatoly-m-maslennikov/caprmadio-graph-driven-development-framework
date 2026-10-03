---
subjects:
  governs: "Relational Atom Classification Validation"
  depends_on:
    - "Relational Atom/Qualified Type"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Content Role: Requirement/Type: Demand"
    - "Atom/Content Role: Plan/Type: Plan"
version: 13
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"evaluation_for": ["CA-R-923", "CA-R-924", "CA-R-1576", "CA-R-1588"]}
atom_id: "CA-E-425"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation"
global_tier: 11
---
# Validate Relational Atom Classifications

the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.
