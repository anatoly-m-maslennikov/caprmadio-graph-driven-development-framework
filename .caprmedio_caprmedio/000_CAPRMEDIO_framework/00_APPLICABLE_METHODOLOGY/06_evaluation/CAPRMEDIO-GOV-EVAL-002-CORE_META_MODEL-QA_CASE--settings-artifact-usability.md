---
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Project Settings"
    - "Project Structure"
    - "Authority Mode"
    - "Operator"
version: 21
updated_at: "2026-10-01 21:46:54 +0400"
relations:
  evaluation_for:
    - CA-R-1052
    - CA-R-1402
    - CA-R-1750
    - CA-R-1430
atom_id: "CAPRMEDIO-GOV-EVAL-002"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-002-CORE_META_MODEL-QA_CASE--settings-artifact-usability.md
  source_atom_id: CAPRMEDIO-GOV-EVAL-002
  source_atom_revision: 21
  source_sha256: 7e8309975d3e47a7bd4e1ab527e3ceeb29ef4fef0ac6c6bb1cc46c6ec70e3de4
  original_relations_sha256: 3dfd518c3330ae94fcc8dd981299feea6bbeed261b4bb583a2ca981d3b03d929
---
# Summary

Settings Artifact Usability

## Scope

the Operator has no undocumented Framework knowledge **and** **must not** edit the Framework Catalog.

## Claim

an Operator unfamiliar with the repository can configure framework-instance behavior, including default **and** Project Authority Modes, through Framework Instance Settings **and** Project initialization inputs through Project Settings using the owning Settings Artifacts **and** their in-file documentation, while recognizing authoritative Project Structure as the separate owner of Scope Unit declarations **and** explicit per-unit Authority Mode overrides. no structural Projection is required **to** make these choices.

## Details

### Acceptance criteria

**every** intended change is made through its owning Settings Artifact **or** Project Structure, **and** **`>=90`**% of classifications correctly distinguish project choices from methodology definitions.

### Failure disposition

record a Concern for **every** misleading **or** missing setting instruction **and** stop settings-usability readiness **until** it is corrected.
