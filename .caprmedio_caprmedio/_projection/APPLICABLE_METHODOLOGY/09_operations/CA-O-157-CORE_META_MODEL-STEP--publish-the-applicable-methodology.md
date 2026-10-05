---
atom_id: CA-O-157
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
  governs: "Applicable Methodology Compilation/Step: publish"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Publish Reconciled Projection"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
    - "Carrier"
    - "Projection/Type: Reconciled Projection"
relations:
  relates_to: [CA-O-011, CA-O-009]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/APPLICABLE_METHODOLOGY_COMPILATION/CA-O-157-CORE_META_MODEL-STEP--publish-the-applicable-methodology.md
  source_atom_id: CA-O-157
  source_atom_revision: 2
  source_sha256: 4007710401af00358dcaf1c04aaa2f62ed396ef9471d74d7940fb35dcafad1c4
  original_relations_sha256: 3d58154a85585cabe11495d37bd8fd0904c638157cd48404ac517de5e5709123
---
# Summary

Publish the Applicable Methodology

## Operation

this Step is the publish node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-009, Publish Reconciled Projection.

### Inputs and parameters

bind the final reassessed source frontier from CA-O-153, the corresponding selection from CA-O-152, required valid decisions from CA-O-155 when applicable, and the Workflow Run's selected Projection Delivery authority.

preserve **every** selected Atom ID, exact source Revision, authority owner, **and** Claim under CA-R-1314 **and** CA-R-1316; enforce CA-R-1461 **and** CA-D-305 **and** CA-D-306 source identity, exact source Carrier bytes **and** Carrier form. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** required approval is invalid. produce the same ordered Applicable Methodology membership from the same resolved source frontier.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
