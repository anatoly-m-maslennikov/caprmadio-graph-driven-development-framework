---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Projection"
    - "Implementation"
    - "Entity"
    - "Relation"
    - "Journal"
    - "Atom/Revision"
version: 5
updated_at: "2026-09-23 14:52:21 +0000"
status: Draft
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CAPRMEDIO-META-REQU-657", "CA-R-1568", "CA-R-1494"]}
---
# Summary

Define Realization Graph

## Claim

Realization Graph **means** a non-authoritative Projection of entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.

- the declared selection identifies the exact Implementation inputs **and** evidence actually used; represented facts retain traceability **to** those inputs under CAPRMEDIO-META-REQU-657.
- include existing Journal records **and** Atom Revisions **when** selected **and** relevant. legacy Implementation does **not** need pre-existing RMED **or** Journals **before** this Projection can be built; missing evidence remains identified rather than invented.
- its Artifact kind is Projection. delivery as an Implementation output follows CA-R-1568 **without** turning its contents into an Atom **or** governing authority.
