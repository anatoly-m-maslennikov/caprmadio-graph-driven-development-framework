---
subjects:
  governs: "Authorize Structural Change"
  depends_on:
    - "Action"
    - "Project Structure"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 5
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
atom_id: "CA-O-013"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Authorize structural change

Authorize Structural Change **means** the Action that checks a structural change proposal against the Operator's actual authorization **and** the effective Autonomous Confidence Threshold, returning permission for the exact proposed effects **or** a blocked decision with its reason. existing authorization **may** cover those effects; a new approval **must** be requested **if** they exceed it, conflict resolution requires it, **or** uncertainty fails the effective threshold. approval **must** remain bound **to** the proposal **and** selected source state. this Action **must not** infer permission from a folder observation, a generated result, confidence alone, **or** the existence of a Plan.
