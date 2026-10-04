---
atom_id: CA-D-528
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:03:24 +0400"
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
- Before append, the library seals the immutable event bytes and a distinct
  sealed `append_context` containing `author`, `local_date`, `timezone`, and
  the resolved original partition reference. The pending carrier under
  `.caprmedio_runtime/state/work_journal/pending/` preserves both byte strings
  and digests, the Event ID, actual result/effect references, diagnostic, and
  retry linkage. Receipts remain under the existing `.../receipts/` path; this
  carrier is runtime recovery evidence, not a second Journal.
- `work_journal.append_sealed_events` continues to seal, validate, append,
  fsync, reconcile, and return canonical receipts. Its Event-ID reconciliation
  is global across Journal partitions and receipt/history indexes: identical
  original bytes return the one canonical receipt wherever found; different
  bytes under one Event ID are an integrity collision. A collision preserves
  the canonical event/receipt/history and pending original without overwrite or
  mutation; it cannot create a date-partition duplicate.
- Recovery retries only the original event bytes, Event ID, and sealed append
  context. A restart, changed clock, timezone, or date rollover must reuse the
  original author/local-date/timezone/partition choice rather than recompute
  it. If bytes were fsynced before the receipt write, recovery reconciles that
  one on-disk event to its receipt and never appends another event. A separately
  warranted `Recovered` event has distinct bytes and identity and cannot mutate
  the pending terminal event. No append/recovery path invokes an executor,
  dispatches a Step, creates a Run, or replays an effect.
