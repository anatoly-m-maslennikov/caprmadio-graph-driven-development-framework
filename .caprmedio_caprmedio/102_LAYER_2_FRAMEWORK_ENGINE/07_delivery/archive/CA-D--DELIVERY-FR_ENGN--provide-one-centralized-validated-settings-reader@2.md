---
subject_scopes:
  - framework-engine-software
  - project-settings
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide one centralized validated Settings Reader

Deliver one shared `SETTINGS_READER` software component inside the installed Engine. It reads `.caprmedio/caprmedio_project_settings.toml`, validates strict versioned Pydantic models, and returns an immutable typed settings snapshot with carrier digest and source-map provenance. It exposes no write operation, business default, environment fallback, or semantic selection.

Every applicable Tool, App service, MCP component, and local control panel consumes this same snapshot contract. Settings mutations use a separate governed Doer that changes RMED authority and regenerates the Project Settings and Map Projections; neither the reader nor the control panel directly edits the Projection.

Candidate alignment: CA-D-001, CA-D-003, CA-M-002, CA-R-004, CA-R-827, CA-R-861.

## Sources

- [Python documentation: `tomllib`](https://docs.python.org/3/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/api/config/)
