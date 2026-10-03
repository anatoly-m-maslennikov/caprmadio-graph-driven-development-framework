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
version: 3
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Migrate Authority and Carriers to Final Roots

**when** CA-P-108 is Done, **then** the Assignee **must** apply the frozen migration map transactionally and establish .caprmedio_framework, .caprmedio_project, and .caprmedio_runtime with their accepted ownership boundaries.

## Scope

`(exactly the source Carriers, target Carriers, lifecycle transitions, relation rewrites, and Scope Unit directories enumerated by the accepted CA-P-108 migration map)`

## Definition of Done

the Task is **not done if** (the applied source and target sets differ from the frozen map **or** any persistent methodology or Tool Carrier is outside .caprmedio_framework **or** any governed Project Artifact or evidence Carrier is outside .caprmedio_project without its exact registered native Carrier Type exception **or** any root Delivery or intentionally root-native Project Carrier lacks the exception mapped by CA-P-108 **or** .caprmedio_runtime contains governing authority **or** any final Scope Unit lacks its accepted Job Carrier **or** any Job Claim changes during Carrier migration **or** 000_APPLICABLE_MTHD_sources is altered by generated-output materialization **or** any final generated Applicable Methodology Carrier is created before CA-P-110 **or** .caprmedio_install remains **or** any Carrier or directory is lost, duplicated, or changed outside its disposition **or** any revised Claim lacks a governed successor and immutable archived predecessor **or** transactional failure cannot restore the exact source frontier **or** a second application is not idempotent).

## Details

apply no discretionary migration decision. preserve every accepted Job as governing authority while changing only its mapped identity or Carrier. migrate every durable installed component to its accepted .caprmedio_framework target, disposition staging as mapped, and retire .caprmedio_install before completing the Task. stop and request Operator disposition when live state differs from the frozen frontier or any target resolution falls below the Autonomous Confidence Threshold.
