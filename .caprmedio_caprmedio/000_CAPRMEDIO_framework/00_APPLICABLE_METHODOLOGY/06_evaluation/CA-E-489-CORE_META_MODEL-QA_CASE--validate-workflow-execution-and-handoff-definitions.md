---
subjects:
  governs: "Workflow"
  depends_on:
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Workflow/Relation Kind: On Result"
    - "Artifact/Revision"
    - "Operator"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1519", "CA-R-1520"]}
atom_id: "CA-E-489"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-489-CORE_META_MODEL-QA_CASE--validate-workflow-execution-and-handoff-definitions.md
  source_atom_id: CA-E-489
  source_atom_revision: 5
  source_sha256: 649fc2ca1ffca21d2aeceb31611f41a06fe7dc2627644241fdabc540acaeeae1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Workflow execution and handoff definitions

## Scope

a Workflow's declared execution **and** handoff behavior.

## Claim

the Evaluation **must** check whether a Workflow's declared execution **and** handoff behavior is well formed under CA-R-1519 **and** CA-R-1520, independently of current executor availability.

## Details

### Cases and expected results

- complete input declarations, resolvable Action references, admitted transitions, explicit terminal outcomes, **and** declared capability requirements: pass this definition check **without** requiring a running executor.
- a missing required input declaration, unresolved definition reference, missing continuation-selection rule, **or** absent applicable approval condition: reject the affected definition.
- a well-formed definition whose selected executor lacks a declared capability, worker, **or** current permission: the definition remains valid; execution admission is blocked under CA-R-1519. do **not** report unavailable execution as malformed authority.
- a missing invocation input **or** runtime resource is an execution-admission problem rather than a definition defect **when** its required binding is correctly declared.
- a terminal handoff declares the target Revision, complete continuation inputs, reason, check evidence, **and** performed-effect account: accept its declared continuation boundary.
- a handoff definition resumes predecessor Steps, claims successor success **before** execution, bypasses approval, resets retries, **or** admits an unbounded continuation cycle: reject.
- a cross-Workflow ON_RESULT Step edge offered as a Run handoff: reject; the two relations have different endpoints **and** responsibilities.

report the exact failing source **and** condition. definition validity **must not** be reported as permission, execution readiness, successful execution, **or** evidence that a Run occurred.
