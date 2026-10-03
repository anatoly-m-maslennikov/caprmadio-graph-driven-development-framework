---
atom_id: CAPRMEDIO-META-REQU-114
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - semantics
version: 13
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001
---
# Preserve content role boundaries through CAPRMEDIO loop

**every** transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Ops produces **or** updates the meaning owned by the receiving Content role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis owns findings, alternatives, explanation, **and** rationale but **not** the action list;
- an Action Policy governs Actors **and** actions **without** itself acting, a Task states one intended action **without** realizing it, **and** an Epic relates **only** its contained Epic **and** Task members **without** adding member actions;
- Requirement states a desired outcome but does **not** select its Method;
- Method, Evaluation, **and** Delivery specify distinct realization obligations;
- Implementation materially realizes accepted claims but does **not** prove their evaluation **or** operational success; **and**
- Ops records enacted facts but does **not** silently rewrite normative authority.

Relations carry meaning between roles while **every** related artifact retains its own identity, authority, lifecycle, **and** owning role.
