---
atom_id: CAPRMEDIO-GOV-REQU-767
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
cce_version: cce_1
cce_form: obligation
version: 13
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-R-1051
---
# Keep RMED-to-RMED Relations within Active Authority

**if** a direct relation is authored by an Active Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Active.
