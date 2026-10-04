---
atom_id: CA-O-135
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entities Graph Construction Step"
  depends_on: ["Step", "Action", "Workflow Run", "Step Run", "Step/Agentic Execution Context", "Projection/Type: Entities Graph"]
version: 1
updated_at: "2026-10-04 16:48:42 +0000"
relations:
  relates_to: [CA-O-133, CA-O-134, CA-R-1509, CA-R-1525, CA-R-1526, CA-R-1527]
---
# Summary

Construct the requested Entities Graph

## Operation

Entities Graph Construction Step **means** the node of CA-O-133 invoking **=1** Action, CA-O-134, with graph kind fixed **to** Entities Graph.

- bind the Action's admitted request, exact source selection, narrower display selection **if** any, current authoritative source set, governing source/Relation Kind authority, representation configuration, target Projection/output destination **and** existing Projection/evidence from the corresponding Workflow invocation inputs.
- bind permissions, admitted realization/execution kind **and** recording context from that invocation's current admitted execution context. retain actual Workflow/Step/Action definition Revisions **and** actual Run/parent references; no previously completed Run **or** projected state supplies missing inputs.
- resolve execution kind under CA-R-1526. for an Agentic invocation, bind **=1** Integrated **or** Isolated context from the explicitly supplied Workflow runtime parameter under CA-R-1527; for Programmatic execution, no Agent context is selected. missing input, capability, permission **or** Agentic context blocks dispatch rather than silently substituting a realization.
- return the Action's exact result/effects/evidence **to** CA-O-133 **without** copying construction behavior, changing scope, repairing sources **or** turning internal Tool calls into Steps.

## Details

this reusable binding is distinct from its Step Run. the separately placed Workflow/Step Carriers retain unambiguous references under CA-D-467.
