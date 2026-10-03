---
atom_id: CA-R-1622
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Action"
    - "Check Atoms"
    - "Atom"
    - "Implementation"
version: 4
updated_at: "2026-10-01 21:44:50 +0400"
relations:
  relates_to:
    - CA-O-087
    - CA-R-1516
    - CA-R-1517
    - CA-R-1519
---
# Summary

Implement Atom Carrier Validation **in** VALIDATE_ATOMS

## Scope

the `VALIDATE_ATOMS` Tool's implementation of the Check Atoms methodology Action.

## Claim

the `VALIDATE_ATOMS` Tool **must** implement **=1** methodology Action, Check Atoms under CA-O-087-CORE_META_MODEL-ACTION--check-atoms.

- that Action is the sole authority for operational behavior, selection, findings, **and** result meanings; the Tool's RMED specifies its Implementation **without** copying that authority.
- a Workflow invokes the Action through a Step; the Tool does **not** implement **or** own the Workflow graph **or** impose a Workflow on direct Action calls.
- return the Action's results faithfully, including failed **and** incomplete assessments; do **not** add repair, promotion, archive, **or** semantic-review behavior.
- this binding follows CA-R-1516-PROJECT_CONFIGURATION-REQUIREMENT--bind-each-tool-to-one-methodology-action **and** CA-R-1517-PROJECT_CONFIGURATION-REQUIREMENT--keep-tool-operational-authority-outside-its-own-subtree. this binding **must not** declare a new Scope Unit **or** require a particular Workflow **to** build the Tool.
- supported mechanical coverage **must** include Author membership **in** the Project's Operator registry **and** the current Content Role-specific body Property contracts. effective Plan Assignee resolution is deferred, **not** a membership check against this registry. distinguish an implemented check blocked by unavailable context from a deferred implementation; neither outcome establishes conformance.

## Details
