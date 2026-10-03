---
atom_id: CAPRMEDIO-META-REQU-657
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact"
    - "Artifact/Revision"
    - "Atom"
    - "Atom/Claim"
    - "Scope Unit"
    - "Journal"
version: 11
updated_at: "2026-09-13 13:05:58 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63
relations: {}
---
# Define Projection Artifact form

a Projection **means** a non-authoritative generated view reproducibly derived from its declared selection of authoritative sources **or** other Projections. source authority is determined per fact: Atoms carry governing Claims, Scope Units supply their observed structural facts, **and** Journals preserve recorded historical facts; other admitted source kinds retain the authority established for their facts by applicable governing Claims.

**every** represented fact retains traceability through **any** upstream Projections **to** its appropriate authoritative sources. a Projection's source specification governs the Projection's required behavior **without** making its derived contents authoritative. multiple Projections of the same source facts, further derived views, **and** the choice of generation mechanism do **not** create another independent authority for those facts.

the declared selection identifies the sources actually used; it does **not** require **every** Projection **to** consume **every** source kind **or** persist a universal source frontier. the registered provenance obligations under CAPRMEDIO-META-REQU-166 remain applicable.
