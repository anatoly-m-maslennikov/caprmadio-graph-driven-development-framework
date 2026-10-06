---
atom_id: CA-O-088
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Check Atoms Step"
  depends_on:
    - "Step"
    - "Action"
    - "Check Atoms"
    - "Workflow Run"
version: 3
updated_at: "2026-10-04 15:14:54 +0000"
relations:
  relates_to:
    - CA-O-087
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/ATOM_CARRIER_VALIDATION/CA-O-088-CORE_META_MODEL-STEP--check-selected-atoms.md
  source_atom_id: CA-O-088
  source_atom_revision: 3
  source_sha256: d8701707d07be609e8cff2177322fcb66b6b54fb190b29d1bbd73b8c12b8754f
  original_relations_sha256: 94ed4306247b86e5e0ce0e5e32ec1a0ecc5092eeb2b491198ee7160e2f32e98a
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
