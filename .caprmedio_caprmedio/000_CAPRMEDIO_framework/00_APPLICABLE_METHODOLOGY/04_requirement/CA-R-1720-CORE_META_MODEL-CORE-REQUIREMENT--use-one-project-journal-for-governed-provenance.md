---
subjects:
  governs: "Journal"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Project"
    - "Artifact"
    - "Implementation"
    - "Action"
    - "Workflow"
    - "Work Journal/Event"
    - "Projection"
    - "Carrier"
    - "Atom/Content Role: Delivery"
version: 17
updated_at: "2026-10-03 02:35:56 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
atom_id: "CA-R-1720"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1720-CORE_META_MODEL-CORE-REQUIREMENT--use-one-project-journal-for-governed-provenance.md
---
# Summary

Use one Project Journal for governed provenance

## Scope

governed events in a Project.

## Claim

**every** Project **must** use **`=1`** authoritative Journal for **all** governed events, including Artifact changes, Workflow Runs, Step Runs, **and** Action executions, **and** Implementation events. this Project-wide Journal is its Work Journal. **every** admitted event record **must** retain **`=1`** canonical Event identity **and** be recorded **only** once as historical authority; another log **or** view references that record instead of independently recording the same historical fact. distinct events **in** the same execution remain distinct records.

the Journal's append-only history **must** remain replayable, checkable, **and** recoverable independently of a version-control system **or** another secondary record. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.

## Details
