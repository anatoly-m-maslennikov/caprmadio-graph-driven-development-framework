---
subject_scopes:
  - runtime
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-458--control-journal-runtime-and-scratch-boundaries
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-306--job-based-carrier-policy
    - CAPRMEDIO-GOV-REQU-475--repeat-ordered-role-folders-in-every-scope
---
# Keep governed Journals in role folders

Every CAPRMEDIO project uses three storage boundaries:

| Boundary | Owned content | Change behavior |
|---|---|---|
| `.caprmedio/` | Governed Atoms, Journals, and Projections; installed methodology; settings; and other durable control-plane carriers | Atom, Journal, Projection, and configuration-specific governed rules |
| `.caprmedio_runtime/` | Ignored reconstructible or resumable run state, checkpoints, caches, recovery material, and temporary materializations | Mutable and disposable between completed workflows |
| Host temporary root | Process scratch and test workspaces | Disposable and cleaned when the owning operation exits |

A governed Journal lives inside the applicable scope's ordered Content-role folder under `.caprmedio/`. CAPRMEDIO does not use a separate `.caprmedio_journal/` root. Every Journal record is one complete UTF-8 JSON value followed by a newline in an NDJSON carrier. Accepted records are never edited, reordered, or deleted. Rotation may create or seal carriers without rewriting accepted records.

A persisted Markdown, TOON, HTML, or other summary derived from a Journal is a Projection. Its declared Journal frontier remains canonical for the represented records, and the Projection is regenerated through its governed procedure.

Nothing under `.caprmedio_runtime/` or the host temporary root may be the only copy of governed truth, durable history, or canonical evidence. Scratch uses the operating system's native temporary root and never an ambient repository path. Cleanup failure is reported as failure.

Short-lived same-directory swap state may exist only for atomic publication and must be replaced or removed before the operation returns.

## Rationale

Keeping each Journal beside the role and scope whose history it owns makes recursive discovery complete and removes a second control-plane root without weakening append-only retention or runtime isolation.
