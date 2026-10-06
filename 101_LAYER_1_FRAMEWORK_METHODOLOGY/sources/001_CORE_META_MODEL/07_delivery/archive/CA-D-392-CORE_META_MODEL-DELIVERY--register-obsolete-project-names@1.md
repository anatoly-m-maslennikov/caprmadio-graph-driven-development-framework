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
version: 1
updated_at: "2026-09-10 20:55:09 +0400"
relations:
  child_of:
    - "CA-R-1052"
    - "CAPRMEDIO-REQU-051-REQUIREMENT--use-caprmedio-as-the-canonical-project-name"
---
# Register obsolete project names

the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Name **or** Obsolete Project Name).
