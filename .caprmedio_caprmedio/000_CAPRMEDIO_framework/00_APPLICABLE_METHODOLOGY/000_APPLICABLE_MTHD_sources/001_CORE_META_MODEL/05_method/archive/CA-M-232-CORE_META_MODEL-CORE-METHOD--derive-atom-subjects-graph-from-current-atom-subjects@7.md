---
atom_id: CA-M-232
cce_version: cce_1
cce_form: method
subjects:
  governs: "Subject Projection Derivation"
  depends_on:
    - "Projection/Type: Atom Subjects Graph"
    - "Atom/Subjects"
    - "Subject Path"
version: 7
updated_at: "2026-09-13 14:31:04 +0400"
relations: {}
---
# Derive Atom Subjects Graph from Current Atom Subjects

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected direct GOVERNS **and** DEPENDS_ON reference with its exact canonical target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.
