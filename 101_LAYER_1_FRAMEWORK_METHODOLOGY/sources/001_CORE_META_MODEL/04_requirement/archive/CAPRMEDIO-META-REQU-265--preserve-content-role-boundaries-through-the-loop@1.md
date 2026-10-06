---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct
      - CAPRMEDIO-META-REQU-093--analysis-and-ops-fact-boundary
      - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
      - CAPRMEDIO-META-REQU-104--keep-requirements-realization-agnostic
      - CAPRMEDIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Requirement — Preserve Content-role boundaries through the loop

Every transition through Concern, Analysis, Requirement, Method, Evaluation,
Delivery, Implementation, and Ops produces or updates the meaning owned by the
receiving Content role without converting the source meaning into that role or
implying completion of a later role.

In particular:

- Analysis may inform a Requirement but does not establish it without
  acceptance;
- a Requirement states the desired outcome but does not select its Method;
- Method, Evaluation, and Delivery specify different realization obligations;
- Implementation materially realizes accepted claims but does not prove that
  they pass Evaluation or succeed in operation; and
- Ops records enacted facts but does not silently rewrite normative authority.

Relations carry meaning between roles while every related artifact retains its
own identity, authority, lifecycle, and owning role.

## Primary claim

CAPRMEDIO transitions connect its eight Content roles without allowing any role
to substitute for another or imply that a later role has been completed.

## Rationale

This adapts FPF Role–Method–Work Alignment to the complete CAPRMEDIO loop while
preserving the independently governed contribution of every role.
