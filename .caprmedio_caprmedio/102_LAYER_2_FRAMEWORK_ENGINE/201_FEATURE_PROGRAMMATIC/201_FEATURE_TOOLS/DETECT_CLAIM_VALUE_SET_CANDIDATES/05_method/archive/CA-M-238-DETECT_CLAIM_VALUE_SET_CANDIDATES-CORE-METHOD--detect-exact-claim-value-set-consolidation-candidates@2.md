---
atom_id: CA-M-238
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Claim Value Set Consolidation Candidate Detection
  depends_on:
    continuant:
      - Claim Value Set Consolidation Candidate Evaluation
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES
      - Atom/Current Scope/Owner
      - Atom/Current Scope/Governed Subject Set
      - Atom/Claim Scope
      - Property
      - Entity Graph Projection
      - IS_ALLOWED_VALUE_OF
version: 2
updated_at: 2026-09-02 01:12:00 +0400
relations:
  method_for:
    - CA-R-1358
---
# Detect Exact Claim Value-Set Consolidation Candidates

**to** detect Claim Value Set consolidation candidates, the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** inspect one Scope Unit's local active Atom frontier **without** its child Scope Unit frontiers, derive **every** Atom's Governed Subject Set from its GOVERNS Subjects, derive its Claim Scope from the Property **in** one exact `<Property>: <Value>[ **if** <Qualifier>].` Claim, accept a value **only** **if** one supplied Entity Graph Projection proves its IS_ALLOWED_VALUE_OF relation for that Property, group **only** identical Current Scope Owner, Governed Subject Set, Claim Scope, Property, **and** qualifier coordinates, report **every** contributing Atom ID **and** one proposed `Property: (A, B, C)` Claim, **and** report no candidate for unparseable, unproven, **or** semantically similar prose.
