---
subject_scopes:
  - semantics
tier: core
version: 4
updated_at: 2026-08-22 21:44:14
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-265--preserve-content-role-boundaries-through-the-loop
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Preserve content role boundaries through CAPRMEDIO loop

Every transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, and Ops produces or updates the meaning owned by the receiving Content role without converting the source meaning into that role or implying completion of a later role.

In particular:

- Analysis owns findings, alternatives, explanation, and rationale but not the
  action list;
- an Action Policy governs Actors and actions without itself acting, a Task states one intended action without realizing it, and an Epic relates only its contained Tasks without adding their actions;
- Requirement states a desired outcome but does not select its Method;
- Method, Evaluation, and Delivery specify distinct realization obligations;
- Implementation materially realizes accepted claims but does not prove their
  evaluation or operational success; and
- Ops records enacted facts but does not silently rewrite normative authority.

Relations carry meaning between roles while every related artifact retains its own identity, authority, lifecycle, and owning role.
