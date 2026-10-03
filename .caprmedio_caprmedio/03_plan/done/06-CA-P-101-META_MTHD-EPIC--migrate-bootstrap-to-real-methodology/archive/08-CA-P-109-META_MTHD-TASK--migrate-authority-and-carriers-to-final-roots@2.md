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
version: 2
updated_at: 2026-08-26 16:23:41 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Migrate Authority and Carriers to Final Roots

**when** CA-P-108 is Done, **then** the Assignee **must** apply the frozen migration map transactionally and establish .caprmedio_framework, .caprmedio_project, and .caprmedio_runtime with their accepted ownership boundaries.

## Scope

`(exactly the source Carriers, target Carriers, lifecycle transitions, relation rewrites, and Scope Unit directories enumerated by the accepted CA-P-108 migration map)`

## Definition of Done

the Task is **not done if** (the applied source and target sets differ from the frozen map **or** any persistent methodology or Tool Carrier is outside .caprmedio_framework **or** any governed Project Artifact or evidence Carrier is outside .caprmedio_project without a registered native Type exception **or** .caprmedio_runtime contains governing authority **or** any of CORE_META_MODEL, INSTALLED_EXTENSIONS, or LOCAL_CONFIGURATION lacks its accepted parent-owned Job Carrier **or** any source-Layer Job Claim changes during carrier migration **or** 000_APPLICABLE_MTHD_sources is altered by generated-output materialization **or** any final generated Applicable Methodology Carrier is created before CA-P-110 **or** any Carrier is lost, duplicated, or changed outside its disposition **or** any revised Claim lacks a governed successor and immutable archived predecessor **or** transactional failure cannot restore the exact source frontier **or** a second application is not idempotent).

## Details

apply no discretionary migration decision. preserve the three accepted source-Layer Jobs as governing authority while changing only their mapped identities or Carriers. retire .caprmedio_install only after every durable installed component has an accepted .caprmedio_framework target. stop and request Operator disposition when live state differs from the frozen frontier or any target resolution falls below the Autonomous Confidence Threshold.
