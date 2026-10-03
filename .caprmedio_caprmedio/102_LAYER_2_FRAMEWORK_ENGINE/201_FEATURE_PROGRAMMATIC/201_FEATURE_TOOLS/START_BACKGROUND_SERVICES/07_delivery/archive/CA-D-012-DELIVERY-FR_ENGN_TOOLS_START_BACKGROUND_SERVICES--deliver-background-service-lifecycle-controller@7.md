---
atom_id: CA-D-012
subject_scopes:
  - feature-boundary
version: 7
updated_at: 2026-08-25 01:49:10 +0400
relations:
  delivery_for:
    - CA-R-857
    - CA-M-104
    - CA-R-1124
    - CA-R-1064
    - CA-R-1065
---
# Deliver the background-service lifecycle controller

Realize START_BACKGROUND_SERVICES through 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/start_background_services.py. Install the Tool and background_services.toml in the same selected release. Expose machine-readable describe, read-only status, and dry-run plus explicit apply forms of pause, resume, stop, start, and reload.

Give each service one .caprmedio_runtime/services/<service-id> directory for process state, lifecycle state, logs, budgets, circuit state, and dead-letter references. Keep queue and action state in its declared Runtime state root so lifecycle commands never delete accepted work. Stop and reload use cooperative bounded shutdown and preserve an active mutation until a declared recoverable boundary. Platform-specific supervision remains behind a replaceable adapter.

The registry includes COMMIT_AUTOMATION only when its accepted Delivery and installed launcher exist. Status for that service reports selected release, process identity, admission, queue count and bytes, current action and phase, pending state, Git lease, last success and failure, budget usage, circuit state, and dead-letter count.
