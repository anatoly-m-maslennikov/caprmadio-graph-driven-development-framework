---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - programmatic-mutation
version: 4
updated_at: 2026-09-02 00:15:00 +0400
relations:
  method_for:
    - CA-R-1127
  derived_from:
    - CA-A-058
---
# Reconcile Work Journal coverage from sealed evidence

## Applicable when

Use this Method when a governed action may be missing required Work Journal coverage.

## Procedure

1. Seal one governed action frontier and collect its action identity, authoritative state, reachable provenance, existing Journal events, and the active Journal-event schema.
2. Determine whether the existing events provide the coverage required for that exact action.
3. Classify absent, duplicate, partial, stale, or conflicting coverage without editing existing Journal lines.
4. Append one `recovered` event only when sealed durable evidence determines every schema-required event field and its action binding unambiguously.
5. Re-run the same reconciliation on the unchanged frontier and confirm that it appends no second recovered event.

## Outcome

Each selected governed action has an explicit coverage state: covered, recovered from sufficient evidence, or blocked for operator resolution.

## Failure or stop

Never invent a schema-required event fact, action binding, or provenance fact; preserve insufficient cases as blocked.
