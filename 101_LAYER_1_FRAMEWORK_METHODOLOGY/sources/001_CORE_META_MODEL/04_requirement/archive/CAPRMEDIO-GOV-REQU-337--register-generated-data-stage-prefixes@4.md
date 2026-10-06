---
cce_version: cce_1
cce_form: definition
subjects:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-23 12:02:00
relations:
  child_of:
    - CAPRMEDIO-META-REQU-150--keep-data-stages-orthogonal-to-artifact-semantics
---
# Register generated-data stage prefixes

GOVERNANCE MUST register this ordered vocabulary for generated-data pipeline stages:

| Prefix | Stage meaning |
| --- | --- |
| `src` | Canonical NDJSON Journal input; authority comes from the Journal, not the prefix. |
| `stg` | Deterministic, lossless TOON projection of a bounded `src` frontier. |
| `mrt` | Consumer-ready semantic Projection, including Requirement groupings by scope and tier or Mermaid relation maps. |
| `biz` | Aggregated CAPRMEDIO artifact and implementation metrics, including point-in-time snapshots and historical trends. |

Dependencies MUST move forward through `src → stg → mrt → biz`; a stage MAY depend on any earlier registered stage but MUST NOT depend on a later stage. These prefixes classify Journal inputs and generated Projections only. Unregistered stage prefixes remain available for later governed extension.
