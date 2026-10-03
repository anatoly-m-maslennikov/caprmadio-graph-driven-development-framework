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
version: 3
updated_at: 2026-08-26 16:23:41 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Freeze the Bootstrap and Final Framework Frontier

the Assignee **must** freeze the exact Bootstrap source frontier and record the accepted final CAPRMEDIO Framework, Project, Runtime, and Applicable Methodology architecture without changing governed authority or carriers.

## Scope

`((all active and draft Atoms where Current Scope in (META_METHODOLOGY, METAMODEL, SEMANTICS, GOVERNANCE)) union (the Project-owned META_METHODOLOGY Job) union (all active Plans that govern BSEED reconciliation or migration except CA-P-101 and CA-P-102 through CA-P-111) union (all current authority, configuration, Journals, Projections, installed components, and runtime classifications under .caprmedio, .caprmedio_install, and .caprmedio_runtime) union (all current root-level numbered Scope Unit directories, Framework and Tool Carriers, root configuration Carriers, and consumers that govern, configure, validate, install, or run CAPRMEDIO))`

## Definition of Done

the Task is **not done if** (the exact source Carrier manifest and digest are absent **or** any current root-level Framework, Tool, Scope Unit, configuration, or consumer Carrier in the migration frontier is omitted **or** CA-P-101, any of CA-P-102 through CA-P-111, or their execution evidence is included in the frozen source manifest **or** the target does not record .caprmedio_framework, .caprmedio_project, and .caprmedio_runtime separately **or** the target does not record 001_CORE_META_MODEL, 002_INSTALLED_EXTENSIONS, and 003_LOCAL_CONFIGURATION as the three ordered Applicable Methodology source Layers **or** the target does not record 00_APPLICABLE_METHODOLOGY and its protected 000_APPLICABLE_MTHD_sources subfolder **or** any active Bootstrap Plan lacks an explicit unresolved or accepted disposition **or** any accepted decision is omitted **or** any unresolved decision is silently treated as accepted **or** any governed source Carrier changes).

## Details

record .caprmedio_framework as the persistent methodology and Tool environment governing the current Project, .caprmedio_project as the persistent governed Artifact and evidence root of the current Project, and .caprmedio_runtime as ephemeral execution state. record Applicable Methodology as a mechanical non-authoritative compilation without LLM inference. treat CA-P-101, its direct Task children, and their execution evidence as migration-control Artifacts outside the frozen source manifest. preserve every other unresolved choice explicitly, including active Plan dispositions, default Types, temporal classification, exact Journal subpaths, and final generated-carrier paths.
