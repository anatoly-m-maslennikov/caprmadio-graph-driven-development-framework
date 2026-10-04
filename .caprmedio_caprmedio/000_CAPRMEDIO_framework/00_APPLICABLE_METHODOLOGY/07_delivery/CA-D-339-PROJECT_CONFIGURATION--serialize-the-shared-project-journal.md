---
subjects:
  governs: "Journal/Carrier"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Project"
    - "Work Journal"
    - "Scope Unit"
    - "Atom/Content Role"
version: 13
updated_at: "2026-10-02 19:18:22 +0400"
relations:
  relates_to:
    - CA-D-308
    - CA-R-1720
atom_id: "CA-D-339"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-339-PROJECT_CONFIGURATION--serialize-the-shared-project-journal.md
---
# Summary

Serialize the shared Project Journal

## Scope

shared Project Work Journal serialization.

## Claim

the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** its registered Project-wide Journal directory. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details
