---
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Atom/Claim"
    - "Action"
    - "Workflow"
    - "Step"
    - "Implementation"
    - "Carrier"
version: 5
updated_at: "2026-09-29 22:52:10 +0000"
relations: {"evaluation_for": ["CA-R-1548", "CA-R-1549", "CA-R-1550", "CA-R-1339", "CA-R-1340", "CA-R-1343", "CA-R-1530", "CA-R-1569"]}
atom_id: "CA-E-498"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-498-CORE_META_MODEL-QA_CASE--validate-specification-change-and-implementation-classification.md
  source_atom_id: CA-E-498
  source_atom_revision: 5
  source_sha256: dcef550f7b655a5c5d55a8ecdd3a078df436974278faebd86f6bdde97f29a8a5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Validate Specification, Change, and Implementation classification

## Scope
classification of an Atom by its Content Role.

## Claim
the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification, Change, **and** Implementation definitions.

- use the evaluated Atom's declared Content Role, complete Main Content, **and** applicable Specification, Change, **and** Implementation definitions as the input evidence.
- compare the declared Content Role with the contribution expressed **in** that Main Content, using the following classification table.
- report unresolved **when** required evidence is unavailable, unresolved, **or** contradictory; **otherwise**, report pass **if** the declared Content Role matches the observed contribution **and** fail **if** it does **not**.
- identify the evaluated Atom **and** report the declared Content Role, relevant content excerpt, applicable definition, **and** comparison result.

| Claim contribution | Expected classification |
|---|---|
| a model definition, required property, **or** permission governing a Concern, Analysis, Task, Action, **or** Workflow | Requirement |
| a convention for authoring **or** constructing that content | Method |
| a falsifiable correctness check | Evaluation |
| a Carrier's fields, format, **or** placement | Delivery |
| a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis, **or** Plan role |
| a particular reusable Action behavior, Workflow graph, Step invocation binding, **or** Actor participation/authorization behavior | Operations |
| a current realization of accepted specification | Implementation |

reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.

## Details
