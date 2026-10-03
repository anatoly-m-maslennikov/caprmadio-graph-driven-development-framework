---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - graph-app
      - derived-project-read-model
      - graph-projection
    occurrent:
      - source-reconciliation
version: 1
updated_at: 2026-08-25 14:14:00 +0400
autonomous_confidence_threshold: 98
relations:
  derived_from:
    - CA-A-062
---
# Implement the first Graph App vertical slice

WHEN `CA-P-096` has selected a database boundary, THE Assignee MUST implement
one working local Graph App slice from authoritative source ingestion through a
read-only backend and usable HTML/JavaScript graph views.

## Scope

Current active Atoms, complete Work Journals, a disposable derived database,
startup and explicit synchronization, local server endpoints, Requirement and
all-Atom graph pages, and the accepted Markdown and business Projections.

## Definition of Done

THE Task is NOT DONE IF (Atoms or full Journals are not the only authoritative
sources OR deleting the database prevents a complete rebuild OR a filesystem
trigger is trusted as the change truth instead of causing reconciliation OR
the backend can directly mutate governed meaning OR Framework Tools and Skills
cannot use the backend for bounded find and read operations OR the UI cannot
filter by Tier, Layer or Feature, and RMED or non-RMED orphan state OR the UI
cannot reveal current body text and full frontmatter OR Subject, lineage,
current-snapshot, and history Projections cannot be regenerated from the same
source frontier OR runtime state escapes `.caprmedio_runtime`).

## Details

Use a complete rescan at startup, on explicit synchronization, and after a
filesystem trigger until measured scale requires a more complex algorithm.
Write operations continue to target Atom and Journal source carriers through
governed Tools. Dynamic local HTML plus JavaScript is the primary first slice;
a self-contained HTML and `data.js` publication remains an optional derived
export rather than a prerequisite.
