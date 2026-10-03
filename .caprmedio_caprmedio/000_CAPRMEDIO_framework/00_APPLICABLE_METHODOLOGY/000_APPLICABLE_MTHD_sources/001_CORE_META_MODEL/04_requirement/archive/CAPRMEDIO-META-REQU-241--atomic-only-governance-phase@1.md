---
subject_scope: framework-boundary
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-228--optional-thin-maintained-views
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-236--drafts-precede-atomic-admission
      - CAPRMEDIO-META-REQU-240--atomic-structural-and-subject-scopes
---

# Requirement — Keep the current governance phase atomic-only

The applied META and GOV layers currently contain only Atomic Artifacts.
Maintained hubs, plans, specifications, projections, and generated views are
not part of the current governance surface.

Existing non-atomic carriers in those layers are deleted. CAPRMEDIO may introduce
maintained artifacts later only after a new Atomic Artifact defines their
semantics, ownership, lifecycle, and relation to Atomic Artifacts.

This phase constraint does not classify Atomic Artifacts by their folder name.
Identity-bearing records remain atomic whether active or archived.

## Primary claim

META and GOV remain atomic-only until maintained artifacts receive new explicit
governance.

## Rationale

Removing partially governed maintained carriers keeps the current control
surface internally coherent while the Atomic Artifact model is finalized.
Their later reintroduction can then follow one deliberate contract instead of
preserving premature structures.
