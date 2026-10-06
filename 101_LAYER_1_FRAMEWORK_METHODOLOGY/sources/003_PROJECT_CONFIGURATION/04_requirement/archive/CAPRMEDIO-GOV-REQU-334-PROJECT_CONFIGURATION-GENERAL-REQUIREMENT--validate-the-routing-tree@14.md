---
atom_id: CAPRMEDIO-GOV-REQU-334
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "CAPRMEDIO Routing Tree Validation"
  depends_on:
    - "CAPRMEDIO Routing Tree"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 14
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
---
# Validate the routing tree

the validator **must** reject a routing tree with an invalid schema, unknown target, ambiguous precedence, duplicate route identity, **or** authority effect that is **not** explicitly declared.
