---
atom_id: CA-D-527
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/caller contract"
  depends_on: [Workflow, Action, Operator, Initiative, Journal, Implementation]
relations:
  delivery_for: [CA-R-1821, CA-R-1822, CA-R-1823]
---
# Summary

Encode shared selected Run request and result contract

## Scope

The small caller-facing contract shared by selected capability, MCP, and
adapter implementations. It is a service interface, not a new Workflow.

## Claim

RUN_SUPPORT **must** expose `run_selected_operation(request) -> result` with
the following exact bounded request and result representations.

## Details

- `request` defaults `mode` to `preview` and requires explicit `execute` to
  start work. It contains `operation_route`; typed `parameters`; optional
  `expected_definition_revisions` (Atom ID, kind, Version, source path, and
  digest); sealed `initiative` (identity, summary, safe reference); explicit
  sealed `operator_authorization` (reference, scope, and freshness evidence);
  optional real `lineage`; and a stable caller idempotency key. Execute also
  carries the assigned stable action and requested Run identities. Unknown
  fields, implicit source selection, ambient authorization, and secret input
  values are rejected.
- `result` contains: disposition (`preview`, `declined`, `blocked`, `started`,
  `terminal`, or `recording_pending`); actual Run IDs and definition bindings
  when started; the truthful outcome/result/effect/report references; canonical
  Event IDs/receipts or recording blocker; currentness/revalidation result; and
  a retry disposition. Preview and unstarted dispositions carry no Run/Event
  identity.
- The service neither decides route-specific domain semantics nor creates a
  second workflow executor. Callers supply their selected route implementation;
  MCP and other adapters reuse this contract and default mutations to preview.
