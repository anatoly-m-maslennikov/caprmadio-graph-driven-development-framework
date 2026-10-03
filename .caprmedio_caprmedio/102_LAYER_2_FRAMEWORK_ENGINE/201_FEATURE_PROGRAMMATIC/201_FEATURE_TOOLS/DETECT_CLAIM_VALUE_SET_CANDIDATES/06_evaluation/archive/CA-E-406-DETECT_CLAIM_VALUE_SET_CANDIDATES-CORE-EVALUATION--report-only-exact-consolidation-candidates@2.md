---
atom_id: CA-E-406
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim Value Set Consolidation Candidate Detection Evaluation
  depends_on:
    continuant:
      - Claim Value Set Consolidation Candidate Evaluation
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES
      - Atom/Current Scope
      - Atom/Claim Scope
version: 2
updated_at: 2026-09-02 00:05:00 +0400
relations:
  evaluation_for:
    - CA-M-238
---
# Report Only Exact Consolidation Candidates

## Test case

Provide one active Source frontier containing: two mechanically parseable
single-value Claims with the same Current Scope, Claim Scope, Property, and
qualifiers but different unique values; one semantically similar prose Claim;
one Claim with a different qualifier; and one unparseable Claim.

Pass only when the Tool reports exactly one consolidation candidate containing
both qualifying Atom IDs and one proposed `Property: (A, B)` Claim, reports no
candidate from the other Claims, and leaves every Source carrier unchanged.
Fail when candidate membership depends on semantic inference, any required
identity is missing, an ineligible Claim is included, an eligible Claim is
omitted, or any Source carrier is mutated.
