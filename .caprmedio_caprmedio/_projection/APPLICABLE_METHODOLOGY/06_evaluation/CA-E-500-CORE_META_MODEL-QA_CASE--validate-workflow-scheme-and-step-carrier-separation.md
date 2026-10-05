---
subjects:
  governs: "Workflow/Carrier"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Directory Carrier"
    - "Atom Collection"
    - "Workflow/Relation Kind: On Result"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1570", "CA-R-1569", "CA-M-305", "CA-D-467"]}
atom_id: "CA-E-500"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-500-CORE_META_MODEL-QA_CASE--validate-workflow-scheme-and-step-carrier-separation.md
  source_atom_id: CA-E-500
  source_atom_revision: 4
  source_sha256: 5db4d560b31de1eb2de323baee397f35eb6dbd70e64bc2aca6e2844df6384156
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Workflow scheme and Step carrier separation

## Scope

Workflow representation; Step Carrier separation.

## Claim

the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.

## Details

- a graph references separate Step Atoms, **every** Step binds **`=1`** Action, **and** two Steps reuse that Action with different inputs: accept.
- place the graph **and** Steps **in** one folder **or** leave them separately addressable: retain the same graph meaning.
- reorder files **or** folder navigation **without** changing the graph: retain the declared execution order.
- copy Step bindings into the graph, copy Action behavior into a Step, introduce an unresolved Step reference, **or** create another Workflow identity for the folder: reject.
- **when** using a folder-backed Workflow, require **`=1`** graph Atom Carrier **and** separately carried Step Atoms; reject a folder that silently becomes their owning Scope Unit.
