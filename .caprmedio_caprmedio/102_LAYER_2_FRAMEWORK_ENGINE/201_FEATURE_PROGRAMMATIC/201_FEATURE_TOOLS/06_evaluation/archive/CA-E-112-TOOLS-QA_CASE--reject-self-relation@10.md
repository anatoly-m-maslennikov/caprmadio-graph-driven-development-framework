---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Relation"
    - "CAPRMEDIO Graph"
version: 10
updated_at: "2026-09-17 21:05:28 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-833
    - CA-R-879
    - CA-E-481
    - CA-R-1137
---
# Reject self relation

## Test case

**Fixture:** point an active normative-authority `child_of` Relation from an Atom **to** itself under CA-R-879. this self-edge creates a cycle prohibited by CA-R-833; do **not** infer a universal self-edge prohibition for other graph kinds **or** Relation Kinds.

**Expected result:** Fail with the stable self-relation diagnostic **and** a non-zero exit.
