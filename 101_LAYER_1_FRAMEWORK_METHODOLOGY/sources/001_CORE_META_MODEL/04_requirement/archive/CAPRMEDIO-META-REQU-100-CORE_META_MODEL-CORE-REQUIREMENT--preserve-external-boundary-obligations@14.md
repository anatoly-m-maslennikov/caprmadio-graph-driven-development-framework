---
atom_id: CAPRMEDIO-META-REQU-100
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "scope-topology"
  depends_on: []
version: 14
updated_at: "2026-09-14 06:21:07 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Preserve external boundary obligations

An operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, **or** comparable external obligation is represented by its semantic contribution **and** external Governance origin.

An obligation imposed by an identified external source occupies the Requirement Content role, has external Governance origin, **and** pins the applicable external source version **or** digest. Its graph connections are typed relations whose Carrier encoding is governed by CA-D-268 **and** do **not** create another Governance origin.

Implementation **must** conform to the exact accepted obligation Revision it consumes **and** cannot rewrite it. A changed external source creates a new accepted Revision **when** the same obligation remains identifiable. a different obligation requires a new Atom **and** explicit predecessor **and** successor Atom IDs in the predecessor’s archival Journal event, **not** a formal replacement relation. Existing Implementations remain bound to their consumed revisions **until** lineage-impact review determines their disposition.

Requirement authority defines this boundary **and** admitted external Type values. Delivery authority governs their Carrier names, identities, **and** catalog representations.

## Primary claim

External boundary obligations use the Requirement Content role, preserve their pinned source revision **and** Governance origin, **and** cannot be rewritten by their Implementations.
