---
atom_id: CA-R-1829
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:03 +0400"
subjects:
  governs: "Tool/PROJECT_STRUCTURE structural request dispatch"
  depends_on: [Tool, Workflow, Action, Scope Unit, Project Structure, Workflow Run, Journal]
relations:
  relates_to: [CA-O-015, CA-O-012, CA-O-013, CA-O-014, CA-O-139, CA-O-140, CA-O-141, CA-O-142, CA-O-143, CA-O-144]
---
# Summary

Dispatch one bounded Scope Unit change

## Scope

The PROGRAMMATIC Tool/PROJECT_STRUCTURE route for exactly one requested Create, Rename, Move, or Remove Scope Unit change through CA-O-015v8. A filesystem folder is a Carrier observation, not a new Scope Unit declaration.

## Claim

The route **must** supply one typed `parameters` payload through CA-D-527's `run_selected_operation(request) -> result` contract and invoke the accepted CA-O-015 step graph without replacing its authority, Action meaning, transition guards, or shared Run/Journal contract.

## Details

- The caller uses CA-D-527's sole outer request and result interface, including its default `preview`, explicit `execute`, pinned definition bindings, sealed Initiative and authorization, idempotency, receipt, and retry semantics. This route does not copy, rename, or supplement those outer fields.
- Route-specific `parameters` contain `operation`, target identity, expected current TOML revision, exact proposed declaration delta, current reference frontier, and the authorized preservation/recovery and Goal-coverage dispositions. Rename/Move additionally name the old and new identity/path/parent; Remove names the declared preservation or breakage disposition.
- The authoritative tree is `.caprmedio_caprmedio/project_structure.toml`; the Tool must read declared `authority_path` and `delivery_path` as distinct fields and must not infer either from a folder listing.
- The route result is a `structural_result`, separate from CA-D-527's service `disposition` and any Workflow Run outcome. Its `state` is one of `completed`, `no_op`, `stale`, `conflict`, `permission_denied`, `partial`, or `rolled_back`, with exact source identities/revisions, affected identity/reference/Carrier sets, actual effects, and evidence references where they exist.
- `no_op` requires the requested declaration and required reference state already to equal the authorized target; no mutation is performed. Preview and any never-started service disposition have no structural effect and no fabricated Run, Event, or journaled completion.
- CA-O-139 through CA-O-144 retain source selection, proposal, assessment, authorization, cutover, and result assessment ownership respectively. Shared Run support remains owned by its existing contract; this Requirement creates no second Journal schema.

## Source bindings

The route is pinned to CA-O-015v8, CA-O-012v5, CA-O-139v2, and CA-O-140v2; CA-D-527 remains the shared outer service contract.
