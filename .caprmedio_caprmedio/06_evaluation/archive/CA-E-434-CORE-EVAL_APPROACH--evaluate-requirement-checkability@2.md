---
atom_id: CA-E-434
cce_version: cce_1
cce_form: evaluation
version: 2
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-E-001
subjects:
  governs:
    occurrent:
      - "Atom/Content Role: Requirement/checkability"
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Evaluation"
      - "Atom"
---
# Evaluate Requirement checkability

**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the Requirement has a contained **or** linked Evaluation that checks the Requirement using recoverable inputs, a recoverable procedure, **and** a recoverable interpretation of **`=1`** result **in** (`pass`, `fail`); **otherwise**, its checkability Evaluation **must** return `fail`.
