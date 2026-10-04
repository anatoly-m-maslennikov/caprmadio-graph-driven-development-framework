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
version: 14
updated_at: "2026-10-04 22:11:59 +0000"
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
---
# Summary

Serialize the shared Project Journal

## Scope

the shared Project-control Work Journal's serialization.

## Claim

the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details

This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.
