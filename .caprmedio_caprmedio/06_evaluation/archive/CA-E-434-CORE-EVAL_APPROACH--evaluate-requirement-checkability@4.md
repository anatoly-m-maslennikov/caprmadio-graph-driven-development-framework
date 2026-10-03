---
atom_id: CA-E-434
cce_version: cce_1
cce_form: evaluation
version: 4
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-E-001
subjects:
  governs: "Atom/Content Role: Requirement/checkability"
  depends_on:
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Evaluation"
    - "Atom"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate Requirement checkability

**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the Requirement has a contained **or** linked Evaluation that checks the Requirement using recoverable inputs, a recoverable procedure, **and** a recoverable interpretation of **`=1`** result **in** (`pass`, `fail`); **otherwise**, its checkability Evaluation **must** return `fail`.
