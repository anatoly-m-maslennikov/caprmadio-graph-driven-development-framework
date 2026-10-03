---
atom_id: CA-P-931
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Project Scope Unit Graph Generator
    occurrent:
      - Project Scope Unit Graph Generator Migration
  depends_on:
    occurrent:
      - CA-P-930
version: 1
updated_at: 2026-08-30 19:25:06 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Migrate Project Scope Unit Graph Generator

**when** CA-P-930 is Done, **then** the Assignee **must** make the canonical Project Scope Unit Graph generator derive Scope Unit nodes and parent edges from the current typed relational folder hierarchy.

## Scope

`((GENERATE_PROJECT_GRAPH_STATE Tool source and tests) union (current Scope Unit and Epic Directory Carrier naming authority) union (the canonical Local Configuration Project Configuration Carrier) union (.caprmedio_caprmedio typed relational folders))`

## Definition of Done

the Task is **not done if** (the generator requires retired `.caprmedio`, retired `002_FRAMEWORK_ENGINE`, **or** root Project Configuration paths **or** treats a Job as a Scope Unit registry **or** treats an Epic Directory as a Scope Unit **or** omits a canonical typed Scope Unit Directory **or** derives parentage from anything other than the nearest typed Scope Unit ancestor **or** emits uppercase `CAPRMEDIO` as the Project identity **or** an identical source frontier produces different output **or** tests fail).

## Details

identify Scope Unit folders through current Directory Carrier grammar. use folder Type to distinguish Scope Units from Epics. use Jobs only as work Claims that may govern Scope Units **or** Epics.
