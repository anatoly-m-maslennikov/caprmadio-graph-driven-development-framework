---
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    continuant:
      - settings authority
  depends_on:
    continuant:
      - Project Settings
      - Framework Instance Settings
      - Projection
version: 15
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-832-CORE-REQUIREMENT--select-optional-capabilities-through-configuration
---
# Separate Project Settings from the Project Scope Unit Graph

the CAPRMEDIO Framework **must** distinguish the human-editable Project Settings Artifact from generated Project Scope Unit Graph Projections. **only** the Project Settings Artifact owns Operator-selected Project values, while the Framework Instance Settings Artifact owns Framework Instance values; Project Scope Unit Graph Projections are read-only derived views **and** never configuration authority.
