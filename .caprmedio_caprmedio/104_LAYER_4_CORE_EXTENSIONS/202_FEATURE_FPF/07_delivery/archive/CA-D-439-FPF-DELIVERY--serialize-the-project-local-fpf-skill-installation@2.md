---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "FPF"
  depends_on:
    - "Skill"
    - "Extension Candidate"
    - "Carrier"
version: 2
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize the project-local FPF Skill installation

The activated Codex-facing FPF Skill **must** use project-local installation path `.agents/skills/fpf/`, package identity `fpf`, and direct invocation `$fpf`; no `ca` Skill, `ca` wrapper, user-global FPF mutation, or alternate Skill identity belongs to this Extension installation.
