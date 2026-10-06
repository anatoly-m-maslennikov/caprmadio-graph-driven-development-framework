---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Project Structure"
  depends_on:
    - "Artifact/Revision"
    - "Journal"
    - "Carrier"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-D-440"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind Project Structure revisions to source evidence

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.
