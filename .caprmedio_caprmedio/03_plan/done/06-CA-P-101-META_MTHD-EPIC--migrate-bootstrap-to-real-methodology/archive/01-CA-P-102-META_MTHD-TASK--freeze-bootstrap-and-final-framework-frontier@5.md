---
atom_id: CA-P-102
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Methodology Migration Frontier
    occurrent:
      - Bootstrap Migration
  depends_on:
    continuant:
      - Bootstrap Authority
version: 5
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Freeze the Bootstrap and Final Framework Frontier

the Assignee **must** freeze the exact Bootstrap source frontier and record the accepted final CAPRMEDIO Framework, Project, Runtime, and Applicable Methodology architecture without changing governed authority or carriers.

## Scope

`(((all active and draft Atoms where Current Scope in (META_METHODOLOGY, METAMODEL, SEMANTICS, GOVERNANCE)) union (the Project-owned META_METHODOLOGY Job) union (all active Plans that govern BSEED reconciliation or migration) union (all current directories and Carriers under .caprmedio, .caprmedio_install, and .caprmedio_runtime) union (all current root-level numbered Scope Unit directories and their descendants) union (all Framework and Tool Carriers, root configuration Carriers, and consumers that govern, configure, validate, install, or run CAPRMEDIO)) difference (CA-P-101, every direct Task of CA-P-101, and all execution evidence produced by CA-P-101))`

## Definition of Done

the Task is **not done if** (the exact source Carrier manifest and digest are absent **or** the exact structural directory manifest is absent **or** the separate migration-control Carrier manifest is absent **or** any current directory or Carrier in the migration frontier is omitted **or** an empty duplicate directory or .caprmedio_install staging directory is omitted **or** CA-P-101, any direct Task of CA-P-101, or their execution evidence is included in the governed source manifests **or** CA-P-101 or any current direct Task Carrier is omitted from the migration-control manifest **or** the target does not record .caprmedio_framework, .caprmedio_project, and .caprmedio_runtime separately **or** the target does not record 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION as the three ordered Applicable Methodology source Layers **or** the target does not record 00_APPLICABLE_METHODOLOGY and its protected 000_APPLICABLE_MTHD_sources subfolder **or** any active Bootstrap Plan lacks an explicit unresolved or accepted disposition **or** any accepted decision is omitted **or** any unresolved decision is silently treated as accepted **or** any governed source Carrier or directory state changes).

## Details

record every directory by exact project-relative path, direct parent, entry count, and empty or non-empty state. record every Carrier by exact project-relative path and content digest. record .caprmedio_framework as the persistent methodology and Tool environment governing the current Project, .caprmedio_project as the persistent governed Artifact and evidence root of the current Project, and .caprmedio_runtime as ephemeral execution state. record Applicable Methodology as a mechanical non-authoritative compilation without LLM inference. record CA-P-101, its direct Task children, and their execution evidence in a separate migration-control manifest so they remain outside the governed source digest but still receive exact final Carrier dispositions before .caprmedio retirement. preserve every other unresolved choice explicitly, including active Plan dispositions, default Types, temporal classification, exact Journal subpaths, and final generated-carrier paths.
