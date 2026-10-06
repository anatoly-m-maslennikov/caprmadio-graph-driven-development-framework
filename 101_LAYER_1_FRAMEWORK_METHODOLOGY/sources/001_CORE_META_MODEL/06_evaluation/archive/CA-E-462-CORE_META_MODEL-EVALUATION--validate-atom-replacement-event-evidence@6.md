---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Journal/Record"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
    - "Atom/Content Role: Operations"
    - "Journal"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 6
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-R-807
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Atom replacement event evidence

## Claim checked

the Evaluation **must** check whether an Atom replacement satisfies CA-R-807. Journal acceptance is **not** proof that the replacement is correct.

## Checks

- report a failed replacement Evaluation **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched.
- verify that **every** named successor was Active **before** the predecessor was archived, that the archive preserves the predecessor's exact prior bytes **and** Version, **and** that **`=1`** authoritative Journal event records that replacement.
- check event field representation against the selected Delivery authority. a format check alone **must not** be reported as proof of replacement correctness.
- repeated submission of the same event **must not** create another authoritative record.

## Failure disposition

a failed **or** unresolved replacement Evaluation **must not** prevent the Journal from preserving the observed event under CA-R-1491. preserve the supplied identities **and** evidence **without** inventing a conforming replacement **or** claiming that a failed check passed. correction changes the governed source through its authorized Process; it does **not** rewrite accepted history.

this Evaluation **must not** require a Git Commit **or** a particular Journal serialization.
