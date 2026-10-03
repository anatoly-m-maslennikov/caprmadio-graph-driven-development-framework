---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Atom/Type"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-17 20:52:46 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-D-267
    - CA-R-1136
---
# Reject stored Type

## Test case

**Fixture:** persist the Type **in** frontmatter **when** the registered Type segment of the canonical filename derives it completely **and** unambiguously under CA-D-267.

**Expected result:** fail with the stable derived-frontmatter-fact diagnostic **and** a non-zero exit.
