---
subject_scopes:
  - development-flow
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
---
# Requirement — Reconcile the Development Backlog after release

After the Release Record is accepted, CAPRMEDIO reconciles the Development
Backlog against its exact released manifest.

Candidates whose promoted Atoms were fully delivered in that release are
removed from the Development Backlog. Unfinished, partially delivered,
excluded, or newly deferred candidates remain unscheduled or move to another
target version. A candidate cannot be removed as shipped unless the released
manifest accounts for its promoted Atoms.

The Development Backlog does not retain a completed-work section. Reconciliation
appends Journal records and regenerates the Projection. Release Records, Plans
under `done/`, and Git history preserve what shipped, what was executed, and how
the planning allocation changed.

## Primary claim

Release reconciliation removes fully shipped candidates from the Development
Backlog and retains or reschedules every candidate not fully accounted for by
the released manifest.
