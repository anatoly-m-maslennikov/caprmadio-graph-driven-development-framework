---
atom_id: CAPRMEDIO-META-REQU-114
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "semantics"
  depends_on: []
version: 15
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-001
---
# Preserve content role boundaries through CAPRMEDIO loop

**every** transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis owns findings, alternatives, explanation, **and** rationale;
- Plan states intended Tasks **and** Objectives **without** realizing them; an Epic groups contained Epics **and** Tasks **without** adding member actions;
- Requirement states a required outcome **or** boundary **without** selecting its Method;
- Method provides Implementation choices **and** conventions, Evaluation checks Spec authority, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns reusable Action **and** Process behavior **and** Actor participation/authorization policies; actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.
