---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode: silent"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Framework Instance Settings/interaction/reporting mode/effects"
    - "Framework Instance Settings/interaction/reporting mode/mandatory information"
    - "Artifact"
    - "Skill"
    - "Project"
version: 7
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"relates_to":["CAPRMEDIO-GOV-REQU-294","CA-R-1439","CA-R-1440","CA-R-1558","CA-O-052","CAPRMEDIO-META-REQU-675"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Report in silent mode

**to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.
