---
atom_id: CA-D-392
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    - "Project Settings"
    - "Project Name"
    - "Obsolete Project Name"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-R-1052"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register obsolete project names

the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Name **or** Obsolete Project Name).
