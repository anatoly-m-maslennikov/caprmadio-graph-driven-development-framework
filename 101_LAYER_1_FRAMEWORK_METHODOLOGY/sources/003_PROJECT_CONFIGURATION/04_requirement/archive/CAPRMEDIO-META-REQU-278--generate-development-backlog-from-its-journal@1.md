---
subject_scope: development-flow
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-262--one-development-backlog
  child_of:
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
---
# Requirement — Generate Development Backlog from its Journal

The project has one append-only Development Backlog Journal with the Concern
Content role. Its records add, revise, allocate, move, remove, or promote
one-line work candidates that may anticipate work in any CAPRMEDIO Content role.

CAPRMEDIO automatically generates the current Development Backlog Projection
from the Journal without operator-authored Projection content. The Projection
groups unresolved candidates into unscheduled work, the current target version,
and future target versions. Candidates express Concerns requiring disposition;
they are neither Plans nor specification authority. A target-version allocation
is not a frozen version or release claim.

## Primary claim

CAPRMEDIO derives one current Development Backlog Concern Projection from an
append-only Journal of candidate-planning events.
