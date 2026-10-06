---
atom_id: CA-O-155
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
  governs: "Applicable Methodology Compilation/Step: decide"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Obtain Source Correction Decision"
    - "Operator"
    - "Journal"
    - "Journal/Record"
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
    - "Project Configuration"
    - "Methodology Source/Expansion Boundary"
relations:
  relates_to: [CA-O-011, CA-O-007]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/APPLICABLE_METHODOLOGY_COMPILATION/CA-O-155-CORE_META_MODEL-STEP--obtain-the-applicable-methodology-correction-decision.md
  source_atom_id: CA-O-155
  source_atom_revision: 2
  source_sha256: 895f31fddd18894449f73321bf1fe3a26e4686a2a474a87ad0c2475812fadc12
  original_relations_sha256: 0327527080511193852b3621512152c3c6601254c66c43323355c91d8fe7ea35
---
# Summary

Obtain the Applicable Methodology correction decision

## Operation

this Step is the decide node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-007, Obtain Source Correction Decision.

### Inputs and parameters

bind the exact proposal from CA-O-154, conflict and source-frontier digest from CA-O-153, and the Workflow Run's required Operator approval context and canonical Journal reference.

enforce CA-R-1317 through CA-O-007: obtain **`=1`** unambiguous actual Operator approval **and** record it **in** the Journal, bound **to** the exact proposal, conflict, **and** source-frontier digest. stale, partial, missing, ambiguous, **or** mismatched approval does **not** qualify. do **not** create an approval Atom **in** Project Configuration; approval **must not** itself bypass Core expansion boundaries.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
