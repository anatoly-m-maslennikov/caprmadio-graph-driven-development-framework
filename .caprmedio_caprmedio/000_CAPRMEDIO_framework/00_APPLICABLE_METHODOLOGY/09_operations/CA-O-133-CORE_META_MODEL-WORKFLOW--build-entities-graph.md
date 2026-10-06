---
atom_id: CA-O-133
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Build Entities Graph"
  depends_on: ["Workflow", "Step", "Workflow Run", "Projection/Type: Entities Graph"]
version: 2
updated_at: "2026-10-04 16:51:32 +0000"
relations:
  relates_to: [CA-O-135, CA-R-1508, CA-R-1519, CA-R-1525, CA-R-1438, CA-R-1728]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-133-CORE_META_MODEL-WORKFLOW--build-entities-graph.md
  source_atom_id: CA-O-133
  source_atom_revision: 2
  source_sha256: 17a2d268d16603d53bc963fdbfdac860eaa978bb78ea0d1096a4b29ebf12f780
  original_relations_sha256: 62ad6908f682e6a52ba0b7df9c1b962e3e1b8cb23b4cca4bbe96e49cfb6156d1
---
# Summary

Build Entities Graph

## Operation

Build Entities Graph **means** the reusable Workflow whose entry **and** only node is CA-O-135, the Entities Graph Construction Step. that Step owns its Action reference **and** invocation bindings; the Action owns construction behavior. the graph uses current Workflow execution authority under CA-R-1519 **and** exact definition Revisions under CA-R-1525.

### Graph scheme

| Entry/node | Result condition | Terminal outcome |
|---|---|---|
| CA-O-135 | built **or** no_op, with the Action's required current-selection, fidelity, validity **and** recording conditions satisfied | complete, preserving built versus no_op **and** the exact Projection/result references |
| CA-O-135 | incomplete, conflicting, stale **or** blocked | stop with that limitation **and** its affected frontier; request the missing evidence **or** authorization |
| CA-O-135 | reported built **or** no_op but **any** required completion condition is unmet **or** unsupported | blocked; retain the actual result **and** missing condition **without** accepting completion |
| CA-O-135 | failed | failed with actual effects **and** recovery evidence |
| CA-O-135 | canceled | canceled with actual effects **and** retained evidence |

there is no next-Step edge **or** automatic revisit. these are terminal outcomes, **not** extra nodes; no ON_RESULT Relation **to** an Action **or** terminal label is invented. a new attempt needs a separately admitted invocation; source discovery, a failed build **or** a no-op does **not** authorize a retry, source repair **or** automatic rebuild.

the Workflow Run retains the exact Step/Action bindings **and** its start/terminal Journal evidence under CA-R-1525, CA-R-1720 **and** CA-R-1728. an absent Workflow recording receipt prevents a complete Run claim even **when** a Projection was produced; retain the actual result **and** recording blocker **without** replaying construction.

## Details

this one-node scheme reuses CA-R-1438's graph kind. it is distinct from a particular build, a Tool **and** a source correction Workflow. a generic rebuild route **may** select this Workflow but does **not** force it **or** create another graph authority.
