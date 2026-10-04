---
atom_id: CA-E-553
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 23:00:41 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES"
  depends_on: [Tool, Workflow, Action, Operator, Artifact, Journal, Workflow Run, Step Run]
relations:
  evaluation_for: [CA-R-1833, CA-R-1834]
---
# Summary

Verify approved reversal admission and happy/no-op results

## Scope

Functional mocked Project/MCP cases for REVERT_CHANGES manifest admission, exact happy reversal, no-op, and pre-effect rejection.

## Claim

Every realization **must** prove that only the exact approved manifest can reach guarded execution, and that admitted/no-op/reverted results remain distinct from a mutation or Journal-completion claim.

## Details

Use a functional Project mock with governed effect adapters and real exposed MCP request/response validation. The happy case supplies one complete approval, current target/reference hashes, permissions, ordered effects, and preservation evidence; it expects `admitted`, then `reverted`, each approved effect once, retained prior history/reference evidence, and shared Run/Journal receipt references. It must assert no automatic inverse beyond the ordered manifest.

The already-satisfied case supplies the same complete approval and current evidence, expects `no_op`, zero applied effects, no fictitious mutation, and truthful shared Run evidence. Independently reject missing approval, altered effect ordering, missing before/after evidence, revoked permission, unsupported effect, or a stale target/reference/governing hash before any effect. Each returns `blocked`, names the precise binding, leaves targets/history/reference and effects unchanged, and creates no invented Action Run when dispatch never started.

Acceptance compares full result, effect account, preserved evidence, mutation trace, and shared receipt references—not outcome text or count alone. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-1833; CA-R-1834; CA-O-131 v2; CA-O-132 v1; CA-P-1463 v1.
