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
version: 7
updated_at: 2026-08-26 19:50:33 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Establish Final Root, Source-Layer, and Engine Topology

**when** CA-P-102 is Done, **then** the Assignee **must** establish the accepted CAPRMEDIO ownership-root, Applicable Methodology source-Layer, Project Delivery, Project authority, and FRAMEWORK_ENGINE Scope Unit topology as governed target authority.

## Scope

`((all active and draft Atoms in the frozen CA-P-102 source frontier that govern Structural levels, Navigational Order Numbers, Scope Unit types, Scope Unit type names, Local Orders, Structural parents, Framework ownership, Project ownership, Runtime ownership, Applicable Methodology sources, Project boundary position, or Scope Unit authority-to-Delivery mappings) union (CAPRMEDIO, FRAMEWORK_METHODOLOGY, FRAMEWORK_ENGINE, OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, RELEASES, COMMUNITY_EXTENSIONS, FIELD, PROGRAMMATIC, AGENTIC, TOOLS, APPS, MCP, SKILLS, APPLICABLE_MTHD_SOURCES, CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION))`

## Definition of Done

the Task is **not done if** (the governed target does not assign persistent methodology and Tools governing the current Project to `.caprmedio_framework/` **or** the governed target does not assign persistent governed Project Artifacts and evidence to `.caprmedio_project/` **or** the governed target assigns governing authority to `.caprmedio_runtime/` **or** the Project root Delivery topology differs from (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) **or** the direct Project-child authority topology differs from (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) under `.caprmedio_project/` **or** FRAMEWORK_ENGINE has any direct child other than PROGRAMMATIC or AGENTIC **or** PROGRAMMATIC has any direct child other than TOOLS, APPS, or MCP **or** AGENTIC has any direct child other than SKILLS **or** the authority paths differ from (201_FEATURE_PROGRAMMATIC, 202_FEATURE_AGENTIC, 301_FEATURE_TOOLS, 302_FEATURE_APPS, 303_FEATURE_MCP, 301_FEATURE_SKILLS) at their accepted parents **or** the Delivery paths differ from (201_PROGRAMMATIC, 202_AGENTIC, 301_TOOLS, 302_APPS, 303_MCP, 301_SKILLS) at their accepted parents **or** any enumerated Project or FRAMEWORK_ENGINE Scope Unit authority folder lacks exactly one explicit governed mapping to its Delivery folder or subfolder **or** 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION are not ordered source Layers under 000_APPLICABLE_MTHD_sources **or** 00_APPLICABLE_METHODOLOGY is treated as an authoritative fourth Layer **or** METAMODEL, SEMANTICS, GOVERNANCE, METHODOLOGY_META_MODEL, CAPRMEDIO_APPLICATION, or PROJECT_LOCAL_METHODOLOGY remains an intended target Scope Unit **or** an obsolete named Scope Unit lacks CA-P-108 as its exact disposition owner).

## Details

establish structural and carrier-mapping authority only. do not materialize Jobs or move final carriers in this Task. derive every final directory basename from exact governed Operator labels or governed defaults. encode Structural Level and Navigational Order Number in every Delivery name. also encode Unit Type Name and applicable Local Order in every authority name. omit PROJECT from every direct Project-child authority directory name because `.caprmedio_project` already establishes Project ownership. make PROGRAMMATIC and AGENTIC the only FRAMEWORK_ENGINE composition branches. place TOOLS, APPS, and MCP directly under PROGRAMMATIC and SKILLS directly under AGENTIC. make the three source Layers ordered as Core Meta-Model first, Installed Extensions second, and Local Configuration third. each Scope Unit Delivery Atom explicitly maps one authority folder to one governed Delivery folder or subfolder; that Delivery location may be at repository root, inside `.caprmedio_project/`, or another governed location. do not create a generic root or root-native Carrier exception. treat generated Applicable Methodology carriers as a non-authoritative Projection compiled from the three sources. preserve `000_APPLICABLE_MTHD_sources` during every compilation of sibling generated carriers under `00_APPLICABLE_METHODOLOGY`.

## Task Scope Resolution

the Task Scope Resolution uses the completed CA-P-102 frozen frontier and its four execution-evidence manifests. the resolved authority set consists of the ownership-root and Applicable Methodology source-placement drafts, the three APPLICABLE_MTHD_SOURCES child-scope-definition drafts, CA-R-862, the seven direct Project-child Delivery Atoms, the six FRAMEWORK_ENGINE descendant Delivery Atoms, and the existing FRAMEWORK_ENGINE, PROGRAMMATIC, and AGENTIC direct-child topology Atoms. [CA-P-103 target-topology projection](execution_evidence/CA-P-103-target-topology.projection.json) records the exact resolved target with SHA-256 `619e738596170ab815269251597ebe0d0f2f395fb0d86c830391c33560513a5b`.

## Execution Result

PASS. the governed target assigns `.caprmedio_framework/` to persistent methodology and Tools governing the current Project, `.caprmedio_project/` to persistent governed Project Artifacts and evidence, and `.caprmedio_runtime/` only to ephemeral execution state. each direct Project-child authority folder has one exact Delivery mapping. FRAMEWORK_ENGINE has the exact confirmed PROGRAMMATIC and AGENTIC branches; their descendants use the exact confirmed authority and Delivery labels. Applicable Methodology has exactly the three ordered sources under its protected source folder and is non-authoritative. the obsolete named Scope Units remain source-frontier items only, with CA-P-108 as their exact disposition owner. no final carrier was moved and no Job was materialized.
