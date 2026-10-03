---
atom_id: CA-P-941
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - CA Main Skill Installation
    occurrent:
      - CA Main Skill Vertical Slice Installation
  depends_on:
    occurrent:
      - CA-P-940
version: 2
updated_at: 2026-09-07 19:43:08 +0000
autonomous_confidence_threshold: 99
relations: {}
---
# Install CA Main Skill Vertical Slice

**when** CA-P-940 is Done, **then** the Assignee **must** install one versioned CA vertical slice containing the accepted authority snapshot, runtime Tools, MCP surface, canonical Skill, and the Codex host adapter.

## Scope

`((accepted source Carriers from CA-P-936 through CA-P-940) union (content-addressed release, installation manifest, launchers, service definitions, Codex host registrations, digests, receipts, rollback boundary, and installation checks))`

## Definition of Done

the Task is **not done if** (installation mutates outside the authorized boundary, includes uncommitted or unvalidated source, changes unrelated Hooks or host configuration, lacks exact source and installed digests, cannot be rolled back, leaves mixed release versions, or bypasses the installed-execution guard **or** manual and automatic lifecycle controls are not reachable from the installed runtime **or** Codex does not discover the intended host adapter **or** installation proof is reported as runtime proof **or** clean-install and upgrade checks fail).

## Details

publish and activate one immutable release within the host-support boundary established by CA-P-936. Claude installation is outside this Task. keep source validation, installation result, process state, and runtime behavior as separate evidence classes. preserve existing disabled Hook state unless the accepted authority and explicit installation boundary require a bounded trigger adapter.
