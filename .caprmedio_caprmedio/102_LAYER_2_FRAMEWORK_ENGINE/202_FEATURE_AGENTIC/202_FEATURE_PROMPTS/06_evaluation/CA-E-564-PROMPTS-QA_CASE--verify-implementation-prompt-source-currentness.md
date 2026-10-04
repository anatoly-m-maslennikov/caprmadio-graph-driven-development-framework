---
atom_id: "CA-E-564"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation prompt source currentness"
  depends_on: ["Prompt", "Workflow", "Step", "Action"]
relations:
  relates_to: [CA-R-1843]
---
# Summary

Verify implementation prompt source currentness

## Scope

the source-binding frontier for all seven Implementation Workflow prompts.

## Claim

the Implementation passes this Evaluation only when each required source identity, version, path, and digest matches current fully reviewed authority.

## Details

The stale delivered O016v9 and old Step/Action pins fail this case until an independent PROMPTS review has refreshed them; a digest edit alone is not a pass.
