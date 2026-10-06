---
cce_version: cce_1
cce_form: restriction
subjects:
  governs: "Applicable Methodology/Member Selection"
  depends_on:
    - "Atom/Content Role"
    - "Entity/Type/Status"
version: 11
updated_at: 2026-09-15 05:51:38
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Select Only Current Active RMEDO Atom Revisions

the Applicable Methodology membership **must** contain **only** current Atom Revisions whose type-qualified Status **`=`** Active **and** whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations).
