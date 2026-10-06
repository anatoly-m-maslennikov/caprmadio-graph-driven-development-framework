---
atom_id: CA-M-225
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Retrieval"
  depends_on:
    - "Applicable Methodology"
    - "Atom/Subjects"
version: 10
updated_at: "2026-09-10 03:25:26 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Retrieve Applicable Methodology Mechanically

**to** retrieve Applicable Methodology for one Subject **or** Process query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
