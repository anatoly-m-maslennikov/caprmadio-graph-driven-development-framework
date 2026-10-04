---
subjects:
  governs: "Journal"
  depends_on:
    - "Core Meta-Model"
    - "Extension"
    - "Projection/Type: Artifact Change Log"
    - "Projection/Type: Process Log"
version: 7
updated_at: "2026-10-02 20:09:13 +0400"
relations:
  evaluation_for:
    - CA-R-1466
    - CA-R-1720
    - CA-R-1463
    - CA-R-1467
    - CA-R-1468
atom_id: "CA-E-464"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-464-CORE_META_MODEL-EVALUATION_APPROACH--validate-journal-independence-from-git.md
---
# Summary

Validate Journal independence from Git

## Scope

Core Meta-Model rules concerning Journal recording, replacement evidence, and canonical log Projections.

## Claim

the Evaluation **must** reject a Core Meta-Model rule that makes Journal recording, replacement evidence, **or** either canonical log Projection depend on Git installation, commit topology, hooks, **or** commit messages.

with no Git Extension selected, admitted Journal records **and** their Artifact Change Log **and** Process Log Projections **must** remain valid under their applicable authority. with the Git Extension selected, its commit references **may** add provenance but **must not** create a second authoritative event history. changing **or** removing secondary Git history **must not** destroy the recorded identity **and** evidence needed **to** rebuild the two logs. a missing **or** invalid authoritative Journal remains a failure **in** either case.

## Details
