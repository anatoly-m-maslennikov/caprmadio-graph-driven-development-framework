---
subjects:
  governs: "provenance"
  depends_on: []
cce_version: cce_1
cce_form: obligation
version: 8
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile Git and Journal provenance in both directions

the Toolset **must** provide deterministic, idempotent reconciliation **in** both directions between real-change Git commits **and** canonical Journal events. It **must** identify a Git commit **without** its expected Journal event, a Journal event whose bound real-change commit is absent **or** unreachable, duplicate action **or** event bindings, mismatched subject revisions **or** digests, **and** Journal-only commit watermark lag.

Reconciliation **may** append missing evidence **only** **when** it can derive that evidence from sealed durable action state **and** reachable repository history **without** invention. Otherwise it **must** preserve the discrepancy as explicit blocked state for operator resolution. A reconciled action **must** expose its action identity, Initiative, real-change commit SHA, Journal event identity, affected subject identity **and** revision **or** digest, **and** Journal-batch commit SHA.
