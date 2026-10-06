---
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "Structural Entity/Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 9
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Prohibit Persisting Derived Containment

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
