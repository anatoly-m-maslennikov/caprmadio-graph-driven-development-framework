---
subjects:
  governs: "semantics"
  depends_on: []
version: 15
updated_at: "2026-09-13 00:51:00 +0400"
relations: {}
atom_id: "CAPRMEDIO-META-REQU-143"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Distinguish enacted release and runtime facts from Operations authority

successful **and** failed release **or** deployment events, deployed environment state, runtime health, **and** incidents **must** be treated as operational facts whose execution evidence **and** state changes are carried by Journal Records. these facts **and** Records are distinct from reusable Operations definitions **and** **must not** themselves establish **or** silently change Plan, Requirement, Method, Evaluation, Delivery, **or** Operations authority.
