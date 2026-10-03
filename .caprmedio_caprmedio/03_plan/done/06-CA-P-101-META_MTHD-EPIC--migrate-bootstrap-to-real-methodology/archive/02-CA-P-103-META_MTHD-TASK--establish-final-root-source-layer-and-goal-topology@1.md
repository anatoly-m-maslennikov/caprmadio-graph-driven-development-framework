---
atom_id: CA-P-103
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - CAPRMEDIO Root and Methodology Source Topology
    occurrent:
      - Bootstrap Migration
  depends_on:
    occurrent:
      - CA-P-102
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Establish Final Root, Source-Layer, and Goal Topology

**when** CA-P-102 is Done, **then** the Assignee **must** establish the accepted CAPRMEDIO root, Applicable Methodology source-Layer, and Goal topology as governed authority.

## Scope

`(all active and draft Atoms and Scope Units that govern BSEED Goals, Structural levels, Scope Unit types, Scope Unit type names, Structural parents, Layer order, Framework ownership, Project ownership, Runtime ownership, Applicable Methodology sources, and Project boundary position)`

## Definition of Done

the Task is **not done if** (.caprmedio_framework does not own persistent methodology and Tools governing the current Project **or** .caprmedio_project does not own persistent governed Project Artifacts and evidence **or** .caprmedio_runtime owns any governing authority **or** 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION are not ordered source Layers under 000_APPLICABLE_MTHD_sources **or** 00_APPLICABLE_METHODOLOGY is treated as an authoritative fourth Layer **or** METAMODEL, SEMANTICS, GOVERNANCE, METHODOLOGY_META_MODEL, CAPRMEDIO_APPLICATION, or PROJECT_LOCAL_METHODOLOGY remains an intended target Scope Unit **or** the target Goals do not match the final topology **or** any replacement or retirement disposition is missing).

## Details

establish structural authority only. do not move carriers in this Task. make the three source Layers ordered as Core Meta-Model first, Installed Extensions second, and Local Configuration third. treat generated Applicable Methodology carriers as a non-authoritative Projection compiled from those sources. preserve 000_APPLICABLE_MTHD_sources during every compilation of sibling generated carriers under 00_APPLICABLE_METHODOLOGY.
