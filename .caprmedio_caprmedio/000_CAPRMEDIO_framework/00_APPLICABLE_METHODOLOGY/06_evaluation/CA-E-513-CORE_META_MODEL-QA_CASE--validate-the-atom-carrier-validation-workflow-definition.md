---
atom_id: CA-E-513
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom Carrier Validation"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow/Relation Kind: On Result"
    - "Evaluation"
version: 4
updated_at: "2026-10-01 21:33:03 +0400"
relations:
  evaluation_for:
    - CA-O-080
    - CA-O-087
    - CA-O-088
  relates_to:
    - CA-E-486
    - CA-E-494
    - CA-E-500
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-513-CORE_META_MODEL-QA_CASE--validate-the-atom-carrier-validation-workflow-definition.md
  source_atom_id: CA-E-513
  source_atom_revision: 4
  source_sha256: 47e76173ba795804a5e43e741dbdbd98fef65836dc5911d0ae8ccc7734b2d234
  original_relations_sha256: 91a4a2fe7a294276f2535d8e32319a5bc8c8b12b3ddcfd793eb4bdb6a9f79774
---
# Summary

Validate the Atom Carrier Validation Workflow definition

## Scope

the Atom Carrier Validation Workflow definition.

## Claim

the Atom Carrier Validation definition check **must** reject a graph **or** binding that cannot preserve its declared read-only assessment boundary.

- require **=1** entry **and** **=1** Step node, a resolvable Step reference, **=1** Action per Step, explicit compatible input bindings, **and** admitted Workflow-scoped transitions.
- require reachable terminal outcomes for incomplete, invalid, valid, **and** execution-error cases as defined by the referenced Action; **none** of the outcomes **may** be silently mapped **to** valid.
- verify that this graph is acyclic, contains no implicit retry **or** repair, **and** does **not** duplicate Action behavior inside its Step bindings **or** graph.
- verify that findings do **not** prevent assessment of independent targets, while missing authority **or** changed inputs cannot become proof of conformance.
- reference current self-sufficiency **and** source-binding Evaluations for the checked conditions; definition conformance **must not** be reported as a successful Tool execution.

## Details
