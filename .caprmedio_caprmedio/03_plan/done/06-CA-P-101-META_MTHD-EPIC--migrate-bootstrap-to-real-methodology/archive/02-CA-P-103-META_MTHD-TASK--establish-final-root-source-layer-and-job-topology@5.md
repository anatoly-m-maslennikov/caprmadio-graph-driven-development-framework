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
version: 5
updated_at: 2026-08-26 17:14:39 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Establish Final Root, Source-Layer, and Job Topology

**when** CA-P-102 is Done, **then** the Assignee **must** establish the accepted CAPRMEDIO root, Applicable Methodology source-Layer, and parent-owned Job topology as governed authority.

## Scope

`((all active and draft Atoms and Scope Units that govern BSEED Jobs, Structural levels, Scope Unit types, Scope Unit type names, Structural parents, Layer order, Framework ownership, Project ownership, Runtime ownership, Applicable Methodology sources, and Project boundary position) union (the three Job Atom drafts whose Claim Scopes are CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION))`

## Definition of Done

the Task is **not done if** (.caprmedio_framework does not own persistent methodology and Tools governing the current Project **or** .caprmedio_project does not own persistent governed Project Artifacts and evidence **or** .caprmedio_runtime owns any governing authority **or** the Project root Delivery topology differs from (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) **or** the direct Project-child authority topology differs from (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) under .caprmedio_project **or** FRAMEWORK_ENGINE has any direct child other than PROGRAMMATIC or AGENTIC **or** PROGRAMMATIC has any direct child other than TOOLS, APPS, or MCP **or** AGENTIC has any direct child other than SKILLS **or** 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION are not ordered source Layers under 000_APPLICABLE_MTHD_sources **or** APPLICABLE_MTHD_SOURCES does not own at least one Job Atom for each of those three direct children **or** any of CORE_META_MODEL, INSTALLED_EXTENSIONS, LOCAL_CONFIGURATION, or another topology Scope Unit established by this Task lacks at least one valid direct-parent-owned Job **or** any materialized source-Layer Job differs from its accepted draft Claim **or** 00_APPLICABLE_METHODOLOGY is treated as an authoritative fourth Layer **or** METAMODEL, SEMANTICS, GOVERNANCE, METHODOLOGY_META_MODEL, CAPRMEDIO_APPLICATION, or PROJECT_LOCAL_METHODOLOGY remains an intended target Scope Unit **or** any replacement or retirement disposition is missing).

## Details

establish structural and Job authority only. do not move final carriers in this Task. encode Structural Level and Navigational Order Number in every root Delivery name. also encode Unit Type Name and applicable Local Order in every direct Project-child authority name. omit PROJECT from every direct Project-child authority directory name because .caprmedio_project already establishes Project ownership. make PROGRAMMATIC and AGENTIC the only FRAMEWORK_ENGINE composition branches. place TOOLS, APPS, and MCP directly under PROGRAMMATIC and SKILLS directly under AGENTIC. make the three source Layers ordered as Core Meta-Model first, Installed Extensions second, and Local Configuration third. materialize the accepted Job drafts without broadening their Claims. treat generated Applicable Methodology carriers as a non-authoritative Projection compiled from those sources. preserve 000_APPLICABLE_MTHD_sources during every compilation of sibling generated carriers under 00_APPLICABLE_METHODOLOGY.
