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
      - Atom/Claim Scope
      - Claim Value Set
      - Property
version: 1
updated_at: 2026-09-01 22:40:10 +0400
relations:
  evaluation_for:
    - CA-R-1358
    - CA-R-1359
---
# Report Exact Claim Value-Set Consolidation Candidates

the Evaluation **must** report one Claim Value Set consolidation candidate **only** **if** every contributing active Atom has the same Current Scope, Claim Scope, Property, **and** exact qualifiers, has one mechanically parseable single-value Claim, **and** differs **only** by one unique allowed value of that Property; it **must not** mutate, merge, archive, replace, compile, **or** otherwise change a Source Atom, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation to fail.
