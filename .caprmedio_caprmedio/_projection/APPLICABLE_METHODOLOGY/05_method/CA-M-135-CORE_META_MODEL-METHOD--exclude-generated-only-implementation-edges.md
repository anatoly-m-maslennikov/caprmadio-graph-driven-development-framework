---
subjects:
  governs: "provenance"
  depends_on: []
version: 18
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-135"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-135-CORE_META_MODEL-METHOD--exclude-generated-only-implementation-edges.md
  source_atom_id: CA-M-135
  source_atom_revision: 18
  source_sha256: 21d7a124cdb31b41665fefbda11604ede8cadeb635c0c3873511bab303969420
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Exclude generated-only implementation edges

## Scope

provenance validation of recorded changes in the governed selection.

## Claim

provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.

## Details
