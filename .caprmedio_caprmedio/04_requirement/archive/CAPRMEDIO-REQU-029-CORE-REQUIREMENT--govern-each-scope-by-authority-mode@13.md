---
version: 13
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
    - CA-R-1430
  child_of:
    - "CA-R-1421"
    - "CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary"
subjects:
  governs: "Project/authority mode"
  depends_on:
    - "Project"
    - "CAPRMEDIO Framework Instance"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Operations"
cce_version: cce_1
cce_form: obligation
atom_id: CAPRMEDIO-REQU-029
---
# Govern each scope by authority mode

the caprmedio Project **must** use the Authority Mode selected by its Framework Instance Settings for the Project **and** **every** configured Scope Unit, according to Core Meta-Model policy **without** weakening active-authority consistency.
