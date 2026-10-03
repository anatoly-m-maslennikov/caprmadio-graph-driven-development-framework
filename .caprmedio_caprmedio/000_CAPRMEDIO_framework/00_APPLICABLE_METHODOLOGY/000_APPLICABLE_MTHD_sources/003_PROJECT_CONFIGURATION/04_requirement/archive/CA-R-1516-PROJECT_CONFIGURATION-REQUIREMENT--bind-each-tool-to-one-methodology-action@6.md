---
subjects:
  governs: "Tool"
  depends_on:
    - "Action"
    - "Workflow"
    - "Step"
    - "Methodology"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Spec"
version: 6
updated_at: "2026-10-03 05:59:00 +0400"
relations:
  relates_to: [CA-R-1452, CA-R-1509, CA-R-1514, CA-R-1515, CA-R-1517]
atom_id: "CA-R-1516"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind each Tool to one methodology Action

## Scope

Tools in the caprmedio Project.

## Claim

**in** the caprmedio Project, **every** Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom.

## Details

- the Tool's RMED identifies that Action as the behavior it realizes **and** specifies its implementation obligations **without** copying the canonical Action definition.
- a Workflow Step binds its Action under CA-R-1509; the corresponding Tool realizes that Action rather than redefining the Workflow graph.
- this cardinality constrains the Action implemented by the Tool. it does **not** count internal instructions, API calls, interactions, **or** retries.

the binding is **not** a requirement **to** use that Action **or** a particular Workflow **to** build the Tool.
