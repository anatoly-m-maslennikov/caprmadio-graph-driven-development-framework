---
atom_id: CA-R-1186
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "TOOLS/Goal"
  depends_on:
    - "PROGRAMMATIC"
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Own Independently Executable Framework Tools

TOOLS **must** own independently executable Tools classified by behavior as Hooks, Finders, or Doers, with Checkers governed as a Finder specialization rather than a separate Scope Unit. Hooks emit triggers into Tool flows and have no read, classification, or mutation authority beyond observing their registered boundary.
