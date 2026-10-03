---
subjects:
  governs: "authority"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Entity"
    - "Implementation"
    - "Action"
    - "Workflow"
    - "Actor"
    - "Journal/Record"
    - "Verification"
version: 23
updated_at: "2026-09-21 00:39:50 +0000"
relations:
  child_of:
    - CA-M-001
atom_id: "CAPRMEDIO-META-REQU-092"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Authority, Evaluation, and Operations remain distinct

CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549, including specific reusable Operations definitions under CA-R-1530; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but cannot themselves establish, edit, replace, **or** override semantic authority.
