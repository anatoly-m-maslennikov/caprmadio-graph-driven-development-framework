---
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "IS_BORNE_BY"
  depends_on:
    - "Primary Entity"
    - "Subject"
version: 6
updated_at: 2026-09-07 09:59:57 +0000
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Give Primary Entity Occurrences No Bearer

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.
