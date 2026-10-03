---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-087
---
# Reconcile one missed external project change

## Claim checked

The repository-local service detects one eligible project change missed by Hook intake without adopting ambiguous or already governed work.

## Test case

With the service stopped, create one eligible external change without a Hook event, one pre-existing dirty carrier of ambiguous ownership, and one carrier already equal to committed repository state; start the service and run its low-frequency reconciliation.

## Acceptance criteria

The eligible external change becomes one stable queued candidate and follows the normal manager-defined pipeline. The committed carrier is ignored. Ambiguous dirty ownership becomes an explicit blocked outcome with deterministic recovery instructions. No SessionStart or Stop baseline is required, and reconciliation performs no unauthorized Journal, index, commit, or governed-content mutation.

## Failure disposition

Reject reconciliation if it misses or duplicates the eligible change, adopts ambiguous work, depends on host-session lifecycle state, or bypasses the normal queue and pipeline.
