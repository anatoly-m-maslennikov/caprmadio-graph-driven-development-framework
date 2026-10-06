---
atom_id: CA-O-138
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Terms Graph Construction Step"
  depends_on: ["Step", "Action", "Workflow Run", "Step Run", "Step/Agentic Execution Context", "Projection/Type: Terms Graph"]
version: 1
updated_at: "2026-10-04 16:48:42 +0000"
relations:
  relates_to: [CA-O-136, CA-O-137, CA-R-1509, CA-R-1525, CA-R-1526, CA-R-1527]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-138-CORE_META_MODEL-STEP--construct-the-requested-terms-graph.md
  source_atom_id: CA-O-138
  source_atom_revision: 1
  source_sha256: 7fbffaea2fced0f5120805623cd6fcebc9bfaa34534cd23db7c71b54025e8005
  original_relations_sha256: 036e05260380041d7f441def4e3e87b1fd2a4c7d7560e5097b8bbcc6144973c8
---
# Summary

Construct the requested Terms Graph

## Operation

Terms Graph Construction Step **means** the node of CA-O-136 invoking **=1** Action, CA-O-137, with graph kind fixed **to** Terms Graph.

- bind the Action's admitted request, exact source selection, narrower/governed-only view selection **if** any, current authoritative source set, governing Term/Relation Kind authority, representation configuration, target Projection/output destination **and** existing Projection/evidence from the corresponding Workflow invocation inputs.
- bind permissions, admitted realization/execution kind **and** recording context from that invocation's current admitted execution context. retain actual Workflow/Step/Action definition Revisions **and** actual Run/parent references; no earlier completed Run **or** projected state supplies missing inputs.
- resolve execution kind under CA-R-1526. for an Agentic invocation, bind **=1** Integrated **or** Isolated context from the explicitly supplied Workflow runtime parameter under CA-R-1527; for Programmatic execution, no Agent context is selected. missing input, capability, permission **or** Agentic context blocks dispatch rather than silent substitution.
- return the Action's exact result/effects/evidence **to** CA-O-136 **without** copying construction behavior, changing scope, repairing sources **or** turning internal Tool calls into Steps.

## Details

this reusable binding is distinct from its Step Run. separately placed Workflow/Step Carriers retain unambiguous references under CA-D-467.
