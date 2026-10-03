---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Project Configuration"
  depends_on:
    - "Project"
    - "Extension"
    - "Framework Instance Settings"
version: 11
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate Project Configuration Rules from Current Settings

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
