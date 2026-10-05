---
atom_id: CA-O-156
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 17:42:12 +0000"
subjects:
  governs: "Applicable Methodology Compilation/Step: correct"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Apply Approved Source Corrections"
    - "Operator"
    - "Journal/Record"
    - "Methodology Source"
    - "Atom/Claim"
relations:
  relates_to: [CA-O-011, CA-O-008]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/APPLICABLE_METHODOLOGY_COMPILATION/CA-O-156-CORE_META_MODEL-STEP--apply-approved-applicable-methodology-source-corrections.md
  source_atom_id: CA-O-156
  source_atom_revision: 2
  source_sha256: 66ad7ecaf6fcaa3368539f464be8345818f71135d85d3e9f9d96c2ba7b32e822
  original_relations_sha256: 096b0599580a28c8c6f7e0bdc2d9f2defb1fb2b6089cf791e3f3adfc1be1f947
---
# Summary

Apply approved Applicable Methodology source corrections

## Operation

this Step is the correct node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-008, Apply Approved Source Corrections.

### Inputs and parameters

bind the exact approved correction and recorded decision from CA-O-155, their selected frontier, and the Workflow Run's current source state and separately authorized owning-source change workflow.

require the separately authorized source change workflow; corrections are **not** compiler side effects **or** edits **to** projected Claims. **if** **any** source changes, the Workflow Run returns **to** select **and** repeats assessment against the new frontier. failure **or** partial effects never justify publishing from the earlier assessment.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
