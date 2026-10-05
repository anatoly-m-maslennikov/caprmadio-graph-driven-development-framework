---
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Project Settings"
    - "Default Settings"
    - "Project Structure"
    - "Authority Mode"
version: 27
updated_at: "2026-09-30 19:58:50 +0000"
relations:
  evaluation_for:
    - "CA-D-361"
    - "CA-D-366"
    - "CA-D-383"
    - "CA-D-387"
    - "CA-D-407"
    - "CA-D-408"
    - "CA-D-442"
    - "CA-M-279"
    - "CA-R-1052"
    - "CA-R-1430"
    - "CA-R-1441"
    - "CA-R-1483"
    - "CA-R-1628"
    - "CA-R-1630"
    - "CA-R-1655"
    - "CA-R-1740"
atom_id: "CAPRMEDIO-GOV-EVAL-006"
content_role: "Evaluation"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/06_evaluation/CAPRMEDIO-GOV-EVAL-006-PROJECT_CONFIGURATION-QA_CASE--canonical-settings-selection.md
  source_atom_id: CAPRMEDIO-GOV-EVAL-006
  source_atom_revision: 27
  source_sha256: 35f125e547f1c9eda79d1981853e729a4f4d8dc884ae153c4ffdd4ec6d06ccd8
  original_relations_sha256: eefe9d7a92dc5d944ca9585e23951f32ebb872628ed357be9a09440d1ad7c31a
---
# Summary
Canonical Settings Selection

## Scope
Framework Instance Settings, Project Settings, **and** Project Structure selections.

## Claim
### Claim checked

the Framework Instance Settings Artifact **and** Project Settings Artifact accept exactly their registered values, resolve deterministically, **and** fail closed on invalid **or** unknown selections; Project Structure owns current unit declarations **and** explicit per-unit overrides **without** duplicating Settings selections **or** requiring a structural Projection.

### Applicable conditions

1. resolve **and** load the exact current caprmedio_framework_settings Artifact **and** caprmedio_<project_name>_settings Artifact **and** the Default Settings Artifact; evaluate framework parameter resolution against `CA-E-450-CORE_META_MODEL-EVALUATION_APPROACH--validate-framework-parameter-fallback`.
2. accept **only** enabled catalog Artifact Types, Atom Content Roles **and** their qualified Types, **and** Governance Origins.
3. accept **only** `medium` **or** `high` artifact creation strictness.
4. accept **only** `silent` **or** `verbose` interaction reporting. select **every** allowed value through Framework Instance Settings **and** confirm that the effective reporting default follows that selection **without** changing source Atoms, using Project Settings as reporting authority, **or** applying an independent Atom-fixed default.
5. validate initialization inputs against Project Settings field authority **and** default **and** Project Authority Modes against Framework Instance Settings field authority, **and** explicit per-unit overrides against Project Structure field authority; do **not** hard-code this Project's selected values **in** the Evaluation.
6. reject unknown keys **when** the governing schema marks their table closed.
7. confirm a second parse produces identical effective settings **and** direct Project Structure resolution uses the same selected declaration bytes **and** consumed Settings revisions, including Default Settings **when** it supplies consumed values; deleting a legacy structural Projection does **not** change those results.

### Acceptance criteria

**every** valid selection resolves deterministically **and** **every** invalid selection fails closed with the exact key **and** allowed values.

### Failure disposition

record a Concern naming the accepted invalid value, rejected valid value, **or** non-deterministic result **and** stop settings-schema readiness.

## Details
