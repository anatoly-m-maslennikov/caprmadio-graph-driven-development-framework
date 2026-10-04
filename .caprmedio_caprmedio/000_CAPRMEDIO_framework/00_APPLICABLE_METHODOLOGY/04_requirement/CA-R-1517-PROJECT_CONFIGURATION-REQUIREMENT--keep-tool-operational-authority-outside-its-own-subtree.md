---
subjects:
  governs: "Tool"
  depends_on:
    - "Scope Unit"
    - "Action"
    - "Workflow"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
    - "Methodology"
version: 4
updated_at: "2026-10-03 00:00:05 +0400"
relations:
  relates_to: [CA-R-1515, CA-R-1516, CA-R-1518]
atom_id: "CA-R-1517"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1517-PROJECT_CONFIGURATION-REQUIREMENT--keep-tool-operational-authority-outside-its-own-subtree.md
---
# Summary

Keep Tool operational authority outside its own subtree

## Scope

Tools' implementation references to methodology Action and Workflow definitions in the caprmedio Project.

## Claim

**in** the caprmedio Project, a Tool's implementation reference **to** a methodology Action **or** Workflow definition **must not** target an O Atom owned by the Tool's Scope Unit **or** **any** descendant of that Scope Unit.

## Details

- the restriction concerns the owner of the operational definition, **not** the location of the Tool's code, prompts, **or** runtime results.
- methodology Evaluations of their own Action **and** Workflow definitions under CA-R-1518 are **not** Tool implementation references **and** are **not** prohibited by this rule.

this restriction prevents self-reference through the Tool's own subtree; it does **not** establish that **all** indirect dependency cycles are absent.
