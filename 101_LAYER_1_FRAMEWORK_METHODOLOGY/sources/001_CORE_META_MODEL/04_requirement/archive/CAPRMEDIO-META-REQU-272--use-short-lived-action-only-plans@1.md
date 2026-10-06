---
subject_scope: lifecycle-traceability
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-270--use-change-plans-and-implementation-record-projections
  child_of:
    - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
---
# Requirement — Use short-lived action-only Plans

A Plan is one short-lived Atom for one bounded execution package. One Plan file
contains one or more action points; CAPRMEDIO does not create one file per
action point. Create a separate Plan only when a subset of work needs an
independent owner, lifecycle, execution boundary, or terminal disposition.

Every Plan belongs to exactly one structural `scope_path`: one Layer or one
Feature. In base mode, project scope acts as the implicit Layer and Feature.
Action points owned by different explicit scopes belong in separate Plans.

A Plan may declare at most one primary source: either one Analysis Atom or one
Concern Atom. The source is optional when the action points are clear directly
from operator input. A primary source is strongly recommended when a Plan has
more than ten action points, so the Plan can remain action-only while its
reasoning and context stay independently reviewable.

An action point is one executable change instruction with an identified
operation, one or more governed artifacts or native project targets, and an
observable completion condition. Operations may add, refine, replace, archive,
review, or otherwise change their targets. A Plan may also state ordering,
dependencies, and ownership needed to execute its action points.

A Plan contains only action points and their execution controls. Findings,
alternatives, interpretation, explanatory narrative, and rationale belong to
Analysis. A Plan does not become Requirement, Method, Evaluation, Delivery, or
Implementation authority merely because its actions affect those roles.

While active, the Plan may be revised and executed. A fully executed Plan moves
unchanged to `done/`. An abandoned Plan, or one fully absorbed by another Plan,
moves unchanged to `archive/`. These terminal conditions are derived from
placement rather than duplicated in frontmatter.

Projects may omit a Plan for a trivial direct change. A Plan is expected when
work spans multiple governed artifacts, Content roles, `scope_path` values, or
native implementation targets.

## Primary claim

One short-lived, single-scope Plan file coordinates one or more action points,
optionally identifies one Analysis or Concern source, and terminates in `done/`
after execution or `archive/` after abandonment or absorption.
