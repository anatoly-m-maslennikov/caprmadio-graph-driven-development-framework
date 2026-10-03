---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject inverse backlink

## Test case

**Fixture:** Store the inverse backlink for a relation already owned by its dependent Atom.

**Expected result:** Fail with the stable inverse-backlink diagnostic and a non-zero exit.
