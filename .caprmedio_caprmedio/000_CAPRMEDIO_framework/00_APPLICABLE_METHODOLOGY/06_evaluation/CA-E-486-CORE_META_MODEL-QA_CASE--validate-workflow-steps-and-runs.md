---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Step Run"
    - "Workflow/Relation Kind: On Result"
    - "Journal/Record"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1508", "CA-R-1509", "CA-R-1510", "CA-R-1511", "CA-R-1513"]}
atom_id: "CA-E-486"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-486-CORE_META_MODEL-QA_CASE--validate-workflow-steps-and-runs.md
  source_atom_id: CA-E-486
  source_atom_revision: 4
  source_sha256: 051c30b75fbb740681b93ec65f81982fa7dc1f7b542117a5b0a9fa36a994023c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Workflow Steps and Runs

## Scope

Workflow Steps **and** Runs.

## Claim

the Evaluation **must** check Workflow Steps **and** Runs.

## Details

### Cases

- define **`=2`** distinct Steps referencing the same Action with different input bindings; follow an admitted conditional transition between the Steps.
- revisit a Step under an accepted retry allowance within **`=1`** Workflow Run.
- introduce a Step with **`=0`** Action references, **`>1`** Action references, an unresolved Action, **or** an unresolved required input binding.
- introduce an untyped edge, an edge whose endpoint is an Action rather than a Step, **or** a next-Step reference missing from that Workflow.
- record a failed Step Run; separately reference a reusable Workflow definition **without** recording an execution.

### Acceptance

- the valid shared Action retains **`=1`** definition; Step bindings remain distinct.
- **every** actual revisit creates a distinct Step Run within the same Workflow Run **without** resetting its retry allowance.
- invalid Action cardinality, unresolved inputs, invalid endpoints, **and** untyped transitions fail the check.
- failed **or** absent execution evidence **must not** become successful completion, a new Workflow definition, **or** another historical source.

report the exact failing source, case, **and** condition; do **not** change source authority **to** make the check pass.
