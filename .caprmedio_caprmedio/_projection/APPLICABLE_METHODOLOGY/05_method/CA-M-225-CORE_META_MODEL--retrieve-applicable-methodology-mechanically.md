---
subjects:
  governs: "Applicable Methodology Retrieval"
  depends_on:
    - "Applicable Methodology"
    - "Atom/Subjects"
version: 15
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-225"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-225-CORE_META_MODEL--retrieve-applicable-methodology-mechanically.md
  source_atom_id: CA-M-225
  source_atom_revision: 15
  source_sha256: a5b42abbafdd7458d70e4282e6912f1ac3073ab697caca67d2d262c85d66b4b5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
