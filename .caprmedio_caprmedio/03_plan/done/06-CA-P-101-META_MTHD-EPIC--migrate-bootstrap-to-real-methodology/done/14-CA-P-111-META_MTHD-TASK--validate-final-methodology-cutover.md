---
atom_id: CA-P-111
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - METHODOLOGY_SOURCES
      - APPLICABLE_METHODOLOGY
      - CAPRMEDIO Framework and Project State
    occurrent:
      - Methodology Cutover
  depends_on:
    occurrent:
      - CA-P-113
      - CA-P-114
version: 7
updated_at: 2026-09-03 15:15:52 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Validate the Final Methodology Cutover

**when** CA-P-113 **and** CA-P-114 are Done, **then** the Assignee **must** validate the final METHODOLOGY_SOURCES, APPLICABLE_METHODOLOGY, Framework, Project, installation, Runtime, and consumer frontier.

## Scope

`((METHODOLOGY_SOURCES and its direct Scope Units CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION) union (APPLICABLE_METHODOLOGY) union (all final Framework, Project, installation, Runtime, Tool, Goal, Journal, and Delivery Carriers) union (the retired Bootstrap roots and CA-P-101 evidence) union (CA-P-101 and every direct Task))`

## Definition of Done

the Task is **not done if** (CA-P-113 or CA-P-114 is not Done with passing evidence **or** any current Framework authority Carrier is outside `.caprmedio_framework` **or** any current Project governed Carrier is outside `.caprmedio_caprmedio` without an accepted native Carrier exception **or** `.caprmedio_install` is absent, moved, or used as Framework authority **or** `.caprmedio_runtime` contains governing authority **or** the root Delivery topology differs from (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) **or** the current Project-child topology differs from (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) **or** METHODOLOGY_SOURCES lacks one independently inspectable CORE_META_MODEL, INSTALLED_EXTENSIONS, or LOCAL_CONFIGURATION Scope Unit **or** APPLICABLE_METHODOLOGY does not deterministically select the active source frontier, reports an unresolved Conflict, has independent authority, or cannot regenerate **or** a consumer or validator resolves `.caprmedio` or `.caprmedio_project` as a current coordinate **or** a retired root contains a governed Carrier **or** the CA-P-114 byte-exact mapping, rollback, or host-only empty-directory-residue evidence is incomplete **or** `.DS_Store` affects a result **or** any direct CA-P-101 Task lacks Done placement and passing evidence **or** CA-P-101 moves to Done before this Task passes).

## Details

perform validation only. preserve archived Carriers, Framework and Project Journals, migration maps, source manifests, retirement evidence, and validation evidence. treat `.DS_Store` as non-governed Finder metadata. treat the CA-P-114 recorded macOS-blocked empty directory shells as non-governed host residue. validate that `.caprmedio_framework`, `.caprmedio_caprmedio`, `.caprmedio_install`, and `.caprmedio_runtime` expose their accepted ownership topology. move this Task and then CA-P-101 to Done only after the final target frontier is self-consistent and reproducible and every direct Task has passing evidence.
