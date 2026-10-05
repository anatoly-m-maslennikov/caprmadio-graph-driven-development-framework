---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 22
updated_at: "2026-10-03 02:10:09 +0400"
relations: {}
atom_id: "CA-R-1690"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1690-CORE_META_MODEL-CORE-REQUIREMENT--preserve-external-boundary-obligations.md
  source_atom_id: CA-R-1690
  source_atom_revision: 22
  source_sha256: 7b1d3537ff15a8f51c6dc295111659d586879f0677c67abb807c4d0564a40011
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve external boundary obligations

## Scope

identified external obligations.

## Claim

an Operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, **or** comparable external obligation is represented by its primary semantic contribution **and** external Governance Origin.

- Content Role follows the Claim's primary contribution under CA-R-1531, independently of Governance Origin under CA-R-1701. an external origin does **not** by itself assign Requirement **or** **any** other Content Role.
- an obligation imposed by an identified external source retains external Governance Origin **and** pins the applicable source version **or** digest. its graph connections use typed Relations whose Carrier encoding is governed by CA-D-268; these Relations do **not** create another Governance Origin.
- Implementation **must** conform **to** the exact accepted obligation Revision it consumes **and** **must not** rewrite that obligation. a changed external source creates a new accepted Revision **when** the same obligation remains identifiable. a different obligation requires a new Atom **and** explicit predecessor **and** successor Atom IDs **in** the predecessor's archival Journal event, **not** a formal replacement Relation.
- existing Implementations remain bound **to** their consumed Revisions **until** lineage-impact review determines their disposition.

Requirement authority defines the external boundary **and** admitted Type values. Delivery authority governs Carrier names, identities, **and** Catalog representations. this separation does **not** reclassify those Carrier specifications as Requirements because their source is external.

## Details
