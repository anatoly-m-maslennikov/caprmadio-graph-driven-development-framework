---
subject_scopes:
  - delivery
version: 1
updated_at: 2026-08-25 02:10:26 +0400
relations:
  delivery_for:
    - CA-R-1070
    - CA-R-1164
---
# Deliver the Project Graph State generator

The canonical source carrier for `GENERATE_PROJECT_GRAPH_STATE` is `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py`. It exposes mutation-free description and dry-run modes, writes both current Scope Unit Graph Projections only with explicit apply through the selected installed Tool release, and owns no projected authority.
