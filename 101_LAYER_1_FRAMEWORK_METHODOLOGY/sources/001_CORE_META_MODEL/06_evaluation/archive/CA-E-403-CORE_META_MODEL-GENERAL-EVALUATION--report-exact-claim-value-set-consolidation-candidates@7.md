---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Claim Value Set Consolidation Candidate Evaluation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Governed Subject"
    - "Atom/Claim/Scope"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 7
updated_at: "2026-09-15 21:31:49 +0000"
relations:
  evaluation_for:
    - CA-R-1358
    - CA-R-1359
---
# Report Exact Claim Value-Set Consolidation Candidates

the Evaluation **must** report one Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Scope, Property, **and** exact qualifiers, has one mechanically parseable single-value Claim, **and** differs **only** by one unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
