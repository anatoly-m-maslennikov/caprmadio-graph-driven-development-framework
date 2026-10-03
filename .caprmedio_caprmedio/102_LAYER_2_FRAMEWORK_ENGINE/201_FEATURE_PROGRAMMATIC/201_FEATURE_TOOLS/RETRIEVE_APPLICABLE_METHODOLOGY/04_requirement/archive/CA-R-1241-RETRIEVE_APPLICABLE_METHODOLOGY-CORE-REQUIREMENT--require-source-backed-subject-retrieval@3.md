---
atom_id: CA-R-1241
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Applicable Methodology Retrieval Tool"
  depends_on:
    - "Applicable Methodology/Compilation Output"
version: 3
updated_at: 2026-08-27 21:45:57 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require Source-Backed Subject Retrieval

the Applicable Methodology Retrieval Tool **must** return only generated projected current RMEDO Atom Carriers that match the exact Subject or Process query through `subjects.governs` or enter its transitive prerequisite closure through `subjects.depends_on`, preserve compilation order, and resolve every returned Carrier to its exact authoritative Source Carrier.
