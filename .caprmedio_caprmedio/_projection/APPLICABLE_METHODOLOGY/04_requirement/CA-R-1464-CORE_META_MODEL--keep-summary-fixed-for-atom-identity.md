---
subjects:
  governs: "Atom/Summary"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-02 23:17:53 +0400"
relations: {}
atom_id: "CA-R-1464"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1464-CORE_META_MODEL--keep-summary-fixed-for-atom-identity.md
  source_atom_id: CA-R-1464
  source_atom_revision: 5
  source_sha256: 5ad1fc1b5e20641bf1455da8afd99276a0635b494074784e41af23de36e3dc88
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Summary fixed for Atom identity

## Scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.

## Details
