---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Revision/Updated At"
  depends_on:
    - "Atom/Revision"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Subjects"
    - "Artifact/Carrier"
    - "Relation"
version: 2
updated_at: "2026-09-17 02:03:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1492
    - CA-R-1415
    - CA-R-1433
---
# Check Updated At preservation during formatting changes

the Evaluation **must** fail **if** **any** of these conditions is observed:

- a formatting-only change changes the Atom's Updated At value.
- a lossless Subject serialization migration changes Updated At despite preserving the canonical targets **and** Relation meanings.
- a changed Claim, Summary, applicability, Content Role, Type, Subject target, **or** authored Relation meaning is accepted as a formatting-only change.
- timestamp preservation is treated as permission **to** omit a required Version increment **or** discard the exact prior Carrier.

valid cases include whitespace **or** markup normalization **and** lossless conversion from temporal Subject nesting **to** flat direct references. compare their **before** **and** **after** Claim content, interpreted Property values, references, **and** Relation meanings; require the same Updated At value **and** apply the independent Revision rules. an ambiguous change does **not** establish a passing formatting-only case.
