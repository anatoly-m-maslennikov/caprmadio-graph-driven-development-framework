---
tier: core
version: 9
updated_at: "2026-09-05 23:00:00 +0400"
llm_session_ids:
  - "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
relations:
  child_of:
    - "CA-R-1421"
    - "CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary"
subjects:
  governs:
    continuant:
      - "Project/authority mode"
  depends_on:
    continuant:
      - "Project"
      - "CAPRMEDIO Framework Instance"
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Method"
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Delivery"
      - "Atom/Content Role: Plan"
      - "Atom/Content Role: Ops"
cce_version: cce_1
cce_form: obligation
atom_id: CAPRMEDIO-REQU-029
---
# Govern each scope by authority mode

CAPRMEDIO **must** govern the Project root **and** **every** configured structural scope through an `authority_mode` of `strict` **or** `casual` that controls PRMEDO topology completeness **without** weakening active-authority consistency.
