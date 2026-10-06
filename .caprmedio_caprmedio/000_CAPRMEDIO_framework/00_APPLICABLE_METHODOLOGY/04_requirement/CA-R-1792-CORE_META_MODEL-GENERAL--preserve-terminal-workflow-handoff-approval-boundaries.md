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
atom_id: "CA-R-1792"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1792-CORE_META_MODEL-GENERAL--preserve-terminal-workflow-handoff-approval-boundaries.md
  source_atom_id: CA-R-1792
  source_atom_revision: 1
  source_sha256: 95d53e72f4b4f7e0542d39003b818ccf48645a2c5e98b43accd889c6fa113180
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve terminal Workflow handoff approval boundaries

## Scope

a terminal Workflow handoff from an Agentic Step Invocation.

## Claim

a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.

## Details
