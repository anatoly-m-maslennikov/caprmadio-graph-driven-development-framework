---
atom_id: CA-R-1829
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE structural request dispatch"
  depends_on: [Tool, Workflow, Action, Scope Unit, Project Structure, Workflow Run, Journal]
relations:
  relates_to: [CA-O-015, CA-O-012, CA-O-013, CA-O-014, CA-O-139, CA-O-140, CA-O-141, CA-O-142, CA-O-143, CA-O-144]
---
# Summary

Dispatch one bounded Scope Unit change

## Scope

The PROGRAMMATIC Tool/PROJECT_STRUCTURE capability for exactly one requested Create, Rename, Move, or Remove Scope Unit change through CA-O-015v8. A filesystem folder is a Carrier observation, not a new Scope Unit declaration.

## Claim

The Tool **must** accept one typed structural request and invoke the accepted CA-O-015 step graph without replacing its authority, Action meaning, transition guards, or shared Run/Journal contract.

## Details

- Input is `operation`, target identity, expected current TOML revision, and an exact proposed declaration delta; Rename/Move additionally name the old and new identity/path/parent, and Remove names the declared preservation or breakage disposition.
- The authoritative tree is `.caprmedio_caprmedio/project_structure.toml`; the Tool must read declared `authority_path` and `delivery_path` as distinct fields and must not infer either from a folder listing.
- The Tool returns a typed result: `completed`, `no_op`, `blocked`, `stale`, `conflict`, `permission_denied`, `partial`, or `rolled_back`, with exact source identities/revisions, affected identity/reference/Carrier sets, actual effects, and evidence/Run references where they exist.
- `no_op` requires the requested declaration and required reference state already to equal the authorized target; no mutation is performed. A never-started denial has no fabricated Run or journaled completion.
- CA-O-139 through CA-O-144 retain source selection, proposal, assessment, authorization, cutover, and result assessment ownership respectively. Shared Run support remains owned by its existing contract; this Requirement creates no second Journal schema.
