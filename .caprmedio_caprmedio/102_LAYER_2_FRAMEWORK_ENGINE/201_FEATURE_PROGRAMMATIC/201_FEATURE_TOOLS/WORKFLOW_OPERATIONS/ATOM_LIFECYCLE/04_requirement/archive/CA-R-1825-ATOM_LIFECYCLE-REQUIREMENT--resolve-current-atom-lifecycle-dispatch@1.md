---
atom_id: CA-R-1825
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Dispatch"
  depends_on: ["Atom", "Atom/Status", "Atom/Revision", "Artifact/Carrier"]
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  relates_to: [CA-O-127, CA-O-128, CA-O-129, CA-O-145, CA-O-067, CA-O-051, CA-R-866, CA-R-868, CA-R-1041]
---
# Summary

Resolve current Atom lifecycle dispatch

## Scope

The selected one-Atom lifecycle dispatcher: Create, identity-preserving Update, Replace, and Change Status (including Archive as its shortcut).

## Claim

The dispatcher **must** resolve the operation from the exact current Atom Carrier, requested result, and applicable admitted status model. It must not hardcode a Content Role status vocabulary. It selects Create only for a new Carrier, Update only when identity and Summary remain fixed, Replace when Summary changes, and Change Status for a status-only lifecycle transition; Archive is Change Status with the model-admitted archive status. A missing, ambiguous, stale, or unadmitted model/result stops before mutation and returns that diagnostic.

The dispatcher returns the selected operation, exact target, expected current Version/digest, current model revision, proposed result, and a `replace_handoff` when a Summary change was requested. `replace_handoff` is a required result, not an implicit Update side effect.

## Details

This Requirement reuses the accepted native Create/Update/Archive/Replace requirements and evaluations. It adds no competing status model or Run schema; shared Run evidence is owned by `WORKFLOW_OPERATIONS/RUN_SUPPORT`.
