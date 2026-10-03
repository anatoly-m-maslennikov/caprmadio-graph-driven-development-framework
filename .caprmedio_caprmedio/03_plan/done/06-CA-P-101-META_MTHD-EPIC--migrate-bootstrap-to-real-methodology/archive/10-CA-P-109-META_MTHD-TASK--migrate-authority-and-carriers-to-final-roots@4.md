---
atom_id: CA-P-109
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - CAPRMEDIO Carrier Root Topology
    occurrent:
      - Bootstrap Migration
  depends_on:
    occurrent:
      - CA-P-108
version: 4
updated_at: 2026-08-27 19:52:33 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Migrate Authority and Carriers to Final Roots

**when** CA-P-108 is Done, **then** the Assignee **must** migrate every mapped Carrier to .caprmedio_framework or .caprmedio_caprmedio, retain .caprmedio_install and .caprmedio_runtime as mapped, and defer only mapped source-directory shells to CA-P-114.

## Scope

`(exactly the source Carriers, target Carriers, lifecycle transitions, and Scope Unit directories enumerated by the accepted CA-P-108 migration map)`

## Definition of Done

the Task is **not done if** (any mapped Carrier lacks its byte-exact target **or** any migrated source Carrier remains **or** any persistent retained Carrier differs from its frozen bytes **or** any governed Project Artifact or evidence Carrier is outside .caprmedio_caprmedio without its exact mapped exception **or** any persistent methodology or Tool Carrier is outside .caprmedio_framework without its exact mapped exception **or** .caprmedio_install changes **or** .caprmedio_runtime is treated as a persistent migration input outside its exact map exception **or** any out-of-scope BSEED history, Plan, or evidence Carrier leaves .caprmedio without its exact mapped disposition **or** any mapped Job Carrier lacks its target **or** any Job Claim changes during Carrier migration **or** 000_APPLICABLE_MTHD_sources is altered by generated-output materialization **or** any final generated Applicable Methodology Carrier is created before CA-P-110 **or** any source-directory shell contains a non-retained Carrier **or** any Carrier is lost, duplicated, or changed outside its disposition **or** any revised Claim lacks a governed successor and immutable archived predecessor **or** transactional failure cannot restore the exact source frontier **or** a second application is not idempotent).

## Details

apply no discretionary migration decision. preserve every accepted Job as governing authority while changing only its mapped Carrier. preserve .caprmedio_install as the durable running FRAMEWORK_ENGINE installation. preserve map-declared .caprmedio_runtime entries as ephemeral state. preserve map-declared out-of-scope BSEED history, Plans, and evidence in .caprmedio. do not materialize Applicable Methodology before CA-P-110. use reversible per-file Carrier moves when directory rename or deletion is unavailable, and defer verified-empty source-directory shells to CA-P-114. stop and request Operator disposition when live state differs from the frozen frontier or any target resolution falls below the Autonomous Confidence Threshold.
