---
atom_id: CA-D-528
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
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/journal carrier"
  depends_on: [Journal, Workflow Run, Step Run, Action, Initiative, Implementation]
relations:
  delivery_for: [CA-R-1822, CA-R-1823, CA-R-1824]
---
# Summary

Extend the sealed Work Journal for selected Run evidence

## Scope

The backward-compatible selected-Run evidence extension of the existing sealed
`work_journal.py` append/receipt library. It is not a separate Journal format.

## Claim

The Project Work Journal **must** accept a schema-v5 `workflow_execution`
event which preserves schema-v4 read support and carries selected-Run evidence
without pretending that every Action has a Workflow parent.

## Details

- The v5 envelope retains the existing sealed Event identity, stable action
  identity, admitted Event Type, author, timezone-qualified occurred time, LLM
  session, structural scope, and digest. It adds sealed `initiative`, `run`,
  ordered `definition_bindings`, safe `input_ref`, `result_ref`, `effect_refs`,
  and `redaction` fields.
- `run` contains a distinct `run_id`, `kind` (`workflow`, `step`, or `action`),
  exact definition Atom ID/Version/path/digest, and optional real parent and
  predecessor/successor references. Parent fields are absent for a standalone
  Action. `definition_bindings` records the Workflow graph's actual admitted
  Workflow/Step/Action revisions in canonical order.
- Receipt/durability status is not part of the immutable event payload. The
  service result and runtime pending-evidence carrier derive `durable` from the
  actual append receipt or `pending` from the preserved append diagnostic; a
  retry never mutates the original event. The event-Type mapping and outcome
  values are exactly CA-R-1823's mapping. No secrets, mutable source snapshot,
  invented status, or duplicate view record is serialized.
- The library continues to seal, validate, append, fsync, reconcile identical
  Event identities, reject conflicting payloads, and return canonical receipts
  through `work_journal.append_sealed_events`. The pending carrier preserves
  the original sealed bytes under `.caprmedio_runtime/state/work_journal/pending/`;
  receipts stay under the existing `.../receipts/` path. Recovery retry uses
  those same original bytes and Event identity; a separately warranted
  `Recovered` event has distinct bytes and identity and cannot mutate the
  pending terminal event.
