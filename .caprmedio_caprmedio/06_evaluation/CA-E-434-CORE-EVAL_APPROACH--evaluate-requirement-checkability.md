---
cce_version: cce_1
cce_form: evaluation
version: 7
updated_at: "2026-09-17 16:55:18 +0000"
relations: {"child_of":["CA-E-001"],"relates_to":["CAPRMEDIO-META-REQU-124"]}
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

**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the available evidence identifies **all** of the following:

- recoverable inputs for checking the Requirement;
- a recoverable check procedure;
- a recoverable interpretation that yields **=1** result **in** (`pass`, `fail`).

**if** **any** of these conditions is missing, the checkability Evaluation **must** return `fail`. satisfying them does **not** require a separate Evaluation Atom **unless** applicable authority requires that Atom for the particular case under CAPRMEDIO-META-REQU-124; an independently governed Evaluation Claim still follows the Atom boundary rules.
