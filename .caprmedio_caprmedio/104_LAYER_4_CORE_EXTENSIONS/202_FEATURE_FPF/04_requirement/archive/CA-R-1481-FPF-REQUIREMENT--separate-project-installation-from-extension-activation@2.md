---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "FPF"
  depends_on:
    - "Extension Candidate"
    - "Installed Extensions Catalog Entry"
    - "Project Configuration"
    - "Skill"
version: 2
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate Project installation from Extension activation

Installing an immutable FPF Extension Candidate **must** register its exact provenance and make its project-local `fpf` Skill available **without** activating its methodology authority; activation **must** require a separate current Project Configuration selection, **must not** mutate upstream or user-global FPF sources, and **must not** be claimed until a fresh Codex session resolves the selected project-local package and invokes it directly as `$fpf` without a `ca` wrapper.
