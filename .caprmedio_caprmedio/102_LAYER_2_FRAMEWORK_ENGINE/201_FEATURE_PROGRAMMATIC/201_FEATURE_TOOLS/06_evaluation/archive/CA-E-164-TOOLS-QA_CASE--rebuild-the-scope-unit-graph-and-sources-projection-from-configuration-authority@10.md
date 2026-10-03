---
atom_id: CA-E-164
subjects:
  governs:
    occurrent:
      - "Project Scope Unit Graph Projection/validation"
  depends_on:
    continuant:
      - "Project Settings"
      - "Framework Instance Settings"
      - "Scope Unit"
      - "Atom"
version: 10
updated_at: "2026-09-09 23:04:14 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1070
---
# Rebuild the Scope Unit Graph and Sources Projection from Configuration Authority

## Test case

remove both generated Project Scope Unit Graph outputs from an isolated Project fixture with valid Project Settings, Framework Instance Settings, Project Atoms, **and** actual Scope Unit folders. include a Scope Unit folder **without** an active Goal.

## Acceptance criteria

**`=1`** authorized generator run recreates both outputs from the exact source revisions **and** directory observations, **without** using a previous Projection. the Goal-less Scope Unit remains visible with its authority gap reported. neither Settings Artifact is regenerated **or** modified.
