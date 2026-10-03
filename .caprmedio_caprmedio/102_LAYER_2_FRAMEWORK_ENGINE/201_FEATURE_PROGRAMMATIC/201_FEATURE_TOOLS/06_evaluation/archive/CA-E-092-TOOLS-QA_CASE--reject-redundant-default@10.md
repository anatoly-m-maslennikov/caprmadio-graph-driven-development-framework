---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Property"
    - "Artifact/Property/Default"
    - "Markdown Atom Carrier/YAML Frontmatter/Default"
version: 10
updated_at: "2026-09-17 20:52:52 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-D-278
    - CA-R-1136
---
# Reject redundant default

## Test case

**Fixture:** persist a Markdown Atom Frontmatter Property whose resolved value **=** its applicable registered default **and** whose omission preserves value-selection **and** inheritance behavior under CA-D-278. also include an explicit override equal **to** the inherited value but whose omission would change later inheritance; equality alone **must not** make that override redundant.

**Expected result:** reject the redundant first fixture with the stable redundant-default diagnostic **and** a non-zero exit. do **not** reject the behavior-preserving explicit override as redundant merely because its present value **=** the inherited value.
