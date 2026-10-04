---
version: 5
updated_at: "2026-10-02 23:35:16 +0400"
relations:
  child_of:
    - CA-R-815
subjects:
  governs: "Project/priority model application"
  depends_on:
    - "Operator"
    - "Project"
    - "Scope"
    - "CAPRMEDIO Framework Instance"
atom_id: "CA-R-1487"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1487-CORE_META_MODEL-REQUIREMENT--follow-the-operator-selected-priority-model.md
---
# Summary

Follow the Operator-selected priority model

## Scope

priority-model selection by the CAPRMEDIO Framework Instance for an affected Scope and Project stage.

## Claim

the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:

- respect applicable authority **and** non-negotiable constraints.
- conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
- remain unresolved **if** the selected model **or** its application does **not** justify a selection.

## Details

the available criteria **and** comparison techniques remain extensible; no fixed criterion set **or** comparison by priority order is mandatory.
