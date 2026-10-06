---
atom_id: CA-E-403
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim Value Set Consolidation Candidate Evaluation
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Current Scope
      - Atom/Current Scope/Owner
      - Atom/Current Scope/Governed Subject Set
      - Atom/Claim Scope
      - Claim Value Set
      - Property
      - IS_ALLOWED_VALUE_OF
version: 2
updated_at: 2026-09-02 01:12:00 +0400
relations:
  evaluation_for:
    - CA-R-1358
    - CA-R-1359
---
# Report Exact Claim Value-Set Consolidation Candidates

the Evaluation **must** report one Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Current Scope Owner, Governed Subject Set, Claim Scope, Property, **and** exact qualifiers, has one mechanically parseable single-value Claim, **and** differs **only** by one unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
