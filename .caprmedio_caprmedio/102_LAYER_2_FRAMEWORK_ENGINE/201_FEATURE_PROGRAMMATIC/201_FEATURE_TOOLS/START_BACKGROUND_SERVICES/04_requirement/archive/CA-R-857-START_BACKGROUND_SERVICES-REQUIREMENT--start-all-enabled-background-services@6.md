---
subjects:
  declared:
    continuant:
      - feature-boundary
version: 6
updated_at: 2026-08-23 16:16:20 +0400
---
# Start all enabled background services

`START_BACKGROUND_SERVICES` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES`, and realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/`. It must read one machine-readable registry from the selected installed release, resolve every enabled background script or server before mutation, and start each service that is not already running.

The Tool must use dry-run unless apply is explicit, treat an empty registry as a successful no-op, reject duplicate or unsafe service declarations before starting any process, permit framework implementation only from `.caprmedio_install`, and write PIDs, service state, logs, and Python caches only below `.caprmedio_runtime`. Repeated apply must not start a second instance of a service whose recorded PID is still running.
