---
subjects:
  declared:
    continuant:
      - feature-boundary
version: 3
updated_at: 2026-08-23 17:53:53 +0400
relations:
  method_for:
    - CA-R-857
---
# Start registered background services

Verify the selected installation release, parse and validate its `background_services.toml`, expand only registered installation, repository, runtime, Tool-root, and interpreter placeholders, and resolve the complete enabled service set. Reject any executable framework carrier outside `.caprmedio_install`.

For apply, start each non-running service without a shell, give it the project-local installation and runtime addresses, route its stdout and stderr to its runtime service directory, verify that it survives its declared startup grace interval, and atomically record its PID and selected release. If a later service fails during the same invocation, terminate every process started by that invocation and remove their incomplete runtime state.
