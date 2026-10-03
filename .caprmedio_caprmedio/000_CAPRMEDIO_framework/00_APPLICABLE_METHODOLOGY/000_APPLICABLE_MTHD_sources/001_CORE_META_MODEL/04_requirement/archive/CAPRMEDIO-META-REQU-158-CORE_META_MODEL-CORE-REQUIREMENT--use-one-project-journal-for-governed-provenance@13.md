---
cce_version: cce_1
cce_form: obligation
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
version: 13
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
---
# Use one Project Journal for governed provenance

**every** Project **must** use **`=1`** authoritative Journal for **all** governed events, including Artifact changes, Workflow Runs, Step Runs, **and** Action executions, **and** Implementation events. this Project-wide Journal is its Work Journal. **every** admitted event record **must** retain **`=1`** canonical Event identity **and** be recorded **only** once as historical authority; another log **or** view references that record instead of independently recording the same historical fact. distinct events **in** the same execution remain distinct records.

the Journal's append-only history **must** remain replayable, checkable, **and** recoverable independently of a version-control system **or** another secondary record. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.
