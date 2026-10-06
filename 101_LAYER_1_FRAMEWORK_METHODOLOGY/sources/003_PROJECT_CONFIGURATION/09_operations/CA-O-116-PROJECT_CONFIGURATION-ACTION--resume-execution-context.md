---
atom_id: CA-O-116
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
  governs: "Execution continuation context"
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
  relates_to: [CA-R-1808, CA-D-516]
---
# Summary

Load the remaining execution work

## Operation

Execution continuation context **means** the Programmatic Action implementing the following responsibility:

- derive remaining work from the saved initial checks and correction dispositions; compare source and criteria fingerprints and report drift before continuation.
- accept the declared inputs **and** return the declared results under CA-D-516-RESUME_EXECUTION_CONTEXT--encode-resume-execution-context-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
