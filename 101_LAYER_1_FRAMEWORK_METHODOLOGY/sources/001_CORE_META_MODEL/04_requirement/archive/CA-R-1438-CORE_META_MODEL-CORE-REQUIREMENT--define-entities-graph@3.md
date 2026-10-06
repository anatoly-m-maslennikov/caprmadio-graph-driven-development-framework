---
atom_id: CA-R-1438
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Projection/Type: Entities Graph"
  depends_on:
    - "Projection"
    - "Entity"
    - "Relation Kind"
    - "Relation"
    - "CAPRMEDIO Graph"
version: 3
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
---
# Define Entities Graph

Entities Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Entity nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CAPRMEDIO-META-REQU-657.

admitted external graph **or** source references under CA-R-1472 do **not** become native Entity nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
