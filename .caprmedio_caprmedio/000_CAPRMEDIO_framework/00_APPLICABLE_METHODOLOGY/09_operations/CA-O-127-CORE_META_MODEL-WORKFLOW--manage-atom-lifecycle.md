---
atom_id: CA-O-127
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow"
  depends_on: ["Step", "Workflow Run", "Workflow/Relation Kind: On Result", "Operator", "Journal"]
version: 3
updated_at: "2026-10-05 01:39:17 +0000"
relations:
  relates_to: [CA-O-129, CA-O-145, CA-M-303, CA-R-1508, CA-R-1513, CA-R-1520, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-127-CORE_META_MODEL-WORKFLOW--manage-atom-lifecycle.md
  source_atom_id: CA-O-127
  source_atom_revision: 3
  source_sha256: 6daf77356ac8bac44e252a546aa1e34a7c02558dc1aa4e6b428cb0b15283fd67
  original_relations_sha256: fcfcc4b2dbb8fc1a8cac622227d404f20f79bf31f172624b9f4b4103aa62748d
---
# Summary

Manage atom lifecycle

## Operation

One reusable parameterized Workflow graph binds Create Atom, Update Atom, Replace Atom and Change Atom Status. Archive is only a Change Status shortcut admitted by the applicable model, not another Workflow. The Step definitions own all Action and input bindings.

Each invocation admits exactly one Create target or one existing current target/predecessor, with its complete required Carrier set. Replace retains the complete accepted set of >=1 distinct successors for that one predecessor, not additional predecessors. A request naming multiple independent targets/predecessors ends blocked before Step dispatch or effects; bulk callers expand their requests into separate individually admitted Runs of this same Workflow, with fresh exact inputs/assessment/permission bindings for each.

### Nodes and entry

The graph has exactly two Step nodes: CA-O-145 and CA-O-129. An admitted Update request enters CA-O-145; admitted Create, Replace or Change Status requests enter CA-O-129. Unsupported request kinds end blocked without an effect.

### Typed transitions and terminal results

| Source Step result | Workflow-owned scheme |
| --- | --- |
| O145: identity-preserving | ON_RESULT O145→O129, subject to current authorization, compatible exact assessment and effect admission. |
| O145: replacement-required | End this Run with an R1520 terminal handoff to the Replace entry of CA-O-127 in a separately admitted Run. Do not call/wait for replacement, perform an intermediate update or treat the handoff as replacement permission. |
| O145: unresolved, invalid, stale, unauthorized or unavailable | End blocked with the exact evidence/decision gap; no approval inferred. |
| O129: reassessment-required for Update | ON_RESULT O129→O145 only with an explicitly admitted fresh proposal/evidence binding and remaining applicable retry allowance. Without them end blocked. |
| O129: applied or no-op | End complete only for the exact admitted boundary with verified results and all required durable Run/change receipts; no-op reports no Artifact change. |
| O129: invalid, stale, unauthorized, unsupported, blocked, recording-blocked, failed, partial or canceled | End with that truthful non-complete outcome, actual completed/incomplete effects and recoverable evidence; no automatic replay. |

The two ON_RESULT edges have Step endpoints in this Workflow. No other route, implicit retry, continuation, graph node or Action-selected successor is admitted. A changed definition pauses dispatch for R1525 revalidation; completed effects and retry accounting remain retained.

## Details

Reuse O067 identity assessment through O145 and O051 accepted replacement persistence through the effect Action. The graph neither duplicates those behaviors nor owns their bindings. A Summary change always follows the replacement-required terminal route; a changed proposal or stale evidence requires reassessment before update persistence.

The separately admitted successor obtains fresh definition/input/permission bindings. Required pending replacement is not reported complete. Change Status resolves the actual current Atom, then its complete Content Role and optional Type-qualified model: use the applicable existing whitelist and transition rule under R1521/R1308, including current Operations R1874 and Analysis R1875 role bindings, not a Workflow list. A more-specific declared Role/Type model overrides its role model; otherwise the role model applies without duplicated Type value sets. A same current status is a no-op. Archive is only a shortcut when that qualified model explicitly defines an archival status; otherwise archive ends missing-archival-model/unsupported without mapping Concern resolved or canceled to archival meaning.

Every Workflow/Step/Action Run, including referenced Action executions, standalone use, nested lineage, failure/cancellation and no-op, retains exact definitions/inputs, parent references, start/terminal/result/effect evidence in the one authoritative Journal under R1720/R1525 and applicable Run policy. Missing durable receipts are recording-blocked, not journaled success. No secret or competing history store is introduced. This is a source graph, not evidence of implementation, MCP, prompt or runtime execution.
