---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Artifact/Carrier"
version: 10
updated_at: "2026-09-17 21:05:20 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Propagate Atom filename diagnostics

## Test case

**Fixture:** Add one carrier that fails the malformed-filename fixture defined by CA-E-073 while leaving the rest of the project valid.

**Expected result:** Fail with the propagated malformed-filename diagnostic **and** a non-zero exit.
