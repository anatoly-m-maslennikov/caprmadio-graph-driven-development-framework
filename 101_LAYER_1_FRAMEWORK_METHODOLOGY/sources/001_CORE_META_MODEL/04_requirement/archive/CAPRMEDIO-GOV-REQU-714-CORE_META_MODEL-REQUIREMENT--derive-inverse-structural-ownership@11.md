---
atom_id: CAPRMEDIO-GOV-REQU-714
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
cce_version: cce_1
cce_form: obligation
version: 11
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706
---
# Derive inverse structural ownership

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.
