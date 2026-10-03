---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Artifact/Carrier"
version: 10
updated_at: "2026-09-17 21:05:15 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1136
---
# Return deterministic carrier diagnostics

## Test case

**Fixture:** Run the malformed-filename fixture defined by CA-E-073 twice with the same settings **and** source frontier.

**Expected result:** Return identical ordered diagnostics **and** exit status on both runs.
