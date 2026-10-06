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
version: 18
updated_at: "2026-10-04 22:05:34 +0000"
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
---
# Summary

Use one Project Journal for governed provenance

## Scope

CAPRMEDIO-governed provenance events in a Project.

## Claim

**every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. **every** admitted event record **must** retain **`=1`** canonical Event identity **and** be recorded **only** once as historical authority; another log **or** view references that record instead of independently recording the same historical fact. distinct events **in** the same execution remain distinct records.

the Work Journal's append-only history **must** remain replayable, checkable, **and** recoverable independently of a version-control system **or** another secondary record. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.

## Details

Runtime technical and business Journals may preserve their own operational histories in configured local or remote sinks. They are not additional Project Work Journals. A runtime record that represents an already recorded governed-provenance fact references its canonical Work Journal identity; distinct operational observations remain distinct facts under CA-R-1470.
