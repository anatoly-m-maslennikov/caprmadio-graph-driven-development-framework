---
subjects:
  governs: "Assess Source Conflicts"
  depends_on:
    - "Action"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Atom/Global Tier"
    - "Atom/Revision/Updated At"
    - "Atom/Local Tier: Principle"
    - "Operator"
version: 8
updated_at: "2026-10-04 15:07:08 +0000"
relations: {}
atom_id: "CA-O-005"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-005-CORE_META_MODEL-ACTION--assess-source-conflicts.md
  source_atom_id: CA-O-005
  source_atom_revision: 8
  source_sha256: 99f3aba94cc96ca3be174c140d818b2cb72bce348338c52ffbe56945e387510c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Assess source conflicts

## Operation

Assess Source Conflicts **means** the reusable Action that assesses one exact selected source frontier against its applicable authority **and** returns the conflict assessment **without** changing sources.

1. load the current accepted active authority **and** applicable Project Principles **before** relying on an earlier report **or** proposed fix.
2. identify the conflicting Claims **and** their applicability. for RMEDO Atoms, collect Global Tier, exact Revision, **and** Updated At. distinguish an actual conflict from different permitted cases.
3. for RMEDO conflicts, preserve higher-tier authority, whose Global Tier number is lower. within the applicable authority boundaries, prefer the freshest accepted active Claim over a conflicting older Claim; Updated At **must not** permit a lower-tier Claim **or** prohibited source override **to** defeat higher-tier authority.
4. check **every** proposed disposition against the active Principles **and** retain the evidence for its effect on alignment. a conflict between active Principles requires the Operator under CA-R-1551.
5. distinguish resolved, unresolved, **and** unevaluated conditions. report missing checks, uncertain applicability, equal **or** ambiguous timestamps, **and** unresolved authority **without** inventing precedence.
6. verify required resolution evidence against the exact proposal **and** current source frontier. missing, stale, partial, ambiguous, **or** mismatched approval **or** delegation does **not** resolve a conflict.

7. check affected authority coverage, including still-required Claims, active references **and** Relations, **and** required Evaluations. report an unresolved gap separately from a resolved conflict; absence of a conflict does **not** prove complete coverage.

this Action **must not** synthesize **or** merge Claims, treat an LLM judgment as Operator authorization, change source **or** projected content, **or** silently exclude a conflicting source from the assessment.

## Details
