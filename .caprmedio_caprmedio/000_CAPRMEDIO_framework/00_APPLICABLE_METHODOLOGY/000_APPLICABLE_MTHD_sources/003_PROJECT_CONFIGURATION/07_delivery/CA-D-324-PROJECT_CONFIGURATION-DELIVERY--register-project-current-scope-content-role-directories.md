---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Project"
    - "Scope Unit"
    - "Atom/Content Role"
    - "Carrier"
    - "Artifact/Revision/Status"
    - "Structural Entity"
    - "Directory Carrier"
version: 12
updated_at: "2026-10-02 19:18:22 +0400"
relations: {"relates_to":["CA-D-296","CA-D-451","CA-D-466"]}
atom_id: "CA-D-324"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Register Project Current-Scope Content Role Directories

## Scope

administrative Content Role directory placement at the CAPRMEDIO Project root **and** **in** **every** descendant Scope Unit, including `CORE_META_MODEL`, `INSTALLED_EXTENSIONS`, **and** `PROJECT_CONFIGURATION`.

## Claim

**every** Scope Unit **in** the CAPRMEDIO Project **must** use the same administrative Content Role directory mapping directly under its own authority directory for current-scope placement:

- Concern: `01_concern/`;
- Analysis: `02_analysis/`;
- Plan: `03_plan/`;
- Requirement: `04_requirement/`;
- Method: `05_method/`;
- Evaluation: `06_evaluation/`;
- Delivery: `07_delivery/`;
- Implementation: `08_implementation/`;
- Operations: `09_operations/`.

materialize these directories under `CA-D-296-CORE_META_MODEL-DELIVERY--materialize-content-role-directories-on-first-artifact`. preserve specific Carrier placement rules **and** apply Status placement under `CA-D-466-CORE_META_MODEL-DELIVERY--place-carriers-by-applicable-status-delivery`.

## Details

the Project Scope Unit uses `.caprmedio_caprmedio/` as its authority directory. **every** descendant uses its own declared authority directory **and** reuses this mapping rather than independently defining it.

these administrative directories provide placement; they do **not** become Structural Entities **or** Directory Carriers under `CA-D-451-CORE_META_MODEL-DELIVERY--classify-folders-by-their-carrier-responsibility`.
