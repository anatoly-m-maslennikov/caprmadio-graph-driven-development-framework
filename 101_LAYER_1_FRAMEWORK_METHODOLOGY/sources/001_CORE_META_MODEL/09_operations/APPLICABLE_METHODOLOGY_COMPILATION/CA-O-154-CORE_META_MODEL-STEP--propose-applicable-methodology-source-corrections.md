---
atom_id: CA-O-154
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
  governs: "Applicable Methodology Compilation/Step: propose"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Propose Source Corrections"
    - "Methodology Source"
    - "Atom/Claim"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
    - "Methodology Source/Expansion Boundary"
relations:
  relates_to: [CA-O-011, CA-O-006]
---
# Summary

Propose Applicable Methodology source corrections

## Operation

this Step is the propose node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-006, Propose Source Corrections.

### Inputs and parameters

bind the assessment, conflicts and exact frontier returned by CA-O-153, together with the Workflow Run's authorized correction boundaries and owning source authority.

propose needed changes **only** through the separately authorized workflow of the owning source authority. source order, Claim synthesis, Claim merge, **and** LLM inference **must not** resolve a conflict. a prohibited Extension **or** Project Configuration override **must not** become conforming **without** an authorized change **to** its governing Core authority.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
