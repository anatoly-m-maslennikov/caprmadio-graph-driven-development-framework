---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "semantics"
  depends_on:
    - "Atom/Content Role"
    - "Implementation"
    - "Action"
    - "Workflow"
    - "Actor"
    - "Journal/Record"
    - "Relation"
version: 21
updated_at: "2026-09-21 00:39:50 +0000"
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
- Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
- Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns specific reusable Action, Workflow, **and** Actor participation/authorization behavior under CA-R-1530; actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.
