---
tier: "core"
version: 7
updated_at: "2026-09-05 03:48:00 +0400"
llm_session_ids:
  - "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
relations:
  child_of:
    - "CA-M-002"
    - "CA-R-1421"
cce_version: "cce_1"
cce_form: "obligation"
subjects:
  governs:
    continuant:
      - "Project/settings authority"
  depends_on:
    continuant:
      - "Project"
      - "Framework Instance Settings"
      - "Project Settings"
      - "Artifact"
      - "Atom"
---
# Keep selected settings in their authoritative Settings Artifact

the CAPRMEDIO Framework Instance **must** read current selected settings from their authoritative Framework Instance Settings **or** Project Settings Artifact under CAPRMEDIO-META-REQU-675; governing Atoms **must** define the available capabilities, constraints, **and** defaults **without** duplicating a selected settings value as another authority.
