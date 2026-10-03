---
atom_id: CA-D-055
subjects:
  governs: "delivery"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  delivery_for:
    - CA-R-1070
    - CA-R-1164
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver the Project Graph State generator

The canonical source carrier for `GENERATE_PROJECT_GRAPH_STATE` is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py`. It exposes mutation-free description and dry-run modes, writes both current Scope Unit Graph Projections only with explicit apply through the selected installed Tool release, and owns no projected authority.
