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
version: 2
updated_at: "2026-10-05 03:37:42 +0400"
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

The Evaluation also fails when a packet resolves the reviewed source rows from
an immutable prompt-code root, ambient current directory, host-path guess, or
unbound mount rather than its `selected_project` binding. It fails when a
source reference is absolute, escapes `.caprmedio_caprmedio`, has a duplicate,
missing, stale, or mismatched identity/version/digest, or when the active-M
Projection is not verified against the same selected Project source frontier.
An Agent must not launch in those cases. If a packet declares executable work,
the Evaluation also requires the existing explicit `workspace` and the exact
matching `permissions.implementation_workspace` capability; their absence or
mismatch is blocked evidence, not a new permission or a successful mock run.
