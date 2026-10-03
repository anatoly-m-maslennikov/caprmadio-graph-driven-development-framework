---
atom_id: CA-P-926
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - caprmedio Project Projection Frontier
    occurrent:
      - caprmedio Project Projection Rebuild
  depends_on:
    occurrent:
      - CA-P-925
version: 3
updated_at: 2026-08-30 17:44:53 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Rebuild caprmedio Project Projections

**when** CA-P-925 is Done, **then** the Assignee **must** rebuild **every** registered persistent non-authoritative caprmedio Project Projection whose source frontier changed during this Epic.

## Scope

`(all registered persistent non-authoritative Projections whose declared source frontier includes a Carrier changed by CA-P-918 through CA-P-925)`

## Definition of Done

the Task is **not done if** (an affected registered persistent Projection remains stale **or** a rebuilt Projection omits its generation procedure, exact source frontier, source digest, updated-at value, **or** deterministic output digest **or** a Projection adds authority **or** independent source identity **or** an on-demand Entity Graph **or** Subject Index is persisted contrary **to** current authority **or** a generated Applicable Methodology Carrier is rebuilt outside CA-P-924 **or** deleting **any** rebuilt Projection prevents regeneration from its declared sources).

## Details

rebuild **only** registered persistent Projections. derive Entity Graphs **and** Subject indexes on demand **and** do **not** persist them. keep Journals as evidence Carriers rather than rewriting them as Projections.

## Completion Evidence

the Task found two registered persistent caprmedio Project Projections. the 60 declared source Carriers have no intersection with the 1,560 Carriers changed by CA-P-918 through CA-P-925. the Task rebuilt zero Projections.

the non-authoritative execution evidence is stored in `execution_evidence/CA-P-926-project-projection-rebuild.projection.json`.
