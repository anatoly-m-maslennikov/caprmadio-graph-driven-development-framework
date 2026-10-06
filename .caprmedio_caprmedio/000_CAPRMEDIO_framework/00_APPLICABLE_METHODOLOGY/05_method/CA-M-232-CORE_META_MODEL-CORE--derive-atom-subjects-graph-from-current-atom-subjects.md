---
subjects:
  governs: "Subject Projection Derivation"
  depends_on:
    - "Projection/Type: Atom Subjects Graph"
    - "Atom/Subjects"
    - "Subject Path"
    - "Subject"
    - "Atom"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-232"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md
  source_atom_id: CA-M-232
  source_atom_revision: 12
  source_sha256: 01e1f3355f52762beabcc19fe30746a536c12f79015f581d00b6ff765a202cd7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Subject as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details
