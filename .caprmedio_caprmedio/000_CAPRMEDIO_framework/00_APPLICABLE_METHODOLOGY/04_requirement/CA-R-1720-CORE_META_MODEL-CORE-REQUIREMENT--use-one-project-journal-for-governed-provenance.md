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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1720-CORE_META_MODEL-CORE-REQUIREMENT--use-one-project-journal-for-governed-provenance.md
  source_atom_id: CA-R-1720
  source_atom_revision: 18
  source_sha256: dcec820250ae672f8557f3b0b5c9dad247c1fd1166e51905d3cf9b7fe401501f
  original_relations_sha256: 4db6cfcf06eed514b4ef8628dc09a64f173b7b3e68b6692583e0c8383d2a593c
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
