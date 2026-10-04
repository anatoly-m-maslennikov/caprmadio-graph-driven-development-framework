---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Action/Execution Kind"
    - "Step/Agentic Execution Context"
    - "Artifact/Revision"
    - "Operator"
    - "Journal"
version: 1
updated_at: "2026-09-30 14:53:54 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1790"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1790-CORE_META_MODEL-GENERAL--retain-agentic-step-executor-state-and-routing.md
---
# Summary

Retain Agentic Step executor state **and** routing

## Scope

execution coordination during dispatch **or** resumption of an Agentic Step, involving the executor together with the participating session **or** separate Agent context.

## Claim

the executor **must** retain execution state **and** select subsequent Steps from the Workflow's declared transitions. the participating session **or** separate Agent context performs the requested Action; it need **not** reconstruct **or** remember what the Workflow will do next.

## Details
