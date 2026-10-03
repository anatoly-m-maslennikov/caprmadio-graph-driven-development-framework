---
atom_id: CA-R-1363
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Atom/Governed Subject"
  depends_on:
    - "Atom/Subjects"
    - "GOVERNS"
    - "Subject"
    - "Relation Kind"
    - "Entity"
    - "Action"
    - "Process"
    - "Atom/Claim"
version: 6
updated_at: "2026-09-14 04:00:22 +0400"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
---
# Define Atom Governed Subject

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Entity, Action, **or** Process governed by the Atom's Claim; the Relation **and** its target are distinct.
