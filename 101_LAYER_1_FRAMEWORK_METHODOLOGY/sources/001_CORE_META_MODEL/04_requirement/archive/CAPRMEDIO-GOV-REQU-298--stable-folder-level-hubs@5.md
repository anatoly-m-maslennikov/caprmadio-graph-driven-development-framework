---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - layout
version: 5
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-410--folder-level-hub-navigation
  child_of:
    - CA-R-1054
---
# Keep durable hubs folder-level

A durable hub MAY directly list stable child areas and their hubs, folders that contain Atoms, enabled Projections, settings, and other long-lived governed carriers.

A hub never enumerates individual atomic carriers. Adding an atom therefore does not require a hub edit. A hub also never lists or links descendants of `.caprmedio_runtime`; runtime state and individual high-churn Journal records are discoverable through their own tools and governed Projections.

## Rationale

Folder-level navigation stays current as immutable atoms and append-only records accumulate.
