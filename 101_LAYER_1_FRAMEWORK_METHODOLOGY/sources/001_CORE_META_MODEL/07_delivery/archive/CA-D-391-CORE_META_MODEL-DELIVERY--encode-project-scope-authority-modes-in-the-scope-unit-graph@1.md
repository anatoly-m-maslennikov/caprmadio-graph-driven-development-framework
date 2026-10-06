---
atom_id: CA-D-391
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Project Scope Unit Graph Projection/Authority Modes"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Project"
      - "Scope Unit"
      - "Authority Mode"
version: 1
updated_at: "2026-09-10 20:55:05 +0400"
relations:
  child_of:
    - "CA-R-1430"
---
# Encode project scope authority modes in the Scope Unit Graph

the generated Project Scope Unit Graph Projections **must** expose the effective `authority_mode` selected by Framework Instance Settings for the Project **and** **every** current Scope Unit **without** selecting **or** owning that mode.
