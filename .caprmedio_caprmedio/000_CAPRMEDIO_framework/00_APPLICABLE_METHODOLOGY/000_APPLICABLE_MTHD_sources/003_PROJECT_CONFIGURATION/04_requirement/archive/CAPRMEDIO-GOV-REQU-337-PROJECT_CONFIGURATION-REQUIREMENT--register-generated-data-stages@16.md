---
subjects:
  governs: "Generated Data Stage Prefix"
  depends_on:
    - "artifact-catalog"
version: 16
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-150
---
# Register generated-data stages

the following ordered generated-data pipeline stages **must** be registered, referenced by their Carrier prefixes governed by CA-D-388:

| Stage reference | Stage meaning |
| --- | --- |
| `src` | canonical Journal input; authority comes from the Journal, **not** the prefix. |
| `stg` | deterministic, lossless Projection of a bounded `src` frontier. |
| `mrt` | consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |
| `biz` | aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |

dependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.
