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
version: 1
updated_at: 2026-08-30 19:25:06 +0400
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
