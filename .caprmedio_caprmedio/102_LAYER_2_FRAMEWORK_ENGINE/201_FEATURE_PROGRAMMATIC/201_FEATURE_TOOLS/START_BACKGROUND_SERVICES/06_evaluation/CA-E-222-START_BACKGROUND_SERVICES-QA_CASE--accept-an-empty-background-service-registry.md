---
subjects:
  governs: "Background Service/Registry"
  depends_on: []
version: 10
updated_at: 2026-09-15 03:37:14
relations:
  evaluation_for:
    - CA-R-857
    - CA-M-104

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Accept an empty background-service registry

## Claim checked

the service starter is usable **before** **any** background service is delivered.

## Test case

Install a release whose valid service registry **contains** zero services; invoke dry-run, apply, **and** status.

## Acceptance criteria

**all** invocations succeed **and** report zero planned, started, enabled, **and** running services. No service runtime directory, PID, log, cache, process, governed carrier, Git state, selected Tool release, **or** temporary-state byte changes.

## Failure disposition

Reject delivery **if** an empty valid registry is an error **or** produces **any** side effect.
