---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Hub Atom"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Type"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Global Tier"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1579", "CA-R-1534"]}
---
# Define Hub Atom as a derived description

Hub Atom **means** a derived description of an Atom with **>0** outgoing `DECOMPOSES_INTO` Relations; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. related Atoms retain their own Claims rather than becoming parts of the Hub Claim.
