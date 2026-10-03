---
atom_id: CA-D-055
subject_scopes:
  - delivery
version: 2
updated_at: 2026-09-04 03:10:59 +0400
relations:
  delivery_for:
    - CA-R-1070
    - CA-R-1164
---
# Deliver the Project Graph State generator

The canonical source carrier for `GENERATE_PROJECT_GRAPH_STATE` is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py`. It exposes mutation-free description and dry-run modes, writes both current Scope Unit Graph Projections only with explicit apply through the selected installed Tool release, and owns no projected authority.
