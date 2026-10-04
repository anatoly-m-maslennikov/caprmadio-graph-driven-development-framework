---
atom_id: CA-E-547
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Sealed Target"
  depends_on: ["Atom", "Atom/Relation", "Authorization"]
version: 1
updated_at: "2026-10-04 18:30:23 +0000"
relations:
  evaluation_for: [CA-R-1827]
---
# Summary

Verify sealed target and Relation diagnostics

## Scope

One target/predecessor and active inbound/outgoing Relation handling.

## Claim

Exercise valid one-target preview, changed-after-seal rejection, absent MCP authorization rejection, and a model-admitted status-change/Archive result that breaks one active inbound and one active outgoing reference. Verify preview reports both references by identity, reason, and active-referrer status without mutation. Then apply the explicitly authorized sealed, current status request: verify the admitted status transition occurs, both broken references remain unretargeted, and the result directs their separate authorized repair. Also exercise an explicitly authorized sealed request whose structural/currentness checks pass.

## Details

### Acceptance criteria

Only an authorized, current request with valid structural/currentness controls may delegate mutation. Broken resulting active references are diagnostics and repair handoff for a model-admitted status transition, not a blanket veto; all rejected cases preserve the original frontier.
