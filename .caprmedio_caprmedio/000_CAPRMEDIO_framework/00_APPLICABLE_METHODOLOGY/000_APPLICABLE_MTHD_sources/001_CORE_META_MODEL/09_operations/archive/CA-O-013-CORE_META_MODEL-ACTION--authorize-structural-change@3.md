---
subjects:
  governs: "Authorize Structural Change"
  depends_on:
    - "Action"
    - "Project Structure"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
---
# Authorize structural change

Authorize Structural Change **means** the Action that checks a structural change proposal against the Operator's actual authorization **and** the effective Autonomous Confidence Threshold, returning permission for the exact proposed effects **or** a blocked decision with its reason. existing authorization **may** cover those effects; a new approval **must** be requested **if** they exceed it, conflict resolution requires it, **or** uncertainty fails the effective threshold. approval **must** remain bound **to** the proposal **and** selected source state. this Action **must not** infer permission from a folder observation, a generated result, confidence alone, **or** the existence of a Plan.
