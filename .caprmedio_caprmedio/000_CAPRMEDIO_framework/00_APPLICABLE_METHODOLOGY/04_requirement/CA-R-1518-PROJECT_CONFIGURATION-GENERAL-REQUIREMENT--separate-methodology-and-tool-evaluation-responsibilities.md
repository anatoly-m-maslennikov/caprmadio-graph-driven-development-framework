---
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Methodology"
    - "Scope Unit"
    - "Action"
    - "Workflow"
    - "Step"
    - "Tool"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Evaluation For Relation"
version: 6
updated_at: "2026-10-03 00:00:32 +0400"
relations:
  relates_to: [CA-R-1018, CA-R-1514, CA-R-1515, CA-R-1516, CA-E-486]
atom_id: "CA-R-1518"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1518-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--separate-methodology-and-tool-evaluation-responsibilities.md
  source_atom_id: CA-R-1518
  source_atom_revision: 6
  source_sha256: 46f41ff287483bf65c3316c11b8b53e09caba44826d8676300efd295b41aa8a0
  original_relations_sha256: 90e68e44340b61b6cc4a017eb658d1ca7eff430492d717ab9ebe442dda294a0b
---
# Summary

Separate methodology and Tool Evaluation responsibilities

## Scope

Evaluation responsibility for operational definitions and their Tool implementations.

## Claim

**in** the CAPRMEDIO Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

## Details

- methodology source Scope Units own Evaluations of Action **and** Workflow definitions, including valid Action references, Step inputs, typed transitions, **and** termination **or** bounded retry conditions. these Evaluations **may** directly check O authority under CA-R-1018; checks for Steps **and** Runs reuse CA-E-486 **when** applicable.
- TOOLS **and** its Tool Scope Units own Evaluations of Tools: implementation behavior, interfaces, failures, **and** conformance **to** the Action implemented by the Tool. these Evaluations **must not** independently define the correctness rules of the referenced Action **or** Workflow.

checking whether a Tool realizes an Action correctly is distinct from checking whether that Action's definition is valid. a Tool test **may** use the methodology definition as its expected-behavior authority **without** taking ownership of definition validation.
