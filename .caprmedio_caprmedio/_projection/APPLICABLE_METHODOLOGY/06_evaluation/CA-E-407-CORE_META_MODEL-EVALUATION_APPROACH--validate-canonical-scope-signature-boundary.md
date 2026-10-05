---
subjects:
  governs: "Canonical Scope Signature Derivation Validation"
  depends_on:
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
    - "Atom/Carrier"
version: 10
updated_at: "2026-10-02 20:03:51 +0400"
relations:
  evaluation_for:
    - CA-R-1361
    - CA-M-241
atom_id: "CA-E-407"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-407-CORE_META_MODEL-EVALUATION_APPROACH--validate-canonical-scope-signature-boundary.md
  source_atom_id: CA-E-407
  source_atom_revision: 10
  source_sha256: ef78590cf46f4f2679aa38bd0dd034bf97e6816adfb0c6e1030b5a0ff82ce65b
  original_relations_sha256: 9f42961de2ab19ebbf0721ed15ec0f854c9df12d1ec58d3936ae5b5e57ad4922
---
# Summary

Validate Canonical Scope Signature Boundary

## Scope

Canonical Scope Signature derivations.

## Claim

the Evaluation **must** reject a Canonical Scope Signature derivation **if** **any** of the following holds:

- it rewrites one source Carrier.
- it treats one Signature as authority **or** Claim equivalence.
- it accepts mixed **and** **or** groups, **without**, **where**, **all**, **any** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose.
- it fails **to** flatten nested same-operator groups, retains duplicate exact Atom IDs, loses the distinction between **and** **and** **or**, **or** yields different Signatures from same-operator groups that differ **only** by operand order.

## Details
