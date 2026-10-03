---
atom_id: CA-P-928
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Project Configuration/Revision Binding
    occurrent:
      - Project Configuration Revision Binding Authority Repair
  depends_on:
    occurrent:
      - CA-P-926
version: 2
updated_at: 2026-08-30 19:32:24 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Repair Project Configuration Revision Binding Authority

**when** CA-P-926 is Done, **then** the Assignee **must** replace retired `.caprmedio` Project Configuration revision-binding authority with authority for the current Local Configuration Carrier and `.caprmedio_caprmedio` Work Journal evidence.

## Scope

`((CA-R-1055) union (CA-D-328) union (the current Local Configuration Project Configuration Carrier) union (the exact archives and evidence required by their revisions))`

## Definition of Done

the Task is **not done if** (current authority still requires a Project Configuration binding under retired `.caprmedio` **or** the canonical Project Configuration Carrier, identity, revision, digest, **or** Work Journal evidence location is absent **or** ambiguous **or** CA-R-1055 conflicts with CA-D-328 **or** a changed Atom lacks its exact predecessor archive **or** the repair changes unrelated Local Configuration authority).

## Details

preserve `CAPRMEDIO-I-001` as the native Project Configuration Atom identity. bind currentness to the canonical Local Configuration Carrier and append-only evidence under `.caprmedio_caprmedio/work_journal/`.

## Completion Evidence

the Task preserved `CAPRMEDIO-I-001` at revision `3`, bound its canonical Local Configuration Carrier and SHA-256 Digest in one append-only Work Journal event, and replaced the retired `.caprmedio/` locator in CA-R-1055. CA-D-328 already places the event under `.caprmedio_caprmedio/work_journal/`.

the non-authoritative execution evidence is stored in `execution_evidence/CA-P-928-project-configuration-revision-binding-repair.projection.json`.
