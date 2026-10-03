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
version: 6
updated_at: 2026-08-27 20:55:44 +0400
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

## Completion Record

the Assignee first applied 4,785 byte-preserving Carrier moves under CA-P-108 map d7143edb25823c1a050a843fb4a810c34e85d4dba8c510776170e937860898b5. its complete baseline record remains immutable in [CA-P-109 migration execution evidence](../execution_evidence/CA-P-109-migration-execution.projection.json). under repaired CA-P-108 map 0bc92f7d5220d3f6c8133ea990ad6d286c13ebfb5af837c35728e11c29550238, the Assignee then applied four further byte-preserving Core Meta-Model moves: CA-M-224, CA-M-225, CA-E-379, and CA-D-253. post-validation confirmed 4,526 byte-exact frozen targets, 78 accepted-currentness records, 37 PROGRAMMATIC current revisions, 155 separately mapped current or archive successors, 2,442 exact persistent retained Carriers, two exact post-freeze retained Carriers, 2,153 retained .caprmedio_install Carriers, 578 checked source-directory shells, the empty 002_INSTALLED_EXTENSIONS marker, no Applicable Methodology output, and no unexpected mapped-shell Carrier. the invalid colliding CA-P-107 evidence remains a non-Atom Projection. a second map-aware application requires no write. [CA-P-109 v17 incremental execution evidence](../execution_evidence/CA-P-109-v17-incremental-migration-execution.projection.json) records the exact operation set and checks.
