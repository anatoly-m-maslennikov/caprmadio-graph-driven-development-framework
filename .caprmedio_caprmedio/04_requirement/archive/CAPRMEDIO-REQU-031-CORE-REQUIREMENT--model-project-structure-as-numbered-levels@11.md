---
version: 11
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001
subjects:
  governs:
    continuant:
      - "Project/Structural Level"
  depends_on:
    continuant:
      - "Scope Unit"
      - "Structural Level"
      - "CAPRMEDIO Framework Instance"
      - "Project"
cce_version: cce_1
cce_form: obligation
atom_id: CAPRMEDIO-REQU-031
---
# Model project structure as numbered levels

CAPRMEDIO **must** model the caprmedio Scope Unit at Structural Level `0`, **`>=0`** upstream Structural Levels with negative numbers, **and** **`>=0`** downstream Structural Levels with positive numbers; a Structural Level groups peer positions but does **not** itself establish parentage, order, **or** authority.
