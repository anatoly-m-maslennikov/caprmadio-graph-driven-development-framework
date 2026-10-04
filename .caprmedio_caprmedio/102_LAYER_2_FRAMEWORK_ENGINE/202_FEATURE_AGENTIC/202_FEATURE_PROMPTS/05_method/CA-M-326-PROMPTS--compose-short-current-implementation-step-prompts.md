---
atom_id: "CA-M-326"
content_role: "Method"
type: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation step prompt construction"
  depends_on: ["Prompt", "Step", "Action"]
relations:
  relates_to: [CA-R-1843, CA-R-1845]
---
# Summary

Compose short current implementation Step prompts

## Scope

one self-contained prompt per current CA-O-016 Step.

## Claim

**to** implement one Step prompt, state its exact Step, Action, and context; name required inputs, permitted work, output artifacts, admitted result labels, and blocking conditions without restating methodology authority.

## Details

Keep each prompt concise, pin-aware, and scoped to its own Step. The caller owns transitions and dispatch; a prompt does not route future Steps or infer a pass.
