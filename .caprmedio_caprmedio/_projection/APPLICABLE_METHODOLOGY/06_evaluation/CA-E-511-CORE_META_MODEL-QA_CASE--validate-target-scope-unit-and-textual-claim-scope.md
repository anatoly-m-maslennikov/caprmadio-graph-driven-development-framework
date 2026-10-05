---
atom_id: CA-E-511
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Revision/Author"
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Subjects"
    - "Current-scope Atom"
    - "Hub Atom"
    - "Operator"
    - "Relational Atom"
    - "Scope Unit"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations:
  evaluation_for:
    - CA-D-482
    - CA-D-495
    - CA-R-1271
    - CA-R-1588
    - CA-R-1595
    - CA-R-1596
    - CA-R-922
    - CA-R-923
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-511-CORE_META_MODEL-QA_CASE--validate-target-scope-unit-and-textual-claim-scope.md
  source_atom_id: CA-E-511
  source_atom_revision: 5
  source_sha256: 7d1a04cabf809fd37379b0367ad0d4732c130e13257a1fb427f3a5d5053197bd
  original_relations_sha256: be5737b9afecc383c01dacfa16b2124d01728c40cbd6c601be94031bfc56f4c4
---
# Summary

Validate Target Scope Unit **and** textual Claim Scope

## Scope

the distinction between an Atom's Claim Target Scope Unit **and** its textual applicability.

## Claim

### Claim checked

**every** Atom resolves **`=1`** Claim Target Scope Unit; its Claim Scope remains applicability restrictions **in** the body sections registered by CA-D-495, including Scope for RMED, **not** another structural target **or** frontmatter Property.

## Details

### Test case

create a Current-scope Atom with its own Scope Unit explicitly carried as target **and** a Claim restricted **to** Python files; repeat with a composite restriction. for RMED, carry those restrictions **in** Scope **and** the qualified contribution **in** Claim. create a permitted Demand with a different explicit target, a parent-owned Goal for its direct child, an external Project Goal with its Author's registered Operator name **and** an explicit Project target, **and** a Plan inside nested Hubs. **then** omit the internally required target even **when** filename **or** placement identifies its owner, provide two targets, use a Hub as a target, leave the target unresolved, duplicate textual applicability **in** frontmatter, **or** infer a target **or** ownership change from the textual restriction alone.

### Acceptance criteria

valid targets resolve **to** **`=1`** Scope Unit. authoring defaults select **and** carry the current Scope Unit **where** one exists; reading does **not** repair an omitted target from placement; external Project Goals retain their explicit target. narrower **or** composite applicability alone leaves a Current-scope Atom Current-scope. a different permitted target yields a Relational Atom **without** transferring ownership **or** changing Scope Unit ancestry. Hub nesting does **not** create another target. **every** invalid fixture fails with the exact missing, unresolved, duplicate, misclassified, **or** independently duplicated fact identified.

### Failure disposition

report the affected Atom **and** target, ownership, **or** textual-applicability distinction; preserve the source **until** an authorized correction is selected.
