---
atom_id: CA-D-012
subject_scopes:
  - feature-boundary
version: 5
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-R-857
    - CA-M-104
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CA-R-1064
    - CA-R-1065
---
# Deliver the background-service starter

Realize `START_BACKGROUND_SERVICES` through `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/start_background_services.py`. Install the Tool and `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/background_services.toml` in the same selected release. The Tool exposes machine-readable `describe`, read-only `status`, dry-run `run`, and explicit `run --apply` interfaces.

Each service receives a separate `.caprmedio_runtime/services/<service-id>` directory containing its PID state and stdout and stderr logs. The shared Python cache remains `.caprmedio_runtime/cache/python`. The canonical registry is empty until another accepted Delivery adds an actual background script or server.
