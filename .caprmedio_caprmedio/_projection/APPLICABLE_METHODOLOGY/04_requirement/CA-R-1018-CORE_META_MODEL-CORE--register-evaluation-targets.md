---
subjects:
  governs: "Evaluation For Relation"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Operations"
    - "Atom/Local Tier"
version: 17
updated_at: "2026-10-02 21:16:45 +0400"
relations: {}
atom_id: "CA-R-1018"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1018-CORE_META_MODEL-CORE--register-evaluation-targets.md
  source_atom_id: CA-R-1018
  source_atom_revision: 17
  source_sha256: 82d35b5486d370f1db60aea0b8eb8a417685f08a210ddd9db4ad2916634f4756
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register Evaluation targets

## Scope

direct `evaluation_for` relations.

## Claim

`evaluation_for` **means** a direct relation owned by an Evaluation Atom **and** directed **to** an Atom whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations) **and** whose authority the Evaluation checks;

- a Standard Evaluation Atom **must** own **`>=1`** such target relations,
- while a Core **or** General Evaluation **may** state a representation-independent evaluation policy **without** an artificial list of individual targets.

**every** supplied target relation **must** retain the same checked-authority qualification regardless of the Evaluation's Local Tier.

## Details
