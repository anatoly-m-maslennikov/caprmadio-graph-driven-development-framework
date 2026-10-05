---
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Journal/Record"
version: 4
updated_at: "2026-10-02 23:53:38 +0400"
relations: {}
atom_id: "CA-R-1510"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1510-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow-run.md
  source_atom_id: CA-R-1510
  source_atom_revision: 4
  source_sha256: df438330aa3b5e466eb347b17b935e2fbf426c258223eba7e6f53610864be562
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Workflow Run

## Scope

the Workflow Run entity.

## Claim

a Workflow Run **means** **`=1`** actual execution of **`=1`** Workflow against the inputs **and** parameters supplied for that run.

## Details

- the execution follows the Workflow's typed Relations **and** retains its actual Step Runs, outcomes, **and** applicable retry allowance.
- the run is distinct from the reusable Workflow **and** from the Journal Records that describe its execution. a reference **to** the definition does **not** prove that a run occurred.
