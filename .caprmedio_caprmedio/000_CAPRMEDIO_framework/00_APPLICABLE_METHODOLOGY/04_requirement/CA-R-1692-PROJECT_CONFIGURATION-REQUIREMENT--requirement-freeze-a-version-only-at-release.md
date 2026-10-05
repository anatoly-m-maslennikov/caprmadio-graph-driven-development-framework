---
subjects:
  governs: "Version/release"
  depends_on:
    - "Version"
    - "Journal/Record"
    - "Artifact/Revision"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Evaluation"
    - "Extension"
    - "Project Configuration"
version: 19
updated_at: "2026-10-03 02:10:09 +0400"
relations:
  relates_to:
    - "CA-R-1712"
    - "CA-R-1646"
    - "CA-O-025"
atom_id: "CA-R-1692"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1692-PROJECT_CONFIGURATION-REQUIREMENT--requirement-freeze-a-version-only-at-release.md
  source_atom_id: CA-R-1692
  source_atom_revision: 19
  source_sha256: aef0f7a90feda3466a625b61d5cf31f4dd55077d873c7a9f47221989862688aa
  original_relations_sha256: bfb0b24f5e8a3603ba95eca3a7b57448a494f25778bf5c7057c5dfb477919a92
---
# Summary

Requirement — Freeze a version only at release

## Scope

target Versions and their selected authorized release events.

## Claim

a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.

- the release record is a factual Journal Record under CA-R-1712, **not** an Operations Atom.
- its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
- the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
- planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.

## Details

this Project Configuration Claim does **not** impose its release Workflow on **every** Project.
