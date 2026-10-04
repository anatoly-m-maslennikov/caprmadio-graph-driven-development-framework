---
subjects:
  governs: "Step"
  depends_on:
    - "Workflow"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Step Run"
    - "Action/Execution Kind"
    - "Step/Agentic Execution Context"
    - "Tool"
version: 6
updated_at: "2026-10-02 23:53:38 +0400"
relations: {"relates_to": ["CA-R-1569"]}
atom_id: "CA-R-1509"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1509-CORE_META_MODEL-CORE-REQUIREMENT--define-step.md
---
# Summary

Define Step

## Scope

the Step entity.

## Claim

a Step **means** a node **in** a Workflow, defined by **`=1`** Step Atom, that specifies invocation of **`=1`** Action with the parameters **and** inputs for that invocation.

## Details

- the binding identifies the source of **every** required input **or** parameter, including a Workflow input **or** an earlier Step result **when** applicable; it need **not** fix runtime values **in** the definition.
- different Steps **may** reference the same Action with different bindings **without** copying **or** redefining that Action.
- an Agentic invocation selects Integrated **or** Isolated context under CA-R-1527; a Programmatic invocation does **not** acquire an Agent context by this rule.
- the Step definition is distinct from its referenced Action **and** from a Step Run. internal Tool calls remain execution details under CA-R-1528, **not** additional Step definitions.
