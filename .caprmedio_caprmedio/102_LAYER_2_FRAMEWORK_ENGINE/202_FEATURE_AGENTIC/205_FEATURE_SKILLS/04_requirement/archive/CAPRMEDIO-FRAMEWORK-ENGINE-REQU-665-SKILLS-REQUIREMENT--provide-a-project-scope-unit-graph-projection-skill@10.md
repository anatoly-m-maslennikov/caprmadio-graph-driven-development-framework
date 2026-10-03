---
subject_scopes:
  - skill-boundary
version: 10
updated_at: "2026-09-09 23:04:14 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-REQU-646
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Provide a Project Scope Unit Graph Projection skill

the framework **must** provide `ca-project-settings` as the thin operator-facing Skill that checks **and** rebuilds the Project Scope Unit Graph **and** Sources Projections through their registered deterministic Tool, routes semantic changes **to** the owning RMED Atoms, **and** never edits either output Projection, authors effective values independently, **or** embeds executable Tool logic.
