---
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    - "Single Source of Truth"
    - "Projection"
    - "Atom"
    - "Atom/Claim"
    - "Structural Entity"
    - "Journal"
    - "Relation"
version: 3
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
---
# Keep secondary graphs derived from source authority

secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.

storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.
