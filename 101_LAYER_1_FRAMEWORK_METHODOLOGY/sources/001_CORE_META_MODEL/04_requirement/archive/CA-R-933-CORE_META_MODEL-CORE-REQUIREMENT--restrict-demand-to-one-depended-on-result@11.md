---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
atom_id: CA-R-933
cce_version: cce_1
cce_form: obligation
version: 11
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-R-932
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
