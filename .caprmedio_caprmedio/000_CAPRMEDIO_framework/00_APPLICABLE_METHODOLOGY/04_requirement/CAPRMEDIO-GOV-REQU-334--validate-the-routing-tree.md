---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - CAPRMEDIO Routing Tree Validation
  depends_on:
    continuant:
      - CAPRMEDIO Routing Tree
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 9
updated_at: 2026-08-30 16:32:06 +0400
relations:
  child_of:
    - CA-R-1054
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-334--validate-the-routing-tree.md
---
# Validate the routing tree

GOVERNANCE **must** reject a routing tree with an invalid schema, unknown target, ambiguous precedence, duplicate route identity, **or** authority effect that is **not** explicitly declared.
