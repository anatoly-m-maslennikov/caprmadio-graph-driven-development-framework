---
atom_id: CA-R-1824
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:03:24 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/journal recovery"
  depends_on: [Journal, Workflow Run, Action, Initiative, Implementation]
relations:
  relates_to: [CA-R-812, CA-R-1644, CA-R-1720]
---
# Summary

Recover selected Run Journal evidence without replaying effects

## Scope

Durable append and recovery of selected-Run evidence through the existing
Project Work Journal. It excludes a second execution log or Journal.

## Claim

RUN_SUPPORT **must** use the existing sealed Work Journal append/receipt
boundary for selected-Run evidence, retain failed terminal append evidence, and
retry only the identical pending event without replaying its Action effect.

## Details

- Before an append attempt, seal one canonical event and Event identity plus
  one append context containing the original author, timezone, local date, and
  resolved Journal partition. Store pending terminal evidence durably in the
  existing Work Journal runtime state with those immutable event bytes and
  digest, sealed append-context bytes and digest, actual result/effect
  references, append diagnostic, and retry linkage. That state is recovery
  evidence, not another historical Journal or derived Process Log.
- The Event identity is globally collision-safe across all Work Journal
  partitions, including partitions selected by a later process date. Before
  append or recovery, the library must resolve the canonical existing
  receipt/history for that identity across the Journal, not only in a newly
  calculated partition. An identical original event returns its one canonical
  receipt; different bytes under that identity are an integrity collision. The
  collision retains the original event, append context, pending evidence, and
  accepted history, reports the conflict, and never overwrites, re-dates, or
  mutates any of them.
- Retry recording uses only the original Event identity, immutable event bytes,
  and sealed append context. It reuses the original author/local-date/timezone
  partition choice after a restart or date rollover; it cannot recompute a new
  date, context, or payload. If fsync completed before a receipt was persisted,
  recovery reconciles that same on-disk event to one receipt rather than appends
  a second event. A later `Recovered` event is separately admissible only for
  independently established facts under CA-R-1644 and has its own identity; it
  never substitutes for or changes the original pending terminal event.
- The storage-retry operation cannot invoke an Action executor, dispatch a
  Step, create a Run, reset authorization, or change an effect. A new execution
  attempt needs a separately admitted request under CA-R-1821.
- Artifact Change Log and Process Log are reconstructed views referencing the
  canonical Event identities. A failed append or incomplete view coverage is
  visible; no caller may manufacture a view record, receipt, time, outcome, or
  effect to claim recovery.
