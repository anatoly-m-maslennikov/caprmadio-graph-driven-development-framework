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
      - Atom/Claim
      - Atom/Current Scope/Owner
      - Atom/Current Scope/Governed Subject Set
      - Atom/Claim Scope
      - Claim Value Set
      - Property
      - Entity Graph Projection
      - IS_ALLOWED_VALUE_OF
version: 3
updated_at: 2026-09-02 01:12:00 +0400
relations:
  evaluation_for:
    - CA-M-238
---
# Report Only Exact Consolidation Candidates

## Test case

provide one active Source frontier containing: two mechanically parseable
single-value Claims with the same Current Scope Owner, Governed Subject Set,
Claim Scope, Property, **and** qualifiers but different unique values; one semantically similar prose Claim;
one Claim with a different qualifier; **and** one unparseable Claim.
place one Claim that differs from a qualifying Claim **only** by its location **in** one child Scope Unit frontier.

pass **only** **when** the Tool reports **`=1`** consolidation candidate containing
the two qualifying Atom IDs **and** one proposed `Property: (A, B)` Claim, reports no
candidate from the other Claims, **and** leaves **every** Source carrier unchanged.
the child Scope Unit Claim **must not** enter the candidate.
fail **when** candidate membership depends on semantic inference, **any** required
identity is missing, an ineligible Claim is included, an eligible Claim is
omitted, **or** **any** Source carrier is mutated.
