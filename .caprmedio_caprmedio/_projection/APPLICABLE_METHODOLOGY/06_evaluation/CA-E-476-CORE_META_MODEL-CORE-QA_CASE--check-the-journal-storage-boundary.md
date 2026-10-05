---
subjects:
  governs: "Journal"
  depends_on:
    - "Journal/Record"
    - "Artifact/Carrier"
    - "Atom"
    - "Project"
    - "Applicable Methodology"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-D-308
    - CA-D-340
atom_id: "CA-E-476"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-476-CORE_META_MODEL-CORE-QA_CASE--check-the-journal-storage-boundary.md
  source_atom_id: CA-E-476
  source_atom_revision: 5
  source_sha256: 6ab9828f130133780eb89ea7dac13b3e3cc60134a92ab8a120d31da9a23ea2ae
  original_relations_sha256: 0bb9bdd707ca608a1c818dea2bc9d515b9d834249c593269b81348c8b6275d01
---
# Summary

Check the Journal storage boundary

## Scope

Journal admission checks event **and** storage integrity **without** becoming a Project-conformance gate.

## Claim

report a failed Evaluation **if** the Journal loses recordable evidence because of Project defects, accepts corrupted **or** unauthorized writes, silently changes observations, **or** rewrites accepted history.

## Details

### Cases

1. submit a correctly encoded event describing a conforming Project change.
2. keep that event envelope valid while recording a legacy Atom ID, broken filename, invalid placement, malformed Atom Properties, unresolved Relation, **or** invalid lifecycle transition.
3. change the live Project **after** capture while leaving the sealed historical observation intact.
4. submit unreadable event data, missing required Event identity **or** fields, a digest mismatch, unauthorized append access, **or** an attempt **to** rewrite accepted history.
5. resubmit the same Event identity **and** payload; **then** supply a conflicting payload under that identity.
6. record an action whose separate conformance Evaluation failed **or** remained unresolved.

### Acceptance

- cases 1, 2, 3, **and** 6 remain recordable **without** inventing identities, repairing observed values, **or** claiming a successful conformance verdict.
- case 4 fails storage admission, preserves pending evidence safely, **and** leaves accepted history unchanged.
- an identical retry creates no duplicate record. an identity collision with different payload fails **without** overwriting history.
- conformance Evaluations remain independently available; their verdicts do **not** become prerequisites for recording the facts they evaluate.
- Journal acceptance grants no Project-mutation permission **and** does **not** bypass a separate action's preconditions.
