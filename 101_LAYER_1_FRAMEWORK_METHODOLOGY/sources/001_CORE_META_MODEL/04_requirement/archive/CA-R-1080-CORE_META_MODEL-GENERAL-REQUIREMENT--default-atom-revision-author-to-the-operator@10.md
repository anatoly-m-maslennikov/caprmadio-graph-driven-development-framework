---
atom_id: CA-R-1080
cce_version: cce_1
cce_form: conditional
subjects:
  governs: "Atom/Revision/Author"
  depends_on:
    - "Operator"
version: 10
updated_at: "2026-09-10 03:38:57 +0400"
relations:
  child_of:
    - CA-R-1078
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Default Atom Revision Author to the Operator

**if** an Atom Revision has no explicit Author, **then** its effective Author **must** be the Operator who admits that Revision.
