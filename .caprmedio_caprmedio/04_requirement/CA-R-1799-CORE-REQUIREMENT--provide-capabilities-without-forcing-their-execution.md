---
atom_id: CA-R-1799
content_role: Requirement
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Core
global_tier: 1
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-30 21:46:00 +0000"
subjects:
  governs: "CAPRMEDIO Framework Instance/capabilities"
  depends_on:
    - "CAPRMEDIO Framework Instance"
    - "Operator"
    - "Atom/Content Role: Requirement"
    - "Workflow"
    - "Action"
relations:
  child_of:
    - CA-P-033
---
# Summary

Provide capabilities **without** forcing their execution

## Scope

capabilities provided by the CAPRMEDIO Framework Instance.

## Claim

the CAPRMEDIO Framework Instance **must** provide capabilities for the Operator **without** initiating **or** forcing their execution independently of Operator authorization.

## Details

- a Requirement **to** provide a capability specifies what is available **to** the Operator; it does **not** itself authorize **or** trigger execution.
- execution follows direct Operator instruction **or** explicit prior authorization. prior authorization **may** cover a Workflow **or** automation **and** its Actions within the authorized targets **and** constraints; separate approval for **every** covered Action is **not** required.
- required outcomes, validation gates, **and** safeguards remain binding **when** an authorized capability executes. capability wording does **not** make those conditions optional.
