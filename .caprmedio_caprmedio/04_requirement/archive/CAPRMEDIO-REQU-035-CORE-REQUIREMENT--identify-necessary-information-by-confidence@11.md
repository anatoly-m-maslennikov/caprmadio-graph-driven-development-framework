---
version: 11
updated_at: "2026-09-11 02:13:22 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-003
  relates_to:
    - CA-M-271
subjects:
  governs:
    occurrent:
      - "Project/information necessity assessment"
  depends_on:
    continuant:
      - "Project"
      - "Atom/Local Tier: Principle"
      - "Atom"
      - "Atom/Claim"
      - "AI Agent"
      - "Relation"
      - "Subject"
      - "Confidence Threshold"
cce_version: cce_1
cce_form: obligation
atom_id: CAPRMEDIO-REQU-035
---
# Identify necessary information by confidence

an AI Agent's assessment of necessary Project information **must** use progressive context acquisition: read **every** active Project Principle **before** using indexes, Relations, **and** Subjects **to** identify applicable Atoms; read **and** check the full Claims of those Atoms; expand inspection **when** dependencies, conflicts, missing evidence, **or** uncertainty require it. indexes, Relations, **and** Subjects support discovery **and** **must not** substitute for checking the applicable Claims. shared ancestry, descendancy, **or** structural scope alone **must not** require loading **every** Atom's full content.

the information is necessary **when** its omission would leave the AI Agent below the effective Confidence Threshold resolved under CA-M-271. the confidence **and** threshold remain operational heuristics, **not** comparable probabilities across configurations.
