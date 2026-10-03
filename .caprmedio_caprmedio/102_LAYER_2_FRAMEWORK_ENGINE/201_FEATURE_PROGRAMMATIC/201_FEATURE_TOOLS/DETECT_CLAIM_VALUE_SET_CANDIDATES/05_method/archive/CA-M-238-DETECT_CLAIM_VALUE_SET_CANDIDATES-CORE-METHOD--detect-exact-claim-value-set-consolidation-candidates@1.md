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
      - Atom/Current Scope
      - Atom/Claim Scope
version: 1
updated_at: 2026-09-01 22:40:10 +0400
relations:
  method_for:
    - CA-R-1358
---
# Detect Exact Claim Value-Set Consolidation Candidates

**to** detect Claim Value Set consolidation candidates, the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** inspect one caller-supplied active Source frontier with one supplied Current Scope **and** Claim Scope, parse **only** exact single-statement Claims in the form `<Property>: <Value>[ **if** <Qualifier>].`, group exact fingerprints, report every contributing Atom ID **and** one proposed `Property: (A, B, C)` Claim, **and** report no candidate for unparseable **or** semantically similar prose.
