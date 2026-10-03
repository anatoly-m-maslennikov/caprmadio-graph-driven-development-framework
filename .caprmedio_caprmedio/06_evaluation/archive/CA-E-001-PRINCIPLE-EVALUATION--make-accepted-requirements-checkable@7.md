---
atom_id: CA-E-001
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/checkability"
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Evaluation"
version: 7
updated_at: 2026-09-05 01:15:08 +0400
relations:
  child_of:
    - CA-INTENT
---
# Make accepted requirements checkable

**every** accepted Requirement **must** have a contained **or** linked Evaluation **when** the Requirement is used to govern work **or** evaluate a result; that Evaluation **must** check the Requirement using recoverable inputs, a recoverable procedure, **and** a recoverable interpretation of **`=1`** result **in** (`pass`, `fail`).
