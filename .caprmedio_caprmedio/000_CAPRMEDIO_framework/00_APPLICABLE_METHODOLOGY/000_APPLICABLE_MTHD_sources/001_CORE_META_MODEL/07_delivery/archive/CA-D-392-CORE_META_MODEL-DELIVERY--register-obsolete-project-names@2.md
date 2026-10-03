---
atom_id: CA-D-392
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Project Scope Unit Graph Projection"
  depends_on:
    continuant:
      - "Project Settings"
      - "Project Name"
      - "Obsolete Project Name"
version: 2
updated_at: "2026-09-11 15:04:40 +0400"
relations:
  child_of:
    - "CA-R-1052"
---
# Register obsolete project names

the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Name **or** Obsolete Project Name).
