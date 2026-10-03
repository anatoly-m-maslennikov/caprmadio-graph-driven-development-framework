---
atom_id: CA-P-111
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - CAPRMEDIO Framework and Project State
    occurrent:
      - Methodology Cutover
  depends_on:
    occurrent:
      - CA-P-114
version: 5
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Validate the Final Methodology Cutover

**when** CA-P-114 is Done, **then** the Assignee **must** validate the complete final Framework, Project, Runtime, Job, consumer, and Applicable Methodology frontier.

## Scope

`((all current Core Meta-Model, Installed Extensions, Local Configuration, final Scope Unit Job, Applicable Methodology, Framework Tool, Project Artifact, Journal, and Runtime Carriers) union (all representative subject- and process-scoped Projections) union (all final authority and Delivery directories) union (all pre-migration roots, Bootstrap Scope Units, and migration evidence) union (CA-P-101) union (the complete execution frontier of every direct Task of CA-P-101))`

## Definition of Done

the Task is **not done if** (any active or draft authority remains owned by obsolete METAMODEL, SEMANTICS, GOVERNANCE, METHODOLOGY_META_MODEL, CAPRMEDIO_APPLICATION, or PROJECT_LOCAL_METHODOLOGY Scope Units **or** the Project root Delivery topology differs from (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) **or** the direct Project-child authority topology differs from (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) under .caprmedio_project **or** any final FRAMEWORK_ENGINE authority or Delivery directory differs from the exact fully labelled CA-P-108 target **or** any obsolete root Delivery name, redundant PROJECT authority token, bare Engine-descendant target, or mapped obsolete directory remains **or** any governing Framework Carrier is outside .caprmedio_framework **or** any governed Project Carrier is outside .caprmedio_project without its exact registered native Carrier Type exception **or** any retained root-native Project Carrier lacks its mapped exception **or** .caprmedio or .caprmedio_install remains **or** .caprmedio_runtime contains governing authority **or** any final Scope Unit lacks an accepted Job with the correct Operator or direct-parent owner **or** CORE_META_MODEL contains authority unnecessary to its Job or is insufficient for it **or** INSTALLED_EXTENSIONS activates or locally mutates an Extension **or** LOCAL_CONFIGURATION fails to determine the Project-owned composition used by compilation **or** the three source Layers are not independently inspectable **or** Applicable Methodology is not deterministic, current, and regenerable **or** Extension and Project Customization provenance is incomplete **or** any validator or consumer resolves obsolete coordinates **or** retirement evidence does not prove every removed directory was empty **or** rollback and migration evidence are incomplete **or** the Epic is marked Done before every direct Task has a recorded passing Scope Resolution).

## Details

perform validation only. preserve archived Carriers, Framework and Project Journals, migration maps, source manifests, retirement evidence, and validation evidence. validate that the Project root, .caprmedio_framework, .caprmedio_project, and .caprmedio_runtime each expose only their accepted ownership topology. move this Epic to Done only after the final target frontier is self-consistent and reproducible and every direct Task has a passing Scope Resolution.
