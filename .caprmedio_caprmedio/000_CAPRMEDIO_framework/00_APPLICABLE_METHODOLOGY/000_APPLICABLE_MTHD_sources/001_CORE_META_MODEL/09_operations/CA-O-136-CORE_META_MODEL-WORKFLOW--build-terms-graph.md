---
atom_id: CA-O-136
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Build Terms Graph"
  depends_on: ["Workflow", "Step", "Workflow Run", "Projection/Type: Terms Graph"]
version: 2
updated_at: "2026-10-04 16:51:32 +0000"
relations:
  relates_to: [CA-O-138, CA-R-1508, CA-R-1519, CA-R-1525, CA-R-1335, CA-R-1728]
---
# Summary

Build Terms Graph

## Operation

Build Terms Graph **means** the reusable Workflow whose entry **and** only node is CA-O-138, the Terms Graph Construction Step. that Step owns its Action reference **and** invocation bindings; the Action owns construction behavior. the graph uses current Workflow execution authority under CA-R-1519 **and** exact definition Revisions under CA-R-1525.

### Graph scheme

| Entry/node | Result condition | Terminal outcome |
|---|---|---|
| CA-O-138 | built **or** no_op, with the Action's required current-selection, fidelity, validity **and** recording conditions satisfied | complete, preserving built versus no_op **and** the exact Projection/result references |
| CA-O-138 | incomplete, conflicting, stale **or** blocked | stop with that limitation **and** its affected frontier; request the missing evidence **or** authorization |
| CA-O-138 | reported built **or** no_op but **any** required completion condition is unmet **or** unsupported | blocked; retain the actual result **and** missing condition **without** accepting completion |
| CA-O-138 | failed | failed with actual effects **and** recovery evidence |
| CA-O-138 | canceled | canceled with actual effects **and** retained evidence |

there is no next-Step edge **or** automatic revisit. these are terminal outcomes, **not** extra nodes; no ON_RESULT Relation **to** an Action **or** terminal label is invented. a new attempt needs a separately admitted invocation; source discovery, a failed build **or** a no-op does **not** authorize a retry, source repair **or** automatic rebuild.

the Workflow Run retains the exact Step/Action bindings **and** its start/terminal Journal evidence under CA-R-1525, CA-R-1720 **and** CA-R-1728. an absent Workflow recording receipt prevents a complete Run claim even **when** a Projection was produced; retain the actual result **and** recording blocker **without** replaying construction.

## Details

this one-node scheme reuses CA-R-1335's graph kind. a governed-only **or** narrower view is **not** another graph kind **or** vocabulary authority. a generic rebuild route **may** select this Workflow but does **not** force it.
