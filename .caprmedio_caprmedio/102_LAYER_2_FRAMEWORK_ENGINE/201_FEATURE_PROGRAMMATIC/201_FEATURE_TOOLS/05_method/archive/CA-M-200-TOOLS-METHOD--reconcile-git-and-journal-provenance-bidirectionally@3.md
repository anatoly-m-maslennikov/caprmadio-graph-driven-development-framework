---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - programmatic-mutation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1120
  derived_from:
    - CA-A-058
---
# Reconcile Git and Journal provenance bidirectionally

## Applicable when

Use this Method when comparing reachable Git change history with Work Journal coverage for the same governed action frontier.

## Procedure

1. Seal a reachable Git frontier and the corresponding Journal batch frontier.
2. Normalize both sides to action, Initiative, commit SHA, event ID, subject path, subject revision, digest, batch SHA, and ordering facts.
3. Match Git real-change commits to Journal events in both directions and classify missing, duplicate, unreachable, digest-mismatched, revision-mismatched, and watermark-lag cases.
4. Append a recovered Journal event only when reachable history and sealed durable state prove every required field; otherwise keep the case blocked.
5. Re-run the comparison over the same frontier and emit a stable reconciliation report whose second unchanged run produces no new events.

## Outcome

Git and Journal provenance are either reconciled idempotently or separated into explicit evidence-backed discrepancy classes.

## Failure or stop

Do not infer missing provenance or rewrite Git history; stop recovery whenever required identity, digest, reachability, or batch evidence is insufficient.
