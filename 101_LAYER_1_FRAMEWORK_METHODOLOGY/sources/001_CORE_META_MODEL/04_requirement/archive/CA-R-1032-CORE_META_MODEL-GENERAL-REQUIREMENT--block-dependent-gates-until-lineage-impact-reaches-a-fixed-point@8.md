---
atom_id: CA-R-1032
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
    - "lifecycle-traceability"
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Block dependent gates until Lineage Impact reaches a fixed point

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
