---
subjects:
  declared:
    continuant:
      - provenance
cce_version: cce_1
cce_form: obligation
version: 3
updated_at: 2026-08-23 16:16:20 +0400
---
# Reconcile Git and Journal provenance in both directions

The Toolset MUST provide deterministic, idempotent reconciliation in both directions between real-change Git commits and canonical Journal events. It MUST identify a Git commit without its expected Journal event, a Journal event whose bound real-change commit is absent or unreachable, duplicate action or event bindings, mismatched subject revisions or digests, and Journal-only commit watermark lag.

Reconciliation MAY append missing evidence only when it can derive that evidence from sealed durable action state and reachable repository history without invention. Otherwise it MUST preserve the discrepancy as explicit blocked state for operator resolution. A reconciled action MUST expose its action identity, Initiative, real-change commit SHA, Journal event identity, affected subject identity and revision or digest, and Journal-batch commit SHA.
