---
atom_id: CAPRMEDIO-GOV-REQU-768
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767-CORE_META_MODEL-CORE-REQUIREMENT--keep-rmed-to-rmed-relations-within-active-authority
---
# Validate RMED-to-RMED Relation Target Status

a relation validator **must** apply the Active-target restriction **only** **when** the source Atom is Active **and** the source **and** target Atoms have Content Role **in** (Requirement, Method, Evaluation, Delivery), resolving the target Status from its canonical lifecycle placement.
