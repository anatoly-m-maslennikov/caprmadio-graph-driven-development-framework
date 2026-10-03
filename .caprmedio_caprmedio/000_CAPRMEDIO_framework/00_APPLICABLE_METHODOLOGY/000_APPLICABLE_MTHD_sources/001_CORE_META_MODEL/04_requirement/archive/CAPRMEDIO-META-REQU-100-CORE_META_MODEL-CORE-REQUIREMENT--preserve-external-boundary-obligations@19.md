---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 19
updated_at: "2026-09-20 23:49:39 +0000"
relations: {}
---
# Preserve external boundary obligations

an Operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, **or** comparable external obligation is represented by its primary semantic contribution **and** external Governance Origin.

- Content Role follows the Claim's primary contribution under CA-R-1531, independently of Governance Origin under CAPRMEDIO-META-REQU-113. an external origin does **not** by itself assign Requirement **or** **any** other Content Role.
- an obligation imposed by an identified external source retains external Governance Origin **and** pins the applicable source version **or** digest. its graph connections use typed Relations whose Carrier encoding is governed by CA-D-268; these Relations do **not** create another Governance Origin.
- Implementation **must** conform **to** the exact accepted obligation Revision it consumes **and** **must not** rewrite that obligation. a changed external source creates a new accepted Revision **when** the same obligation remains identifiable. a different obligation requires a new Atom **and** explicit predecessor **and** successor Atom IDs **in** the predecessor's archival Journal event, **not** a formal replacement Relation.
- existing Implementations remain bound **to** their consumed Revisions **until** lineage-impact review determines their disposition.

Requirement authority defines the external boundary **and** admitted Type values. Delivery authority governs Carrier names, identities, **and** Catalog representations. this separation does **not** reclassify those Carrier specifications as Requirements because their source is external.
