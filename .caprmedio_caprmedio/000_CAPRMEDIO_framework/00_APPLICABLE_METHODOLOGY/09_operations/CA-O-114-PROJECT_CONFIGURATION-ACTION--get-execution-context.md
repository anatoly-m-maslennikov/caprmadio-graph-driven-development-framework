---
atom_id: CA-O-114
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Execution context retrieval"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-R-1806, CA-D-514]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-114-PROJECT_CONFIGURATION-ACTION--get-execution-context.md
  source_atom_id: CA-O-114
  source_atom_revision: 1
  source_sha256: 314c5ac508959890dcb7757184a925b054456a21a4575f42101cf74240db36e2
  original_relations_sha256: e6325c890d179989bbd8c94e53cbb02bf379c2030f29acebc9e7aad4008c6918
---
# Summary

Load the selected execution context

## Operation

Execution context retrieval **means** the Programmatic Action implementing the following responsibility:

- resolve exact identifiers; load the selected definition and directly related Step or Action definitions, relevant bound prompts, and applicable RMED from declared Scope Unit ancestry.
- accept the declared inputs **and** return the declared results under CA-D-514-GET_EXECUTION_CONTEXT--encode-get-execution-context-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
