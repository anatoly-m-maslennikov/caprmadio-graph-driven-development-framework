---
subjects:
  governs: "Claim Value Set Consolidation Candidate Evaluation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Governed Subject"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 9
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  evaluation_for:
    - CA-R-1358
    - CA-R-1359
---
# Report Exact Claim Value-Set Consolidation Candidates

the Evaluation **must** report one Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has one mechanically parseable single-value Claim, **and** differs **only** by one unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
