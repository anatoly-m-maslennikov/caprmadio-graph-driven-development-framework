---
atom_id: CA-R-1276
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Relation Kind"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 6
updated_at: "2026-09-13 02:05:21 +0400"
relations: {}
---
# Type Every Direct Subject Reference

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.
