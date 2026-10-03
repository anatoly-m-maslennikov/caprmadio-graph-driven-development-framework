---
atom_id: CAPRMEDIO-GOV-REQU-749
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Concern/Type"
project_graph_state:
  artifacts:
    enabled_types:
      - concern:question
      - concern:problem
      - concern:risk
      - concern:opportunity
version: 12
updated_at: "2026-09-10 08:02:35 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
---
# Register Type Values for Concern Atoms

Question **and** Problem retain their canonical admission under CA-R-1231 **and** **must** use Carrier tokens `question` **and** `problem`, respectively. Risk with Carrier token `risk` **and** Opportunity with Carrier token `opportunity` **must** be registered as additional internal values of `Atom/Content Role: Concern/Type`.
