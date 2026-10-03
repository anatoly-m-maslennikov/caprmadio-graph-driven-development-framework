---
atom_id: CA-R-1186
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - TOOLS/Job
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 00:26:21 +0400
relations: {}
---
# Own Independently Executable Framework Tools

TOOLS **must** own independently executable Tools classified by behavior as Hooks, Finders, or Doers, with Checkers governed as a Finder specialization rather than a separate Scope Unit. Hooks emit triggers into Tool flows and have no read, classification, or mutation authority beyond observing their registered boundary.
