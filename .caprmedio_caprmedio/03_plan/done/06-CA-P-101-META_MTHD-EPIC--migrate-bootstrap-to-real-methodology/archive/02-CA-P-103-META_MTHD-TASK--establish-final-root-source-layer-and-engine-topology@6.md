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
version: 6
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Establish Final Root, Source-Layer, and Engine Topology

**when** CA-P-102 is Done, **then** the Assignee **must** establish the accepted CAPRMEDIO ownership-root, Applicable Methodology source-Layer, Project Delivery, Project authority, and FRAMEWORK_ENGINE Scope Unit topology as governed authority.

## Scope

`((all active and draft Atoms in the frozen CA-P-102 source frontier that govern Structural levels, Navigational Order Numbers, Scope Unit types, Scope Unit type names, Local Orders, Structural parents, Framework ownership, Project ownership, Runtime ownership, native Carrier Type exceptions, Applicable Methodology sources, and Project boundary position) union (CAPRMEDIO, FRAMEWORK_METHODOLOGY, FRAMEWORK_ENGINE, OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, RELEASES, COMMUNITY_EXTENSIONS, FIELD, PROGRAMMATIC, AGENTIC, TOOLS, APPS, MCP, SKILLS, APPLICABLE_MTHD_SOURCES, CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION))`

## Definition of Done

the Task is **not done if** (.caprmedio_framework does not own persistent methodology and Tools governing the current Project **or** .caprmedio_project does not own persistent governed Project Artifacts and evidence **or** .caprmedio_runtime owns any governing authority **or** the Project root Delivery topology differs from (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) **or** the direct Project-child authority topology differs from (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) under .caprmedio_project **or** FRAMEWORK_ENGINE has any direct child other than PROGRAMMATIC or AGENTIC **or** PROGRAMMATIC has any direct child other than TOOLS, APPS, or MCP **or** AGENTIC has any direct child other than SKILLS **or** any FRAMEWORK_ENGINE descendant lacks one exact effective Structural Level, Navigational Order Number, Unit Type Name, applicable Local Order, or Unit Name **or** any final FRAMEWORK_ENGINE authority or Delivery directory basename cannot be derived exactly from those effective values **or** any target directory uses a bare Unit Name where the applicable naming authority requires navigational labels **or** 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION are not ordered source Layers under 000_APPLICABLE_MTHD_sources **or** 00_APPLICABLE_METHODOLOGY is treated as an authoritative fourth Layer **or** a root Delivery or another intentionally root-native Project Carrier class lacks one registered native Carrier Type exception to .caprmedio_project placement **or** METAMODEL, SEMANTICS, GOVERNANCE, METHODOLOGY_META_MODEL, CAPRMEDIO_APPLICATION, or PROJECT_LOCAL_METHODOLOGY remains an intended target Scope Unit **or** any replacement or retirement disposition is missing).

## Details

establish structural and carrier-class authority only. do not materialize Jobs or move final carriers in this Task. derive every final directory basename from exact governed Operator labels or governed defaults; do not treat PROGRAMMATIC, AGENTIC, TOOLS, APPS, MCP, or SKILLS as a bare physical basename when labels are required. encode Structural Level and Navigational Order Number in every Delivery name. also encode Unit Type Name and applicable Local Order in every authority name. omit PROJECT from every direct Project-child authority directory name because .caprmedio_project already establishes Project ownership. make PROGRAMMATIC and AGENTIC the only FRAMEWORK_ENGINE composition branches. place TOOLS, APPS, and MCP directly under PROGRAMMATIC and SKILLS directly under AGENTIC. make the three source Layers ordered as Core Meta-Model first, Installed Extensions second, and Local Configuration third. register root Deliveries and every other accepted root-native Project Carrier class as explicit native Carrier Type exceptions rather than weakening the .caprmedio_project default. treat generated Applicable Methodology carriers as a non-authoritative Projection compiled from the three sources. preserve 000_APPLICABLE_MTHD_sources during every compilation of sibling generated carriers under 00_APPLICABLE_METHODOLOGY.
