---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-857
    - CA-M-104

---
# Accept an empty background-service registry

## Claim checked

The service starter is usable before any background service is delivered.

## Test case

Install a release whose valid service registry contains zero services; invoke dry-run, apply, and status.

## Acceptance criteria

All invocations succeed and report zero planned, started, enabled, and running services. No service runtime directory, PID, log, cache, process, governed carrier, Git state, or installation byte changes.

## Failure disposition

Reject delivery if an empty valid registry is an error or produces any side effect.
