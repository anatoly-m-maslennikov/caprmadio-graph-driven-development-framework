---
atom_id: CA-R-1294
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Scope/Scope Unit Set"
version: 9
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Demand Direction without Another Relation Kind

a Demand Atom **must not** introduce a graph relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Scope Scope Unit references determine that direction.
