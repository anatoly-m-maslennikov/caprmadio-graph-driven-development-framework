---
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Scope Unit"
    - "Atom"
version: 13
updated_at: "2026-09-15 21:31:49 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Derive the Project Scope Unit Graph and Sources Projection from Configuration Authority

the Project Scope Unit Graph generator **must** use the authoritative Project Structure Artifact under CA-R-1483, CA-R-1484, **and** CA-D-440 as the source of accepted Scope Unit declarations **and** concrete bindings.

- Project Atoms, actual Directory Carriers, Settings, **and** Journal evidence **may** supply observations **and** checks against those declarations; they **must not** independently redefine them.
- a generated Graph **or** Sources Projection **must not** become Project Structure authority, select settings, **or** become a semantic input **to** its own generation.
- show a declared Scope Unit even **when** its folder **or** active Goal is absent. report observed undeclared folders **and** mismatches separately **without** accepting them as declarations.
- **if** the Project Structure Artifact is missing **or** invalid, report the unresolved authority; do **not** claim that an observed folder graph reconstructs accepted Project Structure.
