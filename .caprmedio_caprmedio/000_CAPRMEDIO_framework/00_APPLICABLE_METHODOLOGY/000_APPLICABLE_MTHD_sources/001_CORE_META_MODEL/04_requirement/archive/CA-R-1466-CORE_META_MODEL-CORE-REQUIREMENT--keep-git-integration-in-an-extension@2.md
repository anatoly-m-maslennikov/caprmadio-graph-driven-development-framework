---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Extension"
  depends_on:
    - "Core Meta-Model"
    - "Journal"
    - "Projection"
    - "Project Configuration"
version: 2
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep Git integration in an Extension

Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.
