---
atom_id: CA-R-1200
cce_version: cce_1
cce_form: definition
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Relation Kind"
    - "Atom"
    - "Subject"
    - "Process"
    - "Atom/Content Role: Plan/Type: Task"
version: 7
updated_at: "2026-09-13 02:05:21 +0400"
relations: {}
---
# Define DEPENDS_ON Subject Relation Kind

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** the canonical Entity, Action, **or** Process that its Claim requires **without** making the Atom authoritative about that target. it does **not** establish Process control flow **or** an execution order; Task prerequisite relations remain separately governed by CA-R-1007 **and** CA-R-1026.
