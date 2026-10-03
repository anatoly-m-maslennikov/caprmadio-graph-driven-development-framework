---
subjects:
  governs: "Project Configuration"
  depends_on:
    - "Project"
    - "Extension"
    - "Framework Instance Settings"
version: 12
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
---
# Separate Project Configuration Rules from Current Settings

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
