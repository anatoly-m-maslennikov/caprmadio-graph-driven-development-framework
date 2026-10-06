---
subjects:
  governs: "General Artifact Graph"
  depends_on:
    - "Artifact"
    - "Structural Entity"
    - "Scope Unit"
    - "Atom Collection"
    - "Carrier"
    - "CAPRMEDIO Graph"
    - "Structural Entity/Direct Containment"
    - "Atom"
    - "Journal"
    - "Projection"
version: 6
updated_at: "2026-09-17 17:18:52 +0000"
relations: {}
---
# Define General Artifact Graph

a General Artifact Graph **means** the derived CAPRMEDIO Graph that represents governed Artifacts **and** Structural Entities as nodes, locates them by their authoritative Carriers, **and** connects them through the existing direct containment relations. its Structural Entity nodes include Scope Units **and** Atom Collections; its Artifact nodes include Atoms, Journals, **and** Projections.

node identities, Carrier locations, **and** containment come from existing authoritative sources **and** registered containment rules, **not** independently maintained graph declarations. an administrative directory does **not** become a Structural Entity merely because it is a folder. the graph provides their shared structural context **without** duplicating specialized graphs **or** becoming a separate source of authority.
